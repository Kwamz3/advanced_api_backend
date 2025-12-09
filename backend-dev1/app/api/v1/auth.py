"""
Authentication endpoints for OTP-based email verification
"""

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.security import (
    generate_otp,
    store_otp,
    verify_otp,
    send_otp_via_email,
    create_user_token,
    create_refresh_token,
    cleanup_expired_otps
)
from app.models.users import User, UserRole, UserStatus, VerifyStatus
from app.models.auth import OTPResponse, EmailRequest, TokenResponse, OTPVerifyRequest

router = APIRouter()



@router.post("/send-otp", response_model=OTPResponse, status_code=status.HTTP_200_OK)
async def send_otp(request: EmailRequest, db: AsyncSession = Depends(get_db)):
    """
    Send OTP to email for verification.
    Creates user if doesn't exist.
    """
    # Clean up expired OTPs first
    cleanup_expired_otps()
    
    email = request.email
    
    # Check if user exists, create if not
    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        # Create new user with minimal info
        user = User(
            email=email,
            role=UserRole.CLIENT,
            status=UserStatus.INACTIVE,
            isPhoneVerified=VerifyStatus.NOT_SUBMITTED
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
    
    # Generate and store OTP
    otp_code = generate_otp()
    store_otp(email, otp_code)
    
    # Send OTP via Email
    email_sent = send_otp_via_email(email, otp_code)
    
    if not email_sent:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP. Please try again."
        )
    
    from app.core.config import settings
    return OTPResponse(
        message="OTP sent successfully",
        email=email,
        expires_in_minutes=settings.OTP_EXPIRE_IN_MINS
    )


@router.post("/verify-otp", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def verify_otp_endpoint(request: OTPVerifyRequest, db: AsyncSession = Depends(get_db)):
    """
    Verify OTP and return access token.
    Marks email as verified and activates user account.
    """
    email = request.email
    otp = request.otp
    
    # Verify OTP
    try:
        is_valid = verify_otp(email, otp)
    except HTTPException:
        raise
    
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP"
        )
    
    # Get user
    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Update user verification status
    user.isPhoneVerified = VerifyStatus.APPROVED
    user.status = UserStatus.ACTIVE
    await db.commit()
    await db.refresh(user)
    
    # Create tokens
    token_data = {"sub": str(user.id), "phone": user.phone, "role": user.role.value}
    access_token = create_user_token(token_data)
    refresh_token = create_refresh_token(token_data)
    
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
        user={
            "id": user.id,
            "phone": user.phone,
            "email": user.email,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "role": user.role.value,
            "status": user.status.value,
            "isPhoneVerified": user.isPhoneVerified.value
        }
    )


@router.post("/resend-otp", response_model=OTPResponse, status_code=status.HTTP_200_OK)
async def resend_otp(request: EmailRequest, db: AsyncSession = Depends(get_db)):
    """
    Resend OTP to email.
    """
    # Clean up expired OTPs
    cleanup_expired_otps()
    
    email = request.email
    
    # Check if user exists
    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email not registered. Please use /send-otp first."
        )
    
    # Generate and store new OTP
    otp_code = generate_otp()
    store_otp(email, otp_code)
    
    # Send OTP via Email
    email_sent = send_otp_via_email(email, otp_code)
    
    if not email_sent:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP. Please try again."
        )
    
    from app.core.config import settings
    return OTPResponse(
        message="OTP resent successfully",
        email=email,
        expires_in_minutes=settings.OTP_EXPIRE_IN_MINS
    )