from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum, Text, JSON, ForeignKey, Float
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from typing import List, Optional, Any
from datetime import datetime
from sqlalchemy.sql import func
import uuid 

from app.models.user import Base
from app.models.types import PostgresUUID
from app.models.types import UUID 
 
 
class MovieList(Base):
    __tablename__ = "movie_list"
    
    #Basic Info
    id = Column(UUID(), primary_key=True, default=uuid.uuid4)
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
    category_id = Column(UUID(), ForeignKey("categories.id"), nullable=True)
    category_rel = relationship("Category", back_populates="movies_rel")
    
    
    
class CreateMovieMock(BaseModel):
    title : str = Field(..., examples=["Inception"])
    category : Optional[str] = Field(..., examples=["Action"])
    description : Optional [str] = Field(None, examples=["Action with the best female actress in the bizz"])
    poster_url : str = Field(..., examples=["https://example.com/inception.jpg"])
    trailer_url : str = Field(..., examples=["https://youtube.com/watch?v=YoHD9XEInc0"])
    duration : int =Field(..., examples=[140])
    release_year : int = Field(..., examples=[2024])
    rating : float = Field(..., examples=[7.4])
    cast : Optional[str] = Field(None, examples=["Leonardo DiCaprio"])
    producer : Optional[str] = Field(None, examples=["Christopher Nolan"])
    views : Optional[int] = Field(None, examples=[1037])
    created_at : Optional[datetime] = Field(None, examples=["2025-01-01T00:00:00"])
    updated_at : Optional[datetime] = Field(None, examples=["2025-01-01T00:00:00"])
    is_liked : bool = False

class ResponseMovieMock(CreateMovieMock):
    id : str = Field(default_factory=lambda: str(uuid.uuid4()), examples=["37c65b57-5f58-4a3d-93d8-12a3f8cd71a7"])