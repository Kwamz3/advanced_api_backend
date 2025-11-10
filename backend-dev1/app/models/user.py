"""
User model and related schemas
"""

from sqlalchemy import Column, String, Integer, Enum, JSON, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from sqlalchemy.sql import func
import enum
import uuid
from datetime import datetime


from app.models.types import UUID 
from app.core.database import Base

Base()

class UserRole(str, enum.Enum):
    CLIENT = "CLIENT"
    TASKER = "TASKER"
    ADMIN = "ADMIN"
    
class UserStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"
    
class VerifyEmail(str, enum.Enum):
    NOT_SUBMITTED = "NOT_SUBMITTED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    
class VerifyPhone(str, enum.Enum):
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
    
    __tablename__ = "user"
    
    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    phone = Column(String(20), unique=True, index=True, nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=True)
    firstName = Column(String(100), index=True, nullable=True)
    lastName = Column(String(100), index=True, nullable=True)
    role = Column(Enum(UserRole), nullable=True)
    status = Column(Enum(UserStatus), default=UserStatus.INACTIVE, nullable=False)
    
    #Profile information
    profilePicture = Column(String(500), nullable=True)
    dateOfbirth = Column(DateTime, nullable=True)
    gender = Column(Enum(GenderStatus), default=GenderStatus.NOT_SELECTED, nullable=True)
    bio = Column(Text, nullable=True)
    
    #Location
    location = Column(String(255), nullable=True)
    address = Column(Text, nullable=True)
    location = Column(JSON, nullable=True) #{lat, lng}
    
    #Verifcation
    isEmailVerified = Column(Enum(VerifyEmail), default=VerifyEmail.NOT_SUBMITTED)
    isPhoneVerified = Column(Enum(VerifyPhone), default=VerifyPhone.NOT_SUBMITTED)
        
    #Settings
    preferences = Column(JSON, nullable=True)
    notificationSettings = Column(JSON, nullable=True)
    
    #Timestamps
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())
    

class UserCreate(BaseModel):
    phone: str = Field(..., examples=["+233-54-768-8745"])
    email: str = Field(..., examples=["john.doe@example.com"])
    firstName: str = Field(..., examples=["John"])
    lastName: str = Field(..., examples=["Doe"])
    role: UserRole = Field(default=UserRole.CLIENT, examples=["client"])
    status: UserStatus = Field(default=UserStatus.INACTIVE, examples=["inactive"])

    # Profile info
    profilePicture: Optional[str] = Field(None, examples=["https://example.com/avatar.jpg"]) 
    dateOfbirth: Optional[datetime] = Field(None, examples=["2000-01-01T00:00:00Z"])
    gender: Optional[GenderStatus] = Field(None, examples=["male"])
    bio: Optional[str] = Field(None, examples=["Creative designer and movie lover."])
    serverStatus: ServiceStatus = Field(default= ServiceStatus.FREE, examples=["Premium"])

    # Location
    address: Optional[str] = Field(None, examples=["123 Main Street, Accra"])
    location: Optional[Dict[str, Any]] = Field(None, examples=[{"latitude": 5.6037, "longitude": -0.1870}])

    # Verification
    isEmailVerified: bool = Field(default=False, examples=[False])
    isPhoneVerified: bool = Field(default=False, examples=[True])

    # Settings
    preferences: Optional[Dict[str, Any]] = Field(None, examples=[{"theme": "dark"}])
    notificationSettings: Optional[Dict[str, Any]] = Field(None, examples=[{"email": True, "sms": False}])

    # Timestamps
    createdAt: datetime = Field(default_factory=lambda: datetime.now(), examples=["2025-11-06T00:00:00Z"])
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(), examples=["2025-11-06T00:00:00Z"])


class UserResponse(UserCreate):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), examples=["37c65b57-5f58-4a3d-93d8-12a3f8cd71a7"])
    
    