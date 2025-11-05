from fastapi import FastAPI, HTTPException, APIRouter, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import text, select,insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from pydantic import BaseModel, field_validator
from datetime import datetime
from jose import JWTError
import uuid

from app.api.v1 import users
from app.core.database import get_db
from app.core.mockDB import movies_db
from app.models.movies import MovieList
from app.core.security import verify_token
from app.core.database import init_db

security = HTTPBearer()
router = APIRouter()
db = get_db()


class CreateMovieMock(BaseModel):
    id : str
    title : str
    category : Optional[str] = None
    description : Optional [str] = None
    poster_url : str
    trailer_url : str
    duration : int
    release_year : int
    rating : float
    cast : str
    producer : str
    is_featured : Optional[bool] = None
    views : Optional[int] = None
    created_at : datetime
    updated_at : datetime
    is_liked : bool
    
    
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
    
 
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    
    token = credentials.credentials
    
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
 
@router.post("/", response_model= dict)       
async def create_movie(
    request: CreateMovieMock,
    current_user: dict = Depends(security)
):      
        # movie_data = {
        #     "id" : str(uuid.uuid4()),
        #     "title" : MovieList.title,
        #     "category" : MovieList.category,
        #     "description" : MovieList.description,
        #     "poster_url" : MovieList.poster_url,
        #     "trailer_url" : MovieList.trailer_url,
        #     "duration " : MovieList.duration,
        #     "poster_url" : MovieList.poster_url,
        #     "release_year" : MovieList.release_year,
        #     "rating" : MovieList.rating,
        #     "cast" : MovieList.cast,
        #     "is_featured" : MovieList.is_featured,
        #     "created_at" : MovieList.created_at,
        #     "updated_at" : MovieList.updated_at,
        #     "is_liked" : MovieList.is_liked
        # }
        
        new_dict = request.model_dump()
        movies_db.append(new_dict)
        
        return {"mesage": "Movie added successfully to mock database", "data": new_dict}
        
        