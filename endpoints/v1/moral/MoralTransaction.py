from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel
import datetime
from curd.moral import DL_MoralAction_Retrieve_action_on, MoralActionCreateSchema, DL_MoralAction_Create, \
    DL_MoralAction_Update_By_PK, DL_MoralAction_Delete_By_PK, MoralRecordApplySchema, \
    LL_MoralRecordApply_By_ApplySchema, LL_RetrieveUserMoralRecord_By_username, LL_RetrieveMoralRecord_Unchecked, \
    LL_UpdateOrCheckMoralRecord_CheckSchema, MoralRecordCheckerSchema, UserCurrentMoralScoreSchema, \
    LL_GetUserCurrentMoralScore_By_username, DL_MoralAction_Retrieve_By_PK
from model.Moral import MoralActionSchema, MoralRecordSchema
from response.schemas.stdresp import StdResp

moralTransactionRouter = APIRouter(tags=['德育分事务'])


class MoralActionSchemaRespList(BaseModel):
    data: List[MoralActionSchema]


# MARP1
@moralTransactionRouter.get(
    path="/get/MoralAction",
    name="获取可用德育分活动",
    description="获取所有可用的德育分活动",
    response_model=MoralActionSchemaRespList,
)
async def UG_On_MoralAction():
    data = await DL_MoralAction_Retrieve_action_on()
    return MoralActionSchemaRespList(data=data)


# MAPR6
@moralTransactionRouter.get(
    path="/get/AllMoralAction",
    name="获取所有德育分活动",
    description="获取所有德育分活动，包含不可用的德育分",
    response_model=MoralActionSchemaRespList,
)
async def UG_On_MoralAction():
    data = await DL_MoralAction_Retrieve_action_on(False)
    return MoralActionSchemaRespList(data=data)


# MARP3
@moralTransactionRouter.post(
    path="/add/MoralAction",
    name="新建德育分活动",
    description="注册一个新的德育分活动并公开",
    response_model=StdResp
)
async def UP_Add_MoralAction(newAction: MoralActionCreateSchema):
    await DL_MoralAction_Create(newAction)
    return StdResp()


# MAPR4
@moralTransactionRouter.post(
    path="/update/MoralAction",
    name="修改德育分活动",
    description="更新一个德育分活动信息",
    response_model=StdResp
)
async def UP_Update_MoralAction(action_id: int, action: MoralActionCreateSchema):
    await DL_MoralAction_Update_By_PK(action_id, action)
    return StdResp()


# MARP5
@moralTransactionRouter.get(
    path="/delete/MoralAction",
    name="禁用一个德育分活动",
    description="禁用或是删除一个德育分活动信息",
    response_model=StdResp
)
async def UD_DEL_MoralAction_By_DeleteType(action_id: int):
    await DL_MoralAction_Delete_By_PK(action_id)
    return StdResp()


# MARP9
@moralTransactionRouter.post(
    path="/add/ApplyMoralRecord",
    name="申请德育分活动",
    description="申请一个德育分活动加入到德育分列表",
    response_model=StdResp
)
async def UP_Apply_MoralRecord(applyRecord: MoralRecordApplySchema):
    await LL_MoralRecordApply_By_ApplySchema(applyRecord)
    return StdResp()


class UserMoralRecordResponseSchema(BaseModel):
    data: List[MoralRecordSchema]


# MARP8
@moralTransactionRouter.get(
    path="/get/UserMoralRecord",
    name="查询用户德育分记录",
    description="查询用户的德育分记录",
    response_model=UserMoralRecordResponseSchema
)
async def UG_Query_User_MoralRecord(username: str):
    result = await LL_RetrieveUserMoralRecord_By_username(username)
    return UserMoralRecordResponseSchema(data=result)

#MARP10
@moralTransactionRouter.get(
    path="/get/uncheckedMoralRecord",
    name="获取待审核列表",
    description="获取尚未审核的德育分记录",
    response_model=UserMoralRecordResponseSchema
)
async def UG_Uncheck_MoralRecord(status: int = 1):
    data = await LL_RetrieveMoralRecord_Unchecked(status)
    return UserMoralRecordResponseSchema(data=data)
# MAPR7
@moralTransactionRouter.post(
    path="/update/checkMoralRecord",
    name="提交审核德育分记录",
    description="通过部分更新审核某个德育分记录",
    response_model=StdResp
)
async def UP_Update_CheckMoralRecord(record:MoralRecordCheckerSchema):
    await LL_UpdateOrCheckMoralRecord_CheckSchema(record)
    return StdResp()


#MAPP2
@moralTransactionRouter.get(
    path="/get/userMoralScore",
    name="提交审核德育分记录",
    description="通过部分更新审核某个德育分记录",
    response_model=UserCurrentMoralScoreSchema
)
async def UG_Get_UserCurrentScore_By_username(username:str):
    data = await LL_GetUserCurrentMoralScore_By_username(username)
    return data

# MARP 额外未在文档中注册
@moralTransactionRouter.get(
    path="/get/MoralActionInfoById",
    name="获取一个德育分活动",
    description="通过id获取一个德育分活动详细信息",
    response_model=MoralActionSchema
)
async def UG_GET_MoralActionDetail_By_action_id(action_id:int):
    action = await DL_MoralAction_Retrieve_By_PK(action_id=action_id)
    return action
