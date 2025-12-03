from fastapi import APIRouter, HTTPException, Query, status

from app.core.mockDB import user_db, movies_db
from app.models.movies import CreateMovieMock
from app.models.users import UserCreate

router = APIRouter()

@router.get("/dashboard")
async def admin_dashboard():
    
    max_users = str(max((int(item["id"]) for item in user_db), default=0))
    max_movies = str(max((int(item["id"]) for item in movies_db), default=0))
    
    return{
        "Number of movies": max_movies,
        "Number of users": max_users
    }
    

@router.get("/dashboard/users")
async def get_all_users():
    
        return{
        "success": True,
        "data": user_db
    }
        
 
@router.delete("dashboard/{user_id}")
async def remove_user(
  user_id : int,
  remove_this_user: UserCreate  
):
    
    padded_id = f'{user_id:03d}'
    
    try:
        existing_user = next(
            (u for u in user_db if u["id"] == padded_id)
        )
        
        if not existing_user:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
        
        data_update = remove_this_user.model_dump(exclude_unset=True)
        
        user_db.remove(data_update)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to remove user: {str(e)}"
        )