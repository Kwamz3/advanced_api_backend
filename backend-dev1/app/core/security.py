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
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes= settings.ACCESS_TOKEN_EXPIRE_IN_MINS)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    """Create JWT refresh token"""
    refresh_token = data.copy()
    expire = datetime.now() + timedelta(days= settings.REFRESH_TOKEN_EXPIRE_IN_DAYS)
    refresh_token.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(refresh_token, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    """Verify token"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type") != "access":
            raise HTTPException(status_code=401, detail="Invalid token type")
        
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

# OTP storage with expiration
class OTPEntry(NamedTuple):
    code: str
    expires_at: datetime
    attempts: int = 0
    
# In-memory OTP storage (use Redis in production for scalability)
otp_storage: Dict[str, OTPEntry] = {}

def generate_otp(length: Optional[int] = None) -> str:
    """Generate a random OTP code"""
    if settings.USE_FIXED_OTP_LENGTH_FOR_TESTING and settings.ENVIRONMENT == "development":
        return settings.FIXED_OTP_VALUE
    
    otp_length = length or settings.OTP_LENGTH
    return ''.join(secrets.choice(string.digits) for _ in range(otp_length))

def store_otp(phone: str, code: str) -> None:
    """Store OTP code with expiration time"""
    expires_at = datetime.now() + timedelta(minutes=settings.OTP_EXPIRE_IN_MINS)
    otp_storage[phone] = OTPEntry(code=code, expires_at=expires_at, attempts=0)

def verify_otp(phone: str, code: str) -> bool:
    """Verify OTP code for a phone number"""
    if phone not in otp_storage:
        return False
    
    otp_entry = otp_storage[phone]
    
    # Check if OTP has expired
    if datetime.now() > otp_entry.expires_at:
        del otp_storage[phone]
        return False
    
    # Check if max attempts exceeded
    if otp_entry.attempts >= 3:
        del otp_storage[phone]
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many failed attempts. Please request a new OTP."
        )
    
    # Verify the code
    if otp_entry.code == code:
        del otp_storage[phone]
        return True
    else:
        # Increment attempts
        otp_storage[phone] = OTPEntry(
            code=otp_entry.code,
            expires_at=otp_entry.expires_at,
            attempts=otp_entry.attempts + 1
        )
        return False

def cleanup_expired_otps() -> None:
    """Remove expired OTPs from storage"""
    current_time = datetime.now()
    expired_phones = [phone for phone, entry in otp_storage.items() 
                      if current_time > entry.expires_at]
    for phone in expired_phones:
        del otp_storage[phone]

def send_otp_via_sms(phone: str, code: str) -> bool:
    """Send OTP via SMS using Twilio"""
    try:
        # In development mode, just log the OTP
        if settings.ENVIRONMENT == "development":
            print(f"[DEV MODE] OTP for {phone}: {code}")
            return True
        
        # In production, use Twilio
        from twilio.rest import Client
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            body=f"Your {settings.APP_NAME} verification code is: {code}. Valid for {settings.OTP_EXPIRE_IN_MINS} minutes.",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone
        )
        return message.sid is not None
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")
        return False