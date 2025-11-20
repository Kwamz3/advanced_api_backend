from fastapi import FastAPI, HTTPException, APIRouter, Depends, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import text, select,insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from pydantic import BaseModel, field_validator
from datetime import datetime
from jose import JWTError
import uuid
import json

from app.api.v1 import users
from app.core.database import get_db
from app.core.mockDB import movies_db
from app.models.movies import CreateMovieMock
from app.core.security import verify_token
from app.core.database import init_db

security = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()
db = get_db()


@field_validator('title')
@classmethod
def validate_title(cls, v):
    if len(v) < 5:
        raise ValueError("title has to be atleast 5 characters")
    return v
    
@field_validator('rating')
@classmethod
def validate_rating(cls, v):
    if v > 10.0:
        raise ValueError("rating can not be more than 10.0")
    return v
    
@field_validator('duration')
@classmethod
def validate_duration(cls, v):
    if v < 70:
        raise ValueError("duration can not be less than 1hr 10mins")
    return v
    
 
async def get_current_user(credentials = Depends(security)):
    
    token = credentials
    
    try:
        payload = verify_token(token)
        user_id = payload.get("sub")
        role = payload.get("role")
        
        if user_id is None:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid authenttication token: missing subject (sub)",
                headers= {"WWW-Authentication": "Bearer"}
            )
        
        return {"user": user_id, "role": role}
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Could not validate credentials",
            headers= {"WWW-Authentication": "Bearer"}
        )
 
       
@router.get("/{movie_id}")
async def get_movie_by_id(
    movie_id: str = Query(..., description= "get movie by id")
):
    
    movie = next(
        (u for u in movies_db if u["id"].lower() == '00'+ movie_id.lower()),
        None
    )
    
    if not movie:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "movie not found"
        )
    
    return {
        "success": True,
        "data": movie
    }


@router.post("/create", response_model= dict)       
async def create_movie(
    request: CreateMovieMock = Query(..., description= "add a new movie"),
    current_user: dict = Depends(security)
):      
        
        new_dict = request.model_dump()
        new_dict["id"] = str(uuid.uuid4())
        movies_db.append(new_dict)
        
        return {
            "mesage": "Movie added successfully to mock database",
            "data": new_dict
                }
    
    
@router.get("/", response_model= dict)
async def get_all_movies():
    
    return {
        "success": True,
        "data": movies_db
    }