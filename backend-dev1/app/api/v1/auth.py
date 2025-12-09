"""
Authentication endpoints for OTP-based phone verification
"""

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field, field_validator
from sqlalchemy.orm import Session
from typing import Optional
import re

from app.core.database import get_db
from app.core.security import (
    generate_otp,
    store_otp,
    verify_otp,
    send_otp_via_sms,
    create_user_token,
    create_refresh_token,
    cleanup_expired_otps
)
from app.models.users import User, UserRole, UserStatus, VerifyStatus
from app.models.auth import OTPResponse, PhoneNumberRequest, TokenResponse, OTPVerifyRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Pydantic Schemas



@router.post("/send-otp", response_model=OTPResponse, status_code=status.HTTP_200_OK)
async def send_otp(request: PhoneNumberRequest, db: Session = Depends(get_db)):
    """
    Send OTP to phone number for verification.
    Creates user if doesn't exist.
    """
    # Clean up expired OTPs first
    cleanup_expired_otps()
    
    phone = request.phone
    
    # Check if user exists, create if not
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        # Create new user with minimal info
        user = User(
            phone=phone,
            role=UserRole.CLIENT,
            status=UserStatus.INACTIVE,
            isPhoneVerified=VerifyStatus.NOT_SUBMITTED
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    # Generate and store OTP
    otp_code = generate_otp()
    store_otp(phone, otp_code)
    
    # Send OTP via SMS
    sms_sent = send_otp_via_sms(phone, otp_code)
    
    if not sms_sent:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP. Please try again."
        )
    
    from app.core.config import settings
    return OTPResponse(
        message="OTP sent successfully",
        phone=phone,
        expires_in_minutes=settings.OTP_EXPIRE_IN_MINS
    )


@router.post("/verify-otp", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def verify_otp_endpoint(request: OTPVerifyRequest, db: Session = Depends(get_db)):
    """
    Verify OTP and return access token.
    Marks phone as verified and activates user account.
    """
    phone = request.phone
    otp = request.otp
    
    # Verify OTP
    try:
        is_valid = verify_otp(phone, otp)
    except HTTPException:
        raise
    
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP"
        )
    
    # Get user
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Update user verification status
    user["isPhoneVerified"] = VerifyStatus.APPROVED
    user["status"] = UserStatus.ACTIVE
    db.commit()
    db.refresh(user)
    
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
async def resend_otp(request: PhoneNumberRequest, db: Session = Depends(get_db)):
    """
    Resend OTP to phone number.
    """
    # Clean up expired OTPs
    cleanup_expired_otps()
    
    phone = request.phone
    
    # Check if user exists
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Phone number not registered. Please use /send-otp first."
        )
    
    # Generate and store new OTP
    otp_code = generate_otp()
    store_otp(phone, otp_code)
    
    # Send OTP via SMS
    sms_sent = send_otp_via_sms(phone, otp_code)
    
    if not sms_sent:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP. Please try again."
        )
    
    from app.core.config import settings
    return OTPResponse(
        message="OTP resent successfully",
        phone=phone,
        expires_in_minutes=settings.OTP_EXPIRE_IN_MINS
    )