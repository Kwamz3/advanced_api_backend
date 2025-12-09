"""
User model and related schemas
"""

from sqlalchemy import Column, String, Integer, Enum, JSON, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any,Union
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
    
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, nullable=False)
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
    # Account infomation
    service = Column(Enum(ServiceStatus), nullable= True)
    watchlist = Column(JSON, nullable= True)  # Store as JSON array for SQLite compatibility
    #Location
    location = Column(String(255), nullable=True)
    address = Column(Text, nullable=True)
    location = Column(JSON, nullable=True) #{lat, lng}
    #Verifcation
    isEmailVerified = Column(Enum(VerifyStatus), default=VerifyStatus.NOT_SUBMITTED)
    isPhoneVerified = Column(Enum(VerifyStatus), default=VerifyStatus.NOT_SUBMITTED)
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
    role: UserRole = Field(default= UserRole.CLIENT, examples=[UserRole.CLIENT])
    status: UserStatus = Field(default=UserStatus.INACTIVE, examples=[UserStatus.INACTIVE])
    # Profile info
    profilePicture: Optional[str] = Field(None, examples=["https://example.com/avatar.jpg"]) 
    dateOfbirth: Optional[datetime] = Field(None, examples=["2000-01-01T00:00:00Z"])
    gender: Optional[GenderStatus] = Field(default= GenderStatus.NOT_SELECTED, examples=[GenderStatus.NOT_SELECTED])
    bio: Optional[str] = Field(None, examples=["Creative designer and movie lover."])
    serviceStatus: ServiceStatus = Field(default= ServiceStatus.FREE, examples=[ServiceStatus.FREE])
    # Location
    address: Optional[str] = Field(None, examples=["123 Main Street, Accra"])
    location: Optional[Dict[str, Any]] = Field(None, examples=[{"latitude": 5.6037, "longitude": -0.1870}])
    # Verification
    isEmailVerified: VerifyStatus = Field(default= VerifyStatus.NOT_SUBMITTED, examples=[VerifyStatus.NOT_SUBMITTED])
    isPhoneVerified: VerifyStatus = Field(default= VerifyStatus.NOT_SUBMITTED, examples=[VerifyStatus.NOT_SUBMITTED])
    # Settings
    preferences: Optional[Dict[str, Any]] = Field(None, examples=[{"theme": "dark"}])
    notificationSettings: Optional[Dict[str, Any]] = Field(None, examples=[{"email": True, "sms": False}])
    # Timestamps
    createdAt: datetime = Field(default_factory=lambda: datetime.now(), examples=["2025-11-06T00:00:00Z"])
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(), examples=["2025-11-06T00:00:00Z"])
    
    
class UserUpdate(BaseModel):
    phone: str = Field(..., examples=["+233-54-768-8745"])
    email: str = Field(..., examples=["john.doe@example.com"])
    firstName: str = Field(..., examples=["John"])
    lastName: str = Field(..., examples=["Doe"])
    role: UserRole = Field(default=UserRole.CLIENT, examples=[UserRole.CLIENT])
    status: UserStatus = Field(default=UserStatus.INACTIVE, examples=[UserStatus.INACTIVE])
    # Profile info
    profilePicture: Optional[str] = Field(None, examples=["https://example.com/avatar.jpg"]) 
    dateOfbirth: Optional[datetime] = Field(None, examples=["2000-01-01T00:00:00Z"])
    gender: Optional[GenderStatus] = Field(default= GenderStatus.NOT_SELECTED, examples=[GenderStatus.NOT_SELECTED])
    bio: Optional[str] = Field(None, examples=["Creative designer and movie lover."])
    # Location
    address: Optional[str] = Field(None, examples=["123 Main Street, Accra"])
    location: Optional[Dict[str, Any]] = Field(None, examples=[{"latitude": 5.6037, "longitude": -0.1870}])
     # Settings
    preferences: Optional[Dict[str, Any]] = Field(None, examples=[{"theme": "dark"}])
    notificationSettings: Optional[Dict[str, Any]] = Field(None, examples=[{"email": True, "sms": False}])
    

class WatchListItem(BaseModel):
    movie_id: str = Field(..., examples=["001"])
    title: str = Field(..., examples=["Inception"])
    poster_url: Optional[str] = Field(None, examples=["https://image.tmdb.org/t/p/w500/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg"])
    trailer_url: Optional[str] = Field(None, examples=["https://www.youtube.com/watch?v=LEjhY15eCx0"])