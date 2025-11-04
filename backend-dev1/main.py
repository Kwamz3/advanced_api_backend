from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from contextlib import asynccontextmanager
from typing import Optional
from dotenv import load_dotenv
import uvicorn
import os
load_dotenv()

from app.api.v1 import users
from app.core.config import settings
from app.core.database import init_db
from app.core.security import verify_token

security = HTTPBearer()

