from fastapi import APIRouter

from app.api import notify

api_router = APIRouter()
api_router.include_router(notify.router, prefix="/api", tags=["notify"])
