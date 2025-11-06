from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum, Text, JSON, ForeignKey, Float
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from typing import List, Optional, Any
from datetime import datetime
from sqlalchemy.sql import func
import uuid 

from app.models.user import Base
from app.models.types import PostgresUUID
 
 
class MovieList(Base):
    __tablename__ = "movie_list"
    
    #Basic Info
    id = Column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(225), nullable=False)
    category = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    
    # Media Info
    poster_url = Column(String(500), nullable=True)
    trailer_url = Column(String(500), nullable=True)
    duration = Column(Integer, nullable=True)
    release_year = Column(Integer, nullable=True)
 
    # Additional data
    rating = Column(Float, nullable=True)
    cast = Column(Text, nullable=True)
    producer = Column(String(500), nullable=True)
    
    # Tracking Info
    views = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_liked = Column(Boolean, default=False)

    
    # Relationships
    category_id = Column(PostgresUUID(as_uuid=True), ForeignKey("categories.id"), nullable=True)
    category_rel = relationship("Category", back_populates="movies_rel")
    
    
    
class CreateMovieMock(BaseModel):
    title : str = Field(..., examples=["Inception"])
    category : Optional[str] = None
    description : Optional [str] = None
    poster_url : str
    trailer_url : str
    duration : int
    release_year : int
    rating : float
    cast : str
    producer : str
    views : Optional[int] = None
    created_at : datetime
    updated_at : datetime
    is_liked : bool = False

class ResponseMovieMock(CreateMovieMock):
    id : str = Field(default_factory=lambda: str(uuid.uuid4()), examples=["37c65b57-5f58-4a3d-93d8-12a3f8cd71a7"])