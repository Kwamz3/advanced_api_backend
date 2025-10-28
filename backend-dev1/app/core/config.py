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
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "https://your-frontend-domain.onrender.com"
    ]
    
    # Database - Dual setup (POSGRESQL for production, SQLite for development/testing)
    DATABASE_URL: str = "postgresql://postgresql:1234567890@localhost:5432/streamplus"
    DATABASE_TEST_URL: str = "sqlite:///./test_db.sqlite3"
    USE_SQLITE_FOR_DEV: bool = True
    
    # EnvirOnment
    ENVIRONMENT: str = "production"
    Debug: bool = True
    
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
        
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Security
    SECRET_KEY: str = "Streamplus_123"