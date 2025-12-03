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
        

async def account_approval(
    user_remove: UserCreate
):
    
    try:
        unapproved_account = next(
            (u for u in user_db if u["isEmailVerified"] == "PENDING" or u["isPhoneVerified"] == "PENDING"),
            None
        )
        
        if not unapproved_account:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
        
        return{
            "success": True,
            "data": {
                "id": unapproved_account["id"],
                "phone": unapproved_account["phone"],
                "email": unapproved_account["email"],
                "firstName": unapproved_account["firstName"],
                "lastName": unapproved_account["lastName"],
                "role": unapproved_account["role"],
                "status": unapproved_account["status"],
                "service": unapproved_account["service"],
                "profilePicture": unapproved_account["profilePicture"],
                "dateOfbirth": unapproved_account["dateOfbirth"],
                "gender": unapproved_account["gender"],
                "bio": unapproved_account["bio"],
                "address": unapproved_account["address"],
                "isEmailVerified": unapproved_account["isEmailVerified"],
                "isPhoneVerified": unapproved_account["isPhoneVerified"],
                "preferences": unapproved_account["preferences"],
                "notificationSettings": unapproved_account["notificationSettings"],
                "createdAt": unapproved_account["createdAt"],
                "updatedAt": unapproved_account["updatedAt"]
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to approve unapproved accounts: {str(e)}"
        )