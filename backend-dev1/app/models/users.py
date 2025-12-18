"""
User model and related schemas
"""

from sqlalchemy import Column, String, Integer, Enum, JSON, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Dict, Any,Union
from sqlalchemy.sql import func
import enum
import uuid
from datetime import datetime

from app.core.database import Base
from app.models.user_types import UUID

Base()

class UserRole(str, enum.Enum):
    CLIENT = "CLIENT"
    TASKER = "TASKER"
    ADMIN = "ADMIN"
    
class UserStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"
    
class VerifyStatus(str, enum.Enum):
    NOT_SUBMITTED = "NOT_SUBMITTED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    
class ServiceStatus(str, enum.Enum):
    FREE = "FREE"
    PREMIUM = "PREMIUM"
    PREMIUM_PLUS = "PREMIUM_PLUS"
    
class GenderStatus(str, enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    RATHER_NOT_SAY = "RATHER_NOT_SAY"
    NOT_SELECTED = "NOT_SELECTED"
    
class User(Base):
    
    __tablename__ = "users"
    
    id = Column(UUID(), primary_key=True, default=uuid.uuid4, nullable=False)
    phone = Column(String(20), unique=True, index=True, nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=True)
    first_name = Column(String(100), index=True, nullable=True)
    last_name = Column(String(100), index=True, nullable=True)
    role = Column(Enum(UserRole), nullable=True)
    status = Column(Enum(UserStatus), default=UserStatus.INACTIVE, nullable=False)
    #Profile information
    profile_picture = Column(String(500), nullable=True)
    date_of_birth = Column(DateTime(timezone=True), nullable=True)
    gender = Column(Enum(GenderStatus), default=GenderStatus.NOT_SELECTED, nullable=True)
    bio = Column(Text, nullable=True)
    # Account infomation
    service = Column(Enum(ServiceStatus), nullable= True)
    watch_list = Column(JSON, nullable= True)  # Store as JSON array for SQLite compatibility
    #Location
    location = Column(String(255), nullable=True)
    address = Column(Text, nullable=True)
    location = Column(JSON, nullable=True) #{lat, lng}
    #Verifcation
    is_email_verified = Column(Enum(VerifyStatus), default=VerifyStatus.NOT_SUBMITTED)
    is_phone_verified = Column(Enum(VerifyStatus), default=VerifyStatus.NOT_SUBMITTED)
    #Settings
    preferences = Column(JSON, nullable=True)
    notification_settings = Column(JSON, nullable=True)
    #Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    

class UserCreate(BaseModel):
    phone: str = Field(..., examples=["+233-54-768-8745"])
    email: str = Field(..., examples=["john.doe@example.com"])
    first_name: str = Field(..., examples=["John"])
    last_name: str = Field(..., examples=["Doe"])
    role: UserRole = Field(default= UserRole.CLIENT, examples=[UserRole.CLIENT])
    status: UserStatus = Field(default=UserStatus.INACTIVE, examples=[UserStatus.INACTIVE])
    # Profile info
    profile_picture: Optional[str] = Field(None, examples=["https://example.com/avatar.jpg"]) 
    date_of_birth: Optional[datetime] = Field(None, examples=["2000-01-01T00:00:00Z"])
    gender: Optional[GenderStatus] = Field(default= GenderStatus.NOT_SELECTED, examples=[GenderStatus.NOT_SELECTED])
    bio: Optional[str] = Field(None, examples=["Creative designer and movie lover."])
    service_status: ServiceStatus = Field(default= ServiceStatus.FREE, examples=[ServiceStatus.FREE])
    # Location
    address: Optional[str] = Field(None, examples=["123 Main Street, Accra"])
    location: Optional[Dict[str, Any]] = Field(None, examples=[{"latitude": 5.6037, "longitude": -0.1870}])
    # Verification
    is_email_verified: VerifyStatus = Field(default= VerifyStatus.NOT_SUBMITTED, examples=[VerifyStatus.NOT_SUBMITTED])
    is_phone_verified: VerifyStatus = Field(default= VerifyStatus.NOT_SUBMITTED, examples=[VerifyStatus.NOT_SUBMITTED])
    # Settings
    preferences: Optional[Dict[str, Any]] = Field(None, examples=[{"theme": "dark"}])
    notification_settings: Optional[Dict[str, Any]] = Field(None, examples=[{"email": True, "sms": False}])
    # Timestamps
    created_at: datetime = Field(default_factory=lambda: datetime.now(), examples=["2025-11-06T00:00:00Z"])
    updated_at: datetime = Field(default_factory=lambda: datetime.now(), examples=["2025-11-06T00:00:00Z"])
    
    
class UserUpdate(BaseModel):
    phone: Optional[str] = Field(None, examples=["+233-54-768-8745"])
    email: Optional[str] = Field(None, examples=["john.doe@example.com"])
    first_name: Optional[str] = Field(None, examples=["John"])
    last_name: Optional[str] = Field(None, examples=["Doe"])
    role: Optional[UserRole] = Field(None, examples=[UserRole.CLIENT])
    status: Optional[UserStatus] = Field(None, examples=[UserStatus.INACTIVE])
    # Profile info
    profile_picture: Optional[str] = Field(None, examples=["https://example.com/avatar.jpg"]) 
    date_of_birth: Optional[datetime] = Field(None, examples=["2000-01-01T00:00:00Z"])
    gender: Optional[GenderStatus] = Field(None, examples=[GenderStatus.NOT_SELECTED])
    bio: Optional[str] = Field(None, examples=["Creative designer and movie lover."])
    # Location
    address: Optional[str] = Field(None, examples=["123 Main Street, Accra"])
    location: Optional[Dict[str, Any]] = Field(None, examples=[{"latitude": 5.6037, "longitude": -0.1870}])
     # Settings
    preferences: Optional[Dict[str, Any]] = Field(None, examples=[{"theme": "dark"}])
    notification_settings: Optional[Dict[str, Any]] = Field(None, examples=[{"email": True, "sms": False}])
    