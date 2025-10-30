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