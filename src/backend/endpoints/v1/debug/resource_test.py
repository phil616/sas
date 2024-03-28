from fastapi import APIRouter, Security

from core.authorize import check_permissions
from core.logger import logger

resourceTestRouter = APIRouter(tags=["联通测试"])

@resourceTestRouter.get("/get/basic/info")
async def get_base_test_info():
    return "success get user basic info"