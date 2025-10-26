"""
User model and related schemas
"""

from sqlalchemy import Column, String, Integer, Enum, JSON, DateTime, Boolean, Text
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.sql import func
import enum
import uuid

Base = declarative_base()

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
    
    id = Column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
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
    isEmailVerified = Column(Boolean, default=False)
    isPhoneVerified = Column(Boolean, default=False)
    
    #Settings
    preferences = Column(JSON, nullable=True)
    notificationSettings = Column(JSON, nullable=True)
    
    #Timestamps
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())