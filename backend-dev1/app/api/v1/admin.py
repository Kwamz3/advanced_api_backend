from fastapi import APIRouter, HTTPException, Query, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.movies import CreateMovieMock, MovieList
from app.models.users import UserCreate, User 
from app.models.admin import AccountApproval, AccountBan, Status
from app.core.database import get_db
from sqlalchemy import func

router = APIRouter()

@router.get("/dashboard")
async def admin_dashboard(
    db: AsyncSession = Depends(get_db)
):
    
    # Count total users
    user_count_result = await db.execute(select(func.count(User.id)))
    total_users = user_count_result.scalar()
    
    # Count total movies
    movie_count_result = await db.execute(select(func.count(MovieList.id)))
    total_movies = movie_count_result.scalar()
    
    return{
        "Number of movies": str(total_movies),
        "Number of users": str(total_users)
    }
    

@router.get("/dashboard/users")
async def get_all_users(
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(select(User))
    users = result.scalars().all()
    
    return{
        "success": True,
        "data": [{
            "id": user.id,
            "phone": user.phone,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role.value if user.role is not None else None,
            "status": user.status.value if user.status is not None else None,
            "service": user.service.value if user.service is not None else None,
            "profile_picture": user.profile_picture,
            "date_of_birth": user.date_of_birth,
            "gender": user.gender,
            "bio": user.bio,
            "address": user.address,
            "location": user.location,
            "is_email_verified": user.is_email_verified.value if user.is_email_verified is not None else None,
            "is_phone_verified": user.is_phone_verified,
            
        } for user in users]
    }
        
@router.get("/approvals") 
async def get_pending():
     
    pending_accounts= [
        u for u in user_db if u["isEmailVerified"] == "PENDING" or u["isPhoneVerified"] == "PENDING"
    ]
        
    count = len(pending_accounts)
    
    if not pending_accounts:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "No pending accounts"
        )
        
    return{
        "success": True,
        "count": f"You have {count} unapproved accounts",
        "data": pending_accounts
    }

        
         
@router.put("/approvals/{user_id}")
async def account_approval(
    user_id: int,
    user_approval: AccountApproval
):
    padded_id = f'{user_id:03d}'
    
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

@router.put("/bans/{user_id}")
async def account_ban(
    user_id: int,
    user_ban: AccountBan
):
    padded_id = f'{user_id:03d}'
    
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
            detail= f"Failed to ban user: {str(e)}"
        )

@router.get("/serviceStatus")
async def get_serviceStatus():
     
    serviceStatus_accounts= [
        u for u in user_db if u["service"] == "FREE" or u["service"] == "PREMIUM"
    ]
        
    count = len(serviceStatus_accounts)
    
    if not serviceStatus_accounts:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "No modifications recorded"
        )
        
    return{
        "success": True,
        "count": f"You have {count} service modifications",
        "data": serviceStatus_accounts
    }

@router.put("/serviceStatus/{user_id}")
async def service_Status(
    user_id: int,
    user_ban: Status
):
    padded_id = f'{user_id:03d}'
    
    try:
        serviceStatus = next(
            (u for u in user_db if u["id"] == padded_id),
            None
        )
        
        if not serviceStatus:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= "No service modification recorded"
            )
            
        update_data = user_ban.model_dump(exclude_unset=True)
        
        for key, item in update_data.items():
            serviceStatus[key] = item
        
        return{
            "success": True,
            "message": "User account modified successfully",
            "data": {
                "id": serviceStatus["id"],
                "service_status": serviceStatus["service"],
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to modify account: {str(e)}"
        )


@router.get("/users/{user_id}")
async def get_user(
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
    
        return{
            "success": True,
            "data": {
                "id": existing_user["id"],
                "phone": existing_user["phone"],
                "email": existing_user["email"],
                "firstName": existing_user["firstName"],
                "lastName": existing_user["lastName"],
                "role": existing_user["role"],
                "status": existing_user["status"],
                "service": existing_user["service"],
                "profilePicture": existing_user["profilePicture"],
                "dateOfbirth": existing_user["dateOfbirth"],
                "gender": existing_user["gender"],
                "bio": existing_user["bio"],
                "address": existing_user["address"],
                "isEmailVerified": existing_user["isEmailVerified"],
                "isPhoneVerified": existing_user["isPhoneVerified"],
                "preferences": existing_user["preferences"],
                "notificationSettings": existing_user["notificationSettings"],
                "createdAt": existing_user["createdAt"],
                "updatedAt": existing_user["updatedAt"]
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f"Failed to remove user: {str(e)}"
        )
        
        
@router.delete("/users/{user_id}")
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