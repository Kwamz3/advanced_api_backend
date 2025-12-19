# from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum, Text, JSON, ForeignKey, Float
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

# from app.models.users import Base
 
 
# class SeriesList(Base):
#     __tablename__ = "series_list"
    
#     #Basic Info
#     id = Column(Integer, primary_key=True, nullable=False)
#     title = Column(String(225), nullable=False)
#     category = Column(String(50), nullable=True)
#     description = Column(Text, nullable=True)
#     # Media Info
#     poster_url = Column(String(500), nullable=True)
#     trailer_url = Column(String(500), nullable=True)
#     duration = Column(Integer, nullable=True)
#     release_year = Column(Integer, nullable=True)
#     # Additional data
#     rating = Column(Float, nullable=True)
#     cast = Column(Text, nullable=True)
#     producer = Column(String(500), nullable=True)
#     # Tracking Info
#     is_featured = Column(Boolean, default=False)
#     views = Column(Integer, default=0)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())
#     is_liked = Column(Boolean, default=None)