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
    
    