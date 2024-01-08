from fastapi import APIRouter
from curd.user import DL_User_Create_By_Schema, DL_User_Update_By_Schema
from model.User import UserSchema
from response.schemas.stdresp import StdResp
from response.exceptions import E500

system = APIRouter(tags=['资源管理'])


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

