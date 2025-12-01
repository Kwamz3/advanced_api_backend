from fastapi import APIRouter, HTTPException, Query, status

from app.core.mockDB import user_db

router = APIRouter()


async def get_all_users():
    
    return{
        "success": True,
        "data": user_db
    }