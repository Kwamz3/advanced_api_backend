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


# password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create jwt token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes= settings.ACCESS_TOKEN_EXPIRE_IN_MINS)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    """Create JWT refresh token"""
    refresh_token = data.copy()
    expire = datetime.utcnow() + timedelta(days= settings.REFRESH_TOKEN_EXPIRE_IN_DAYS)
    refresh_token.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(refresh_token, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    """Verify token"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
        
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify hashed password against plain password"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generate a hashed password"""
    return pwd_context.hash(password)

# # otp storage with expiration
# class OTPEntry(NamedTuple):
#     code: str
#     expires_at: datetime
#     attempts: int = 0
    
# # In-memory OTP storage (use Redis in production for scalability)
# otp_storage: Dict[str, OTPEntry] = {}