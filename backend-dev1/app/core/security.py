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

def store_otp(email: str, code: str) -> None:
    """Store OTP code with expiration time"""
    expires_at = datetime.now() + timedelta(minutes=settings.OTP_EXPIRE_IN_MINS)
    otp_storage[email] = OTPEntry(code=code, expires_at=expires_at, attempts=0)

def verify_otp(email: str, code: str) -> bool:
    """Verify OTP code for an email address"""
    if email not in otp_storage:
        return False
    
    otp_entry = otp_storage[email]
    
    # Check if OTP has expired
    if datetime.now() > otp_entry.expires_at:
        del otp_storage[email]
        return False
    
    # Check if max attempts exceeded
    if otp_entry.attempts >= 3:
        del otp_storage[email]
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many failed attempts. Please request a new OTP."
        )
    
    # Verify the code
    if otp_entry.code == code:
        del otp_storage[email]
        return True
    else:
        # Increment attempts
        otp_storage[email] = OTPEntry(
            code=otp_entry.code,
            expires_at=otp_entry.expires_at,
            attempts=otp_entry.attempts + 1
        )
        return False

def cleanup_expired_otps() -> None:
    """Remove expired OTPs from storage"""
    current_time = datetime.now()
    expired_emails = [email for email, entry in otp_storage.items() 
                      if current_time > entry.expires_at]
    for email in expired_emails:
        del otp_storage[email]

def send_otp_via_email(email: str, code: str) -> bool:
    """Send OTP via email"""
    try:
        # In development mode, just log the OTP
        if settings.ENVIRONMENT == "development":
            print(f"[DEV MODE] OTP for {email}: {code}")
            return True
        
        # In production, send actual email
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Your {settings.APP_NAME} Verification Code"
        msg['From'] = f"{settings.EMAILS_FROM_NAME} <{settings.EMAILS_FROM_EMAIL}>"
        msg['To'] = email
        
        # Email body
        html = f"""
        <html>
          <body>
            <h2>Your Verification Code</h2>
            <p>Your {settings.APP_NAME} verification code is:</p>
            <h1 style="color: #4CAF50; font-size: 36px; letter-spacing: 5px;">{code}</h1>
            <p>This code will expire in {settings.OTP_EXPIRE_IN_MINS} minutes.</p>
            <p>If you didn't request this code, please ignore this email.</p>
          </body>
        </html>
        """
        
        text = f"Your {settings.APP_NAME} verification code is: {code}. Valid for {settings.OTP_EXPIRE_IN_MINS} minutes."
        
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        # Send email
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            if settings.SMTP_TLS:
                server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False