from fastapi import APIRouter, HTTPException, Query, status

from app.core.mockDB import user_db, movies_db
from app.models.movies import CreateMovieMock

router = APIRouter()

@router.get("/dashboard")
async def admin_dashboard():
    
    max_users = str(max((int(item["id"]) for item in user_db), default=0))
    max_movies = str(max((int(item["id"]) for item in movies_db), default=0))
    
    return{
        "Number of movies": max_movies,
        "Number of users": max_users
    }
    

@router.get("/dashboard/users", response_model= dict[str, list[CreateMovieMock]])
async def get_all_users():
    
        return{
        "success": True,
        "data": user_db
    }