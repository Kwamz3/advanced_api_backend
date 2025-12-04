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
        
 
@router.put("/dashboard/{user_id}/account_approval")
async def account_approval(
    user_id: int,
    user_approval: UserCreate
):
    padded_id = f'{user_db:03d}'
    
    try:
        unapproved_account = next(
            (u for u in user_db if u["id"] == padded_id),
            None
        )
        
        if not unapproved_account:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "No account pending approval"
            )
            
        update_data = user_approval.model_dump(exclude_unset=True)
        
        for key, item in update_data.items():
            unapproved_account[key] = item
        
        return{
            "success": True,
            "message": "Account approved successfully",
            "data": {
                "id": unapproved_account["id"],
                "isEmailVerified": unapproved_account["isEmailVerified"],
                "isPhoneVerified": unapproved_account["isPhoneVerified"],
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to approve unapproved accounts: {str(e)}"
        )

@router.put("/dashboard/{user_id}/account_ban")
async def account_ban(
    user_id: int,
    user_ban: UserCreate
):
    padded_id = f'{user_db:03d}'
    
    try:
        ban_account = next(
            (u for u in user_db if u["id"] == padded_id),
            None
        )
        
        if not ban_account:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "No account pending approval"
            )
            
        update_data = user_ban.model_dump(exclude_unset=True)
        
        for key, item in update_data.items():
            ban_account[key] = item
        
        return{
            "success": True,
            "message": "User account ban successfully",
            "data": {
                "id": ban_account["id"],
                "status": ban_account["status"],
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to approve unapproved accounts: {str(e)}"
        )


@router.delete("dashboard/{user_id}")
async def remove_user(
    user_id : int
):
    
    padded_id = f'{user_id:03d}'
    
    try:
        existing_user = next(
            (u for u in user_db if u["id"] == padded_id),
            None
        )
        
        if not existing_user:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "User not found"
            )
    
        
        user_db.remove(existing_user)
        return{
            "message": f"User {padded_id} removed successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to remove user: {str(e)}"
        )