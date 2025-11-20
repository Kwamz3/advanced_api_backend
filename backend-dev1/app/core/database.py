"""
Database configuration and connection - Dual database setup
Supports both PostgreSQL (production) and SQLite (development/testing)
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import logging
import os

from app.core.config import settings

logger = logging.getLogger(__name__)

# Create base class for models
Base = declarative_base()

# Determine database URL and create appropriate engine
db_url = settings.effective_database_url

if db_url.startswith("sqlite"):
    # SQLite configuration
    logger.info(f"Using SQLite Databse: {db_url}")
    # For async SQLite, use aiosqlite
    async_db_url = db_url.replace("sqlite:///", "sqlite+aiosqlite:///")
    
    # Ensure directory exists for SQLite file
    if not db_url.startswith("sqlite:///:memory:"):
        db_path = db_url.replace("sqlite:///", "")
        db_dir = os.path.dirname(db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
            logger.info(f"Created SQLite database: {db_dir}")
            
    engine = create_async_engine(
        async_db_url,
        echo = settings.DEBUG,
        future = True,
        connect_args = {"check_same_thread": False}
    )
else:
    logger.info(f"Using postgreSQL databse")
    async_db_url = db_url.replace("postgresql://", "postgresql+asyncpg://")
    
    engine = create_async_engine(
        async_db_url,
        echo = settings.DEBUG,
        future = True,
        pool_pre_ping= True,
        pool_recycle= 300
    )
    
    
AsyncSessionLocal = async_sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    autoflush= False,
    autocommit=True,
    expire_on_commit=False
)

async def get_db():
    """Dependency to get db session"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
            
async def init_db():
    """Initialize database tabels"""
    try:
        from app.models import admin, category, movies, series, types, users
        
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            logger.info("Database tables created successfully...")
            
    except ImportError as e:
        logger.warning(f"Could not import models: {e}")
        logger.warning("Creating tables without model imports...")
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
                logger.info("Database tables created successfully (without models)...")
        except ImportError as e2:
            logger.error(f"Error creating database tables: {e2}")
            logger.warning("Continuing without database initialization...")
            
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        logger.warning(f"Continuing without database initialization...")
            