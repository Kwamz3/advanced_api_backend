from fastapi import APIRouter, HTTPException, Depends, status, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy import text, select, insert, update, delete
from jose import JWTError

from app.core.database import get_db
from app.models.users import UserRole, UserUpdate, UserCreate, WatchListItem, User
from app.models.movies import WatchListItem
from app.core.security import verify_token

router = APIRouter()
security = OAuth2PasswordBearer(tokenUrl="token") 

async def get_current_user(credentials: str = Depends(security)):
    
    token = credentials
    
    try:
        payload = verify_token(token)
        user_id = payload.get("sub")
        role = payload.get("role")
        
        if user_id is None:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid authenttication token: missing subject (sub)",
                headers= {"WWW-Authenticate": "Bearer"}
            )
        
        return {"user_id": user_id, "role": role}
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Could not validate credentials",
            headers= {"WWW-Authenticate": "Bearer"}
        )


@router.get("/profile/{user_id}")
async def get_user_profile(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
                
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
    
        return{
            "success": True,
            "data": {
                "id": user.id,
                "phone": user.phone,
                "email": user.email,
                "firstName": user.firstName,
                "lastName": user.lastName,
                "role": user.role.value if user.role is not None else None,
                "status": user.status.value if user.status is not None else None,
                "service": user.service.value if user.service is not None else None,
                "profilePicture": user.profilePicture,
                "dateOfbirth": user.dateOfbirth.isoformat() if user.dateOfbirth is not None else None,
                "gender": user.gender.value if user.gender is not None else None,
                "bio": user.bio,
                "address": user.address,
                "location": user.location,
                "isEmailVerified": user.isEmailVerified.value if user.isEmailVerified is not None else None,
                "isPhoneVerified": user.isPhoneVerified.value if user.isPhoneVerified is not None else None,
                "preferences": user.preferences,
                "notificationSettings": user.notificationSettings,
                "createdAt": user.createdAt.isoformat() if user.createdAt is not None else None,
                "updatedAt": user.updatedAt.isoformat() if user.updatedAt is not None else None
            }
        }          
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to retrieve user: {str(e)}"
        ) 
        

@router.post("/profile")
async def create_user_profile(
    create_user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    try:
        # Create User model instance
        new_user = User(
            phone= create_user.phone,
            email= create_user.email,
            firstName= create_user.firstName,
            lastName= create_user.lastName,
            role= create_user.role,
            status= create_user.status,
            service= create_user.serviceStatus,
            profilePicture= create_user.profilePicture,
            dateOfbirth= create_user.dateOfbirth,
            gender= create_user.gender,
            bio= create_user.bio,
            location= create_user.location,
            address= create_user.address,
            isEmailVerified= create_user.isEmailVerified,
            isPhoneVerified= create_user.isPhoneVerified,
            preferences= create_user.preferences,
            notificationSettings= create_user.notificationSettings
        )
        
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        
        return{
            "success": True,
            "message": "New user created successfully",
            "data": {
                "id": new_user.id,
                "phone": new_user.phone,
                "email": new_user.email,
                "firstName": new_user.firstName,
                "lastName": new_user.lastName,
                "role": new_user.role.value if new_user.role is not None else None,
                "status": new_user.status.value if new_user.status is not None else None,
                "service": new_user.service.value if new_user.service is not None else None,
                "profilePicture": new_user.profilePicture,
                "dateOfbirth": new_user.dateOfbirth.isoformat() if new_user.dateOfbirth is not None else None,
                "gender": new_user.gender.value if new_user.gender is not None else None,
                "bio": new_user.bio,
                "address": new_user.address,
                "location": new_user.location,
                "isEmailVerified": new_user.isEmailVerified.value if new_user.isEmailVerified is not None else None,
                "isPhoneVerified": new_user.isPhoneVerified.value if new_user.isPhoneVerified is not None else None,
                "preferences": new_user.preferences,
                "notificationSettings": new_user.notificationSettings,
                "createdAt": new_user.createdAt.isoformat() if new_user.createdAt is not None else None,
                "updatedAt": new_user.updatedAt.isoformat() if new_user.updatedAt is not None else None
            }
        }
        
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create user: {str(e)}"
        )
  
    
@router.put("/profile/{user_id}")
async def update_user_profile(
    user_id: int,
    update_user: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    
    try:
        result = await db.execute(select(User). filter(User.id == user_id))
        existing_user = result.scalar_one_or_none()
        
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        data_update = update_user.model_dump(exclude_unset=True)
        
        for key, value in data_update.items():
            setattr(existing_user, key, value)
        
        await db.commit()
        await db.refresh(existing_user)
        
        from datetime import datetime
        existing_user.updatedAt = datetime.now()
        
        
        return {
            "success": True,
            "message": "Profile updated successfully",
            "data": existing_user
        }
        
    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update user profile: {str(e)}"
        )
        
@router.get("/watchlist/user/{user_id}")
async def get_watchlist(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):    
        
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
            
        user_watchlist = user.watchlist

        if not user_watchlist or len(user_watchlist) == 0:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "No movies added to watchlist"
            )
            
        return{
            "success": True,
            "data": user_watchlist
        }


@router.post("/watchlist/user/{user_id}")        
async def add_to_watchlist(
    user_id: int,
    add_movie: WatchListItem,
    db: AsyncSession = Depends(get_db)
):
    
    try:
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()
        
        if not user:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
            
        if any(
            ad == add_movie.movie_id for w in user["watchlist"]
            ):
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail= "Movie already in watchlist"
            )
            
        user["watchlist"].append(add_movie.model_dump())
        
        return{
            "success": True,
            "message": "Movie added successfully to watchlist",
            "data": user["watchlist"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to add movie to watchlist: {str(e)}"
        )
     
        
@router.put("/watchlist/user/{user_id}")        
async def remove_movie(
    user_id: int,
    movie_id: str
):
    padded_id = f'{user_id:03d}'
    padded_movieId = f'{movie_id}'
    
    try:
        user = next(
            (u for u in user_db if u["id"] == padded_id)
        )
        
        if not user:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
            
        watchlist = user["watchlist"]  
            
        movie = next(
            (m for m in watchlist if m["id"] == padded_movieId)
        )
        
        if not movie:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "Movie not found in watchlist"
            )
            
        watchlist.remove(movie)
        
        return{
            "success": True,
            "message": "Movie rem"
            
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to remove watchlist: {str(e)}"
        )
        
@router.delete("/watchlist/user/{user_id}")        
async def clear_watchlist(
    user_id: int
):
    
    padded_id = f'{user_id:03d}'
    
    user = next(
        (u for u in user_db if u["id"] == padded_id)
    )
    
    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )
    
    user["watchlist"] = []
    
    return{
        "success": True,
        "message": "Watchlist cleared successfully"
    }
    