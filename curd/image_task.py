"""
开发目标：ImageTaskAction/ImageTaskRecord表的CURD
开发标准：
数据层：DataLayer_TargetModel_CURD_By_Param()->
逻辑层：LogicLayer_Name_By_Param()->
开发进度：
ImageTaskAction
ImageTaskRecord
逻辑：

"""
from typing import Optional, List

from .student import DL_Student_Retrieve_By_username
from .user import DL_User_Retrieve_By_username, DL_Users_Retrieve_By_user_clazz
from pydantic import BaseModel
from model.ImageTask import ImageTaskAction, ImageTaskRecord, ImageTaskActionSchema, ImageTaskRecordSchema


# --------ImageTaskAciton------
# Image Task Action Create
## Create Schema

class ImageTaskActionCreateSchema(BaseModel):
    # act_id: int # not used
    act_grant: str
    act_title: str
    act_desc: Optional[str]
    act_range: Optional[str] = "全体"
    act_on: bool = True


# Image Task Action Create Func
async def DL_ImageTaskAction_Create(action: ImageTaskActionCreateSchema):
    await ImageTaskAction.create(**action.dict())


# Image Task Action Update
async def DL_ImageTaskAction_Update_By_RAWSchema(newAction: ImageTaskActionSchema):
    ret = await ImageTaskAction.filter(act_id=newAction.act_id).first()
    await ret.update_from_dict(newAction.dict())
    await ret.save()


# Image Task Action Delete
async def DL_ImageTaskAction_Delete_By_PK(pk: int):
    ret = await ImageTaskAction.filter(act_id=pk).first()
    await ret.delete()


# Image Task Action Retrieve By Available
async def DL_ImageTaskAction_Retrieve_By_On() -> List[ImageTaskActionSchema]:
    ret = await ImageTaskAction.filter(act_on=True).all()
    return [ImageTaskActionSchema(**item.__dict__) for item in ret]


async def DL_ImageTaskAction_Retrieve_By_PK(pk: int):
    ret = await ImageTaskAction.filter(act_id=pk).first()
    return ret


# ---------- Image Task Record
## Image Task Record Create Schema
class ImageTaskRecordCreateSchema(BaseModel):
    # id: int # not used
    act_id: int
    act_username: str
    act_clazz: str
    act_url: str


# Image Task Record Create
async def DL_ImageTaskRecord_Create(newRecord: ImageTaskRecordCreateSchema):
    await ImageTaskRecord.create(**newRecord.dict())


# Image Task Record Update
async def DL_ImageTaskRecord_Update_By_RAWSchema(updateRecord: ImageTaskRecordSchema):
    ret = await ImageTaskRecord.filter(id=updateRecord.id).first()
    await ret.update_from_dict(updateRecord.dict())
    await ret.save()


# Image Task Record Delete
async def DL_ImageTaskRecord_Delete_By_Pk(pk: int):
    ret = await ImageTaskRecord.filter(id=pk).first()
    await ret.delete()


# Image Task Record Retrieve
async def DL_ImageTaskRecord_Retrieve_By_PK():
    pass


async def DL_ImageTaskRecord_Retrieve_By_username():
    pass


async def DL_ImageTaskRecord_Retrieve_By_id():
    pass


async def DL_ImageTaskRecord_Retrieve_by_username_and_Id(username: str, action_id):
    ret = await ImageTaskRecord.filter(act_username=username, act_id=action_id).first()
    if ret:
        return ImageTaskRecordSchema(**ret.__dict__)
    else:
        return None


async def DL_ImageTaskRecord_Retrieve_By_clazz(clazz: str):
    ret = await ImageTaskRecord.filter(act_clazz=clazz).all()
    return [ImageTaskRecordSchema(**item.__dict__) for item in ret]
    pass


# Image Task Record Delete
async def DL_ImageTaskRecord_Delete_By_Id():
    pass


# --------Logic Layer
# same as DL_ImageTaskAction_Create
async def LL_ImageTaskRegisterAction():
    pass


class ImageTaskRecordNewUploadSchema(BaseModel):
    # id: int # not used
    act_id: int
    act_username: str
    act_url: str


async def LL_ImageTaskRecord_Upload(newRecord: ImageTaskRecordNewUploadSchema) -> bool:
    dbData = await ImageTaskRecord.filter(act_id=newRecord.act_id, act_username=newRecord.act_username).first()
    if dbData:
        # Delete it
        await DL_ImageTaskRecord_Delete_By_Pk(dbData.pk)
    user = await DL_User_Retrieve_By_username(newRecord.act_username)
    clazz = user.user_clazz
    try:
        await DL_ImageTaskRecord_Create(
            ImageTaskRecordCreateSchema(
                act_id=newRecord.act_id,
                act_username=newRecord.act_username,
                act_clazz=clazz,
                act_url=newRecord.act_url
            )
        )
        return True
    except:
        return False


# 根据action_id和clazz查看某个班级某个id的简要情况
# disabled
async def LL_RetrieveClazzBriefOfAction(action_id: int, clazz: str) -> list:
    """
    根据班级和活动查看简要情况，首先获得班级全体人员，其次获得每个人的情况,
    目标结构：    List[{username:bool}]
    时间复杂度 和 IO复杂度： o(n2)
    :param action_id:
    :param clazz:
    :return:
    """
    allUserList = await DL_Users_Retrieve_By_user_clazz(clazz)  # all user schema
    uploadedUser = []
    uploadedRecords = await ImageTaskRecord.filter(act_id=action_id, act_clazz=clazz).all()
    for uploadedRecord in uploadedRecords:
        uploadedUser.append(uploadedRecord.act_username)
    target_list = []
    for user in allUserList:
        if user in uploadedUser:
            target_list.append({user: True})
        else:
            target_list.append({user: False})
    return None
    return target_list


async def LL_RetrieveClazzBriefOfAction_Advanced(action_id: int, clazz: str) -> list:
    """
    target json structure:
    [
        {
        username:
        student_name:
        status:
        message:
        }
    ]
    T = O(n2)
    :param action_id:
    :param clazz:
    :return:
    """
    schemaObj = {}
    allUserList = await DL_Users_Retrieve_By_user_clazz(clazz)  # all user schema
    uploadedUser = []
    uploadedRecords = await ImageTaskRecord.filter(act_id=action_id, act_clazz=clazz).all()
    result_list = []
    for uploadedRecord in uploadedRecords:
        uploadedUser.append(uploadedRecord.act_username)
    for user in allUserList:
        student_info = await DL_Student_Retrieve_By_username(user.username)
        if not student_info:
            continue
        schemaObj.update({"username": user.username})
        schemaObj.update({"stu_name": student_info.stu_name})
        if user.username in uploadedUser:
            schemaObj.update({"status": True})
            schemaObj.update({"message": "已提交"})
        else:
            schemaObj.update({"status": False})
            schemaObj.update({"message": "未提交"})
        result_list.append(schemaObj.copy())
    return result_list
