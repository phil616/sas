from fastapi import APIRouter
from .v1 import v1
api = APIRouter(prefix="/api")
api.include_router(v1.v1_router)
