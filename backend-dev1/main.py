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

from app.api.v1 import users, movies, admin
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

app.add_middleware(
    CORSMiddleware,
    allow_origins= settings.ALLOWED_ORIGINS,
    allow_credentials= True,
    allow_headers=["*"],
    allow_methods=["*"]
)

@app.get("/health")
async def health_check():
    import platform
    from datetime import datetime
    
    return{
        "status": "healthy",
        "message": "Streamplus API is running",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT,
        "timestamp": datetime.now().isoformat(),
        "database": "connected" if settings.effective_database_url else "not configured",
        "python_version": platform.python_version(),
        "platform": platform.system()
    }
    
    
app.include_router(users.router, prefix= "/api/v1/users", tags=["Users"])
app.include_router(movies.router, prefix="/api/v1/movies", tags=["Movies"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])

@app.get("/")
async def root():
    return{
        "message": "Welcome to Streamplus",
        "docs": "/docs",
        "health": "/health",
        "version": "1.0.0"
    }
    
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host= "localhost",
        port= 8000,
        reload= True,
        log_level= "info"
    )