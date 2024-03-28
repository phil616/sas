from fastapi import APIRouter,Security
from starlette.requests import Request

from core.authorize import check_permissions
from core.logger import logger
debug = APIRouter(tags=['调试'])

@debug.get("/group",dependencies=[Security(check_permissions,scopes=["group"])])
async def get_group():
    return "success"

@debug.get("/normal",dependencies=[Security(check_permissions,scopes=["student"])])
async def get_normal():
    return "success"