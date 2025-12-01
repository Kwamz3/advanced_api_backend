from fastapi import APIRouter, HTTPException, Query, status

from app.core.mockDB import user_db
from app.models.movies import CreateMovieMock

router = APIRouter()


@router.get("/", response_model= dict[str, list[CreateMovieMock]])
async def get_all_users():
    
        return{
        "success": True,
        "data": user_db
    }