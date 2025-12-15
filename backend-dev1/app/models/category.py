from sqlalchemy import String, Integer, Column, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from sqlalchemy.sql import func
import uuid

from app.models.types import PostgresUUID
from app.models.users import Base

class Category(Base):
    
    __tablename__ = "category"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    
    # Relationship
    movies_rel = relationship("MovieList", back_populates="category_rel")
    series_rel = relationship("SeriesList", back_populates="category_rel")