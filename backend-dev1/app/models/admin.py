from sqlalchemy import Column, String, Integer, DateTime, Enum, Text, Boolean, JSON, ForeignKey
from sqlalchemy.sql import func
import uuid

from app.models.types import UUID
from app.models.user import Base


class SystemSettings(Base):
    
    __tablename__ = "system_settings"
    
    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(50), nullable=True)
    
    #Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    

class AuditLog(Base):
    
    __tablename__ = "audit_log"
    
    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(), ForeignKey("user.id"),nullable=True)
    action = Column(String(100), nullable=False)
    resource = Column(String(100), nullable=False)
    resource_id = Column(String(100), nullable=True)
    details = Column(JSON, nullable=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(Text, nullable=True)
    
    # Timestmps
    created_at = Column(DateTime(timezone=True), server_default=func.now())