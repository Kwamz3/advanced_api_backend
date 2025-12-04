from fastapi import APIRouter, HTTPException, Depends, status, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy import text, select, insert, update, delete
from jose import JWTError

from app.core.database import get_db
from app.models.users import UserUpdate, UserCreate, WatchListItem
from app.core.security import verify_token
from app.core.mockDB import user_db, movies_db

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


@router.get("/")
async def get_all_users():
    
    return {
        "success": True,
        "data": user_db
    }

@router.get("/profile/{user_id}")
async def get_user_profile(
    user_id: int
):
    padded_id = f'{user_id:03d}'
    
    try:
        user = next(
        (u for u in user_db if u["id"] == padded_id),
        None
    )
                
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
    
        return{
            "success": True,
            "data": {
                "id": user["id"],
                "phone": user["phone"],
                "email": user["email"],
                "firstName": user["firstName"],
                "lastName": user["lastName"],
                "role": user["role"],
                "status": user["status"],
                "service": user["service"],
                "profilePicture": user["profilePicture"],
                "dateOfbirth": user["dateOfbirth"],
                "gender": user["gender"],
                "bio": user["bio"],
                "address": user["address"],
                "isEmailVerified": user["isEmailVerified"],
                "isPhoneVerified": user["isPhoneVerified"],
                "preferences": user["preferences"],
                "notificationSettings": user["notificationSettings"],
                "createdAt": user["createdAt"],
                "updatedAt": user["updatedAt"]
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
    # user_id: int,
    create_user: UserCreate = Query(..., description= "create new user")
):
    new_id = str(max((int(item["id"]) for item in user_db), default=0) + 1).zfill(3)
       
       
    from datetime import datetime
    
    new_user = {
        "id": new_id,
        "phone": create_user.phone,
        "email": create_user.email,
        "firstName": create_user.firstName,
        "lastName": create_user.lastName,
        "role": create_user.role,
        "status": create_user.status,
        "service": create_user.serviceStatus,
        "profilePicture": create_user.profilePicture,
        "dateOfbirth": create_user.dateOfbirth.strftime("%Y-%m-%dT%H:%M:%SZ") if create_user.dateOfbirth else None,
        "gender": create_user.gender,
        "bio": create_user.bio,
        "location": create_user.location,
        "address": create_user.address,
        "isEmailVerified": create_user.isEmailVerified,
        "isPhoneVerified": create_user.isPhoneVerified,
        "preferences": create_user.preferences,
        "notificationSettings": create_user.notificationSettings,
        "createdAt": create_user.createdAt.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "updatedAt": create_user.updatedAt.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    
    
    user_db.append(new_user)
    
    return{
        "success": True,
        "message": "New user created successfully",
        "data": new_user
    }
  
    
@router.put("/profile/{user_id}")
async def update_user_profile(
    user_id: int,
    update_user: UserUpdate
):
  
    padded_id = f"{user_id:03d}"
    
    try:
        existing_user = next(
            (u for u in user_db if u["id"] == padded_id),
            None
        )
        
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        data_update = update_user.model_dump(exclude_unset=True)
        
        for key, value in data_update.items():
            if key in existing_user:
                existing_user[key] = value
        
        from datetime import datetime
        existing_user["updatedAt"] = datetime.now().isoformat()
        
        return {
            "success": True,
            "message": "Profile updated successfully",
            "data": existing_user
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update user profile: {str(e)}"
        )
        
@router.get("/watchlist/user/{user_id}")
async def get_watchlist(
    user_id: int
):
    
    padded_id = f'{user_id:03d}'
    
    user_watchlist = next(
        (u for u in user_db if u["id"] == padded_id)
    )
    
    if not user_watchlist:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Watchlist not found"
        )
        
    return{
        "success": True,
        "data": user_watchlist["watchlist"]
    }


@router.post("/watchlist/user/{user_id}")        
async def add_to_watchlist(
    user_id: int,
    add_movie: WatchListItem
):
    padded_id = f'{user_id:03d}'
    
    try:
        user = next(
            (u for u in user_db if u["id"] == padded_id),
            None
        )
        
        if not user:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
            
        if any(
            w["id"] == add_movie.movie_id for w in user["watchlist"]
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
    