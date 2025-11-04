from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from contextlib import asynccontextmanager
from typing import Optional
from dotenv import load_dotenv
import logging
import uvicorn
import os
load_dotenv()

from app.api.v1 import users
from app.core.config import settings
from app.core.database import init_db
from app.core.security import verify_token

security = HTTPBearer()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Streamplus backend...")
    
    await init_db()
    logger.info("Database initialized...")
    
    yield
    logger.info("Shutting down Streamplus Backend...")
    
    
app = FastAPI(
    title= "Streamplus API",
    description= "Backend API for Streamplus - Movie streaming platform",
    version= "1.0.0",
    docs_url= "/docs",
    redoc_url= "/redoc",
    lifespan= lifespan
)