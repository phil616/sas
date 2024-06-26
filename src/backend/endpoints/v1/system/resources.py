from fastapi import APIRouter
from curd.user import DL_User_Create_By_Schema, DL_User_Update_By_Schema,DL_User_Retrieve_ALL
from model.User import UserSchema
from response.schemas.stdresp import StdResp
from response.exceptions import E500
from fastapi.openapi.utils import get_openapi
from fastapi import Request

system = APIRouter(tags=['资源管理'])
@system.get("/get/users")
async def MF_GET_ALL_USERS():
    users = await DL_User_Retrieve_ALL()
    return users


@system.post("/create/user", response_model=StdResp)
async def MF_new_user(user: UserSchema):
    result = await DL_User_Create_By_Schema(user)
    if result:
        return StdResp()
    else:
        E500()


@system.post("/update/user", response_model=StdResp)
async def MF_update_user(user: UserSchema):
    result = await DL_User_Update_By_Schema(user)
    if result:
        return StdResp()
    else:
        E500()

@system.get("/openapi", include_in_schema=True)
async def get_openapi_json(req:Request):
    openapi_schema = get_openapi(
        title="test_title",
        version="0.0.1",
        description="none desc",
        routes=req.app.routes,  
    )
    return openapi_schema

