"""
Application settings for Streamplus Backend
"""

from typing import List, Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # API SETTINGS
    API_V1_STR: str = "/api/v1"
    APP_NAME: str = "StreamPlus"
    VERSION: str = "1.0.0"
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    # DATABASE - Dual setup (POSGRESQL for production, SQLite for development/testing)
    DATABASE_URL: str = "postgresql://postgresql:1234567890@localhost:5432/streamplus"
    DATABASE_TEST_URL: str = "sqlite:///./test_db.sqlite3"
    USE_SQLITE_FOR_DEV: bool = True
    
    # ENVIRONMENT
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    @property
    def effective_database_url(self) -> str:
        if self.ENVIRONMENT == "testing":
            return self.DATABASE_TEST_URL
        elif self.ENVIRONMENT == "production":
            # In production, use the DATABASE_URL provided by Render
            return self.DATABASE_URL
        elif self.ENVIRONMENT and self.USE_SQLITE_FOR_DEV in ["development", "dev"]:
            return "sqlite:///./streamplus.sqlite3"
        else:
            return self.DATABASE_URL
        
    # REDIS
    REDIS_URL: str = "redis://localhost:6379"
    
    # SECURITY
    SECRET_KEY: str = "Streamplus_123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_IN_MINS: int = 30
    REFRESH_TOKEN_EXPIRE_IN_DAYS: int = 7
    
    # OTP SETTINGS
    OTP_EXPIRE_IN_MINS: int = 5
    OTP_LENGTH: int = 6
    USE_FIXED_OTP_LENGTH_FOR_TESTING: bool = True
    FIXED_OTP_VALUE: str = "123456"
    
    # File Storage (MinIO/S3)
    MINIO_ENDPOINT: str = "localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_BUCKET_NAME: str = "streamplus"
    MINIO_SECURE: bool = False
    
    # Email Settings for OTP
    SMTP_TLS: bool = True
    SMTP_PORT: int = 587
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_USER: str = "your-email@gmail.com"
    SMTP_PASSWORD: str = "your-app-password"
    EMAILS_FROM_EMAIL: str = "noreply@streamplus.com"
    EMAILS_FROM_NAME: str = "StreamPlus"
    
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"
        
# Create an instance
settings = Settings()