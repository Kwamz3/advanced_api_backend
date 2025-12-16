from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum, Text, JSON, ForeignKey, Float
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Any
from datetime import datetime
from sqlalchemy.sql import func
import uuid 

from app.models.users import Base
from app.models.types import PostgresUUID
from app.models.types import UUID 
 
 
 
class MovieList(Base):
    __tablename__ = "movie_list"
    
    #Basic Info
    id = Column(Integer, primary_key=True, nullable=False)
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
    
class WatchListBase(Base):
    __tablename__ = "watchlist"
    
    movie_id = Column(Integer, primary_key= True, nullable= False)
    user_id = Column(Integer, primary_key= True, nullable= False)
    title = Column(String(225), nullable= True)
    poster_url = Column(String(500), nullable=True)
    trailer_url = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
class CreateMovieMock(BaseModel):
    id : str = Field(...,examples=["001"])    
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
    
class WatchListItem(BaseModel):
    movie_id: str = Field(..., examples=["001"])
    user_id: str = Field(..., examples=["001"])
    title: str = Field(..., examples=["Inception"])
    poster_url: Optional[str] = Field(None, examples=["https://image.tmdb.org/t/p/w500/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg"])
    trailer_url: Optional[str] = Field(None, examples=["https://www.youtube.com/watch?v=LEjhY15eCx0"])