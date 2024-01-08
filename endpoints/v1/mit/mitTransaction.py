# doc https://www.yuque.com/cst3/orwkic/kw0khrg9kvyblep6

from typing import List, Optional
from fastapi import APIRouter
from pydantic import BaseModel
from model.MIT import MITSchema
from curd.mit import STATUS_CODE_MAPPING, DL_MIT_Retrieve_By_username, MITCreateSchema, DL_MIT_Create
from response.exceptions import E404
from response.schemas.stdresp import StdResp
mitTransactionRouter = APIRouter(tags=['学生医保事务'])

class MITStatusCodeMappingSchema(BaseModel):
    data: dict

@mitTransactionRouter.get(
    path="/get/mit/static/mapping",
    name="获取医保状态码映射表",
    description="获取静态的字典医保状态码映射表",
    response_model=MITStatusCodeMappingSchema,
)
async def UAG_Static_Mapping_Code():
    return MITStatusCodeMappingSchema(data=STATUS_CODE_MAPPING)

@mitTransactionRouter.get(
    path="/get/mit/userStatus",
    name="获取用户的医保状态",
    description="获取用户的医保情况状态",
    response_model=MITSchema
)
async def UG_Get_UserMITSchema(username:str):
    mitInfo = await DL_MIT_Retrieve_By_username(username)
    if mitInfo:
        return mitInfo
    else:
        E404("未找到内容")

@mitTransactionRouter.post(
    path="/crete/mit",
    name="新建一个医保记录",
    description="通过Schema新建一个记录",
    response_model=StdResp
)
async def MG_Create_UserMIT_Record_By_RAWSchema(data:MITCreateSchema):
    await DL_MIT_Create(data)
    return StdResp()