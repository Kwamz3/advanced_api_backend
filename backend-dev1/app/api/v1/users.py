from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete

from app.core.database import get_db
from app.models.user import User
from app.core.security import verify_token

router = APIRouter()
security = HTTPBearer() 