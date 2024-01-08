from fastapi import APIRouter, Security

from core.authorize import check_permissions
from core.logger import logger

resourceTestRouter = APIRouter()

@resourceTestRouter.get("/basicinfo")
async def get_base_test_info():
    return "success get user basic info"