from fastapi import APIRouter, HTTPException, Depends, status, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy import text, select, insert, update, delete
from jose import JWTError

from app.core.database import get_db
from app.models.user import UserCreate
from app.models.user import UserResponse
from app.core.security import verify_token
from app.core.mockDB import user_db

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


@router.get("/profile")
async def get_user_profile(
    email: str = Query(..., description= "user's email")
):
    
    try:
        user = next(
        (u for u in user_db if u["email"].lower() == email.lower()),
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
                "status": user["status"]
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
    create_user: UserResponse = Query(..., description= "create new User")
):
    existing_user = next(
        (u for u in user_db if u["email"].lower() == create_user.email.lower()),
        None
    )
    
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "User with this email already exists"
        )
        
    new_user = {
        "id": create_user.id,
        "phone": create_user.phone,
        "email": create_user.email,
        "firstName": create_user.firstName,
        "lastName": create_user.lastName,
        "role": create_user.role,
        "status": create_user.status 
    }
    
    user_db.append(new_user)
    
    return{
        "success": True,
        "message": "New user created successfully",
        "data": new_user
    }