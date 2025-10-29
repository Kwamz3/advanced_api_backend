"""
Security utilies for authentication and authorization 
"""

from datetime import datetime, timedelta
from typing import Optional, Union, Dict, NamedTuple
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
import secrets
import string

from app.core.config import settings


# passeword hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# otp storage with expiration
class OTPEntry(NamedTuple):
    code: str
    expires_at: datetime
    attempts: int = 0
    
# In-memory OTP storage (use Redis in production for scalability)
otp_storage: Dict[str, OTPEntry] = {}

def create_user_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_IN_MINS)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt