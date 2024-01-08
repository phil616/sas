from fastapi import APIRouter
from pydantic import BaseModel
from curd.image_task import ImageTaskActionCreateSchema, DL_ImageTaskAction_Create, \
    ImageTaskRecordNewUploadSchema, DL_ImageTaskAction_Retrieve_By_On, DL_ImageTaskAction_Retrieve_By_PK, \
    DL_ImageTaskRecord_Retrieve_by_username_and_Id, LL_ImageTaskRecord_Upload, LL_RetrieveClazzBriefOfAction, \
    LL_RetrieveClazzBriefOfAction_Advanced
from model.ImageTask import ImageTaskRecordSchema
from response.exceptions import E404
from response.schemas.stdresp import StdResp

imageTaskTransactionRouter = APIRouter(tags=['材料提交事务'])

@imageTaskTransactionRouter.post(
    path="/post/ImageTaskAction",
    name="新建一个材料申请活动",
    description="通过Schema创建一个全局可用的材料申请",
    response_model=StdResp,
)
async def MG_Create_ImageTaskAction(action:ImageTaskActionCreateSchema):
    await DL_ImageTaskAction_Create(action)
    return StdResp()

@imageTaskTransactionRouter.post(
    path="/post/ImageTask/Record",
    name="提交某个材料活动的信息",
    description="提交某个材料活动的信息",
    response_model=StdResp,
)
async def UP_Create_ImageTaskRecord(newRecord:ImageTaskRecordNewUploadSchema):
    await LL_ImageTaskRecord_NewUpload(newRecord)
    return StdResp

@imageTaskTransactionRouter.get(
    path="/get/ImageActions",
    name="获取所有当前材料提交活动",
    description="获取所有可用的材料提交活动",

)
async def UG_Get_AllImageActionsON():
    ret = await DL_ImageTaskAction_Retrieve_By_On()
    return ret

@imageTaskTransactionRouter.get(
    path="/get/ImageActionById",
    name="获取材料提交的某个活动详细信息",
    description="通过ID获取某个材料提交的详细信息",
)
async def UG_GET_ImageActionDetail_By_ID(action_id:int):
    ret = await DL_ImageTaskAction_Retrieve_By_PK(action_id)
    if ret:
        return ret
    else:
        E404()

@imageTaskTransactionRouter.get(
    path="/get/userImageRecord",
    name="获取用户的材料状态记录",
    description="通过username获取用户的材料状态记录",
    response_model=ImageTaskRecordSchema
)
async def UG_Get_UserImageRecordDetail_By_username_and_act_id(act_id:int,username:str):
    ret = await DL_ImageTaskRecord_Retrieve_by_username_and_Id(username=username,action_id=act_id)
    if ret:
        return ret
    else:
        return E404()

@imageTaskTransactionRouter.post(
    path="/update/userImageRecord",
    name="更新用户的材料状态记录",
    description="通过简要Schema更新",
    response_model=StdResp
)
async def UP_Update_UserImageTaskRecord(data:ImageTaskRecordNewUploadSchema):
    await LL_ImageTaskRecord_Upload(data)
    return StdResp()

@imageTaskTransactionRouter.get(
    path="/get/userClazzImageTaskRecord",
    name="获取班级状况",
    description="通过id和clazz获取班级情况",
)
async def UG_Get_UserClazzTaskRecordStatus_By_id_clazz(action_id:int,clazz:str):
    ret = await LL_RetrieveClazzBriefOfAction_Advanced(action_id=action_id,clazz=clazz)
    return ret
