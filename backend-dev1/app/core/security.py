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