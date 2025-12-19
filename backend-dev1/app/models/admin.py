from sqlalchemy import Column, String, Integer, DateTime, Enum, Text, Boolean, JSON, ForeignKey
from pydantic import BaseModel, Field
from sqlalchemy.sql import func
import enum

from app.models.users import Base, VerifyStatus, UserStatus, ServiceStatus


class AccountApproval(BaseModel):
    """
    Account Approval Base Model for admin
    refer to admin.py/ account_approval
    """
    isEmailVerified: VerifyStatus = Field(default= VerifyStatus.NOT_SUBMITTED, examples=[VerifyStatus.NOT_SUBMITTED])
    isPhoneVerified: VerifyStatus = Field(default= VerifyStatus.NOT_SUBMITTED, examples=[VerifyStatus.NOT_SUBMITTED])

class AccountBan(BaseModel):
    """
    Account Ban Base Model for admin
    refer to admin.py/ account_ban
    """
    status: UserStatus = Field(default=UserStatus.INACTIVE, examples=[UserStatus.INACTIVE])

class Status(BaseModel):
    """
    Account Service status Base Model for admin
    refer to admin.py/ serviceStatus
    """
    service: ServiceStatus = Field(default=ServiceStatus.FREE, examples=[ServiceStatus.PREMIUM])


# class Priority(str, enum.Enum):
#     HIGH = "HIGH"
#     MEDIUM = "MEDIUM"
#     LOW = "LOW"
#     NOT_SET = "NOT_SET"

# class SystemSettings(Base):
#     __tablename__ = "system_settings"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     key = Column(String(100), unique=True, nullable=False)
#     value = Column(Text, nullable=False)
#     description = Column(Text, nullable=True)
#     category = Column(String(50), nullable=True)
#     #Timestamps
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    

# class AuditLog(Base):
#     __tablename__ = "audit_log"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("users.id"),nullable=True)
#     action = Column(String(100), nullable=False)
#     resource = Column(String(100), nullable=False)
#     resource_id = Column(String(100), nullable=True)
#     details = Column(JSON, nullable=True)
#     ip_address = Column(String(50), nullable=True)
#     user_agent = Column(Text, nullable=True)
#     # Timestmps
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    
# class SupportTicket(Base):
#     __tablename__ = "support_ticket"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False) 
#     # Ticket details
#     subject = Column(String(255), nullable=False)
#     description = Column(Text, nullable=False)
#     category = Column(String(50), nullable=False)
#     priority = Column(Enum(Priority), default= Priority.NOT_SET)
#     status = Column(String(20), default="OPEN")
#     # Assignment
#     assigned_to = Column(Integer, nullable=True)
#     # Additional data
#     attachments = Column(JSON, nullable=True)
#     # Timestamps
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())
#     resolved_at = Column(DateTime(timezone=True), nullable=True)
    
