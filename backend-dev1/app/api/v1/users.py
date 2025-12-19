from fastapi import APIRouter, HTTPException, Depends, status, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy import text, select, insert, update, delete, func
from jose import JWTError

from app.core.database import get_db
from app.models.users import UserRole, UserUpdate, UserCreate, User
from app.models.movies import WatchListBase, WatchListItem
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
    user_id: str,
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
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role.value if user.role is not None else None,
                "status": user.status.value if user.status is not None else None,
                "service": user.service.value if user.service is not None else None,
                "profile_picture": user.profile_picture,
                "date_of_birth": user.date_of_birth.isoformat() if user.date_of_birth is not None else None,
                "gender": user.gender.value if user.gender is not None else None,
                "bio": user.bio,
                "address": user.address,
                "location": user.location,
                "is_email_verified": user.is_email_verified.value if user.is_email_verified is not None else None,
                "is_phone_verified": user.is_phone_verified.value if user.is_phone_verified is not None else None,
                "preferences": user.preferences,
                "notification_settings": user.notification_settings,
                "created_at": user.created_at.isoformat() if user.created_at is not None else None,
                "updated_at": user.updated_at.isoformat() if user.updated_at is not None else None
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
        new_user = User(
            phone= create_user.phone,
            email= create_user.email,
            first_name= create_user.first_name,
            last_name= create_user.last_name,
            role= create_user.role,
            status= create_user.status,
            service= create_user.service_status,
            profile_picture= create_user.profile_picture,
            date_of_birth= create_user.date_of_birth,
            gender= create_user.gender,
            bio= create_user.bio,
            location= create_user.location,
            address= create_user.address,
            is_email_verified= create_user.is_email_verified,
            is_phone_verified= create_user.is_phone_verified,
            preferences= create_user.preferences,
            notification_settings= create_user.notification_settings
        )
        
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        
        user_count = await db.execute(select(func.count(User.id)))
        
        return{
            "success": True,
            "message": "New user created successfully",
            "data": {
                "id": new_user.id,
                "phone": new_user.phone,
                "email": new_user.email,
                "first_name": new_user.firstName,
                "last_name": new_user.lastName,
                "role": new_user.role.value if new_user.role is not None else None,
                "status": new_user.status.value if new_user.status is not None else None,
                "service": new_user.service.value if new_user.service is not None else None,
                "profile_picture": new_user.profilePicture,
                "date_of_birth": new_user.date_of_birth.isoformat() if new_user.date_of_birth is not None else None,
                "gender": new_user.gender.value if new_user.gender is not None else None,
                "bio": new_user.bio,
                "address": new_user.address,
                "location": new_user.location,
                "is_email_verified": new_user.is_email_verified.value if new_user.is_email_verified is not None else None,
                "is_phone_verified": new_user.is_phone_verified.value if new_user.is_phone_verified is not None else None,
                "preferences": new_user.preferences,
                "notification_settings": new_user.notification_settings,
                "created_at": new_user.created_at.isoformat() if new_user.created_at is not None else None,
                "updated_at": new_user.updated_at.isoformat() if new_user.updated_at is not None else None
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
    user_id: str,
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
        
        return {
            "success": True,
            "message": "Profile updated successfully",
            "data": {
                "id": existing_user.id,
                "phone": existing_user.phone,
                "email": existing_user.email,
                "first_name": existing_user.first_name,
                "last_name": existing_user.last_name,
                "role": existing_user.role.value if existing_user.role is not None else None,
                "status": existing_user.status.value if existing_user.status is not None else None,
                "profile_picture": existing_user.profile_picture,
                "gender": existing_user.gender.value if existing_user.gender is not None else None,
                "bio": existing_user.bio,
                "service": existing_user.service.value if existing_user.service is not None else None,
                "watch_list": existing_user.watch_list,
                "location": existing_user.location,
                "address": existing_user.address,
                "is_email_verified": existing_user.is_email_verified.value if existing_user.is_email_verified is not None else None,
                "is_phone_verified": existing_user.is_phone_verified.value if existing_user.is_phone_verified is not None else None,
                "preferences": existing_user.preferences,
                "notification_settings": existing_user.notification_settings,
                "created_at": existing_user.created_at.isoformat() if existing_user.created_at is not None else None,
                "updated_at": existing_user.updated_at.isoformat() if existing_user.updated_at is not None else None
            }
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
    user_id: str,
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
    user_id: str,
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
            
        result = await db.execute(
            select(WatchListBase).filter(
            WatchListBase.user_id == user_id,
            WatchListBase.movie_id == add_movie.movie_id
            )
                )
            
        existing_entry = result.scalar_one_or_none()
        
        if existing_entry:
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail= "Movie already in watchlist"
            )
            
        new_watchlist_item = WatchListBase(
            user_id = user_id,
            movie_id = add_movie.movie_id
        )
        
        db.add(new_watchlist_item)
        
        await db.commit()
        await db.refresh(new_watchlist_item)
        
        return{
            "success": True,
            "message": "Movie added successfully to watchlist",
            "data": new_watchlist_item
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
    user_id: str,
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
    user_id: str,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    
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
    