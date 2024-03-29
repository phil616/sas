from core.authorize import check_permissions
from .v1 import authorization
from .v1 import resources
from .v1 import background
from fastapi import APIRouter,Security

api_router = APIRouter()

api_router.include_router(background.background_router)
api_router.include_router(authorization.authorization_router)
api_router.include_router(resources.resource_router)