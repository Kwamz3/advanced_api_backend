from sqlalchemy import String, Integer, Column, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from sqlalchemy.sql import func
import uuid

from app.models.types import PostgresUUID
from app.models.users import Base

class Category(Base):
    
    __tablename__ = "category"
    
    id = Column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    
    # Relationship
    movies_rel = relationship("MovieList", back_populates="catergory_rel")
    series_rel = relationship("SeriesList", back_populates="catergory_rel")
    category_chosen = relationship("User", back_populates="user_category")