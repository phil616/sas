"""
开发目标： MoralAction和MoralRecord表的CURD
开发标准：
数据层：DataLayer_TargetModel_CURD_By_Param()->
逻辑层：LogicLayer_Name_By_Param()->
开发进度：
MoralAction表
MoralRecord表
逻辑：
1. 查询所有可用的MoralAction,返回列表
2. 按照username查询MoralRecord,返回列表
"""
from datetime import datetime
from typing import Union, List, Optional

from pydantic import BaseModel

from model.Moral import MoralRecord, MoralAction, MoralRecordSchema, MoralActionSchema


# =========== Data Access Layer
# ------- Moral Action ----------

# Moral Action Create
## Moral Action Create Schema
class MoralActionCreateSchema(BaseModel):
    # action_id: int # Create 模式不能使用主键
    action_on: bool = True
    action_grant: str = "系统创建"
    action_reduce: bool = False
    action_date: Optional[datetime]
    action_score: float
    action_title: str
    action_type: int
    action_detail: Optional[str]


## Moral Action Create Function
async def DL_MoralAction_Create(moralAction: MoralActionCreateSchema):
    await MoralAction.create(**moralAction.dict())


# Moral Action Delete
async def DL_MoralAction_Delete_By_PK(action_id: int):
    result = await MoralAction.filter(action_id=action_id).first()
    await result.delete()


# Moral Action Update
async def DL_MoralAction_Update_By_PK(action_id: int, updateSchema: MoralActionCreateSchema):
    result = await MoralAction.filter(action_id=action_id).first()
    print(updateSchema.dict())
    rs = await result.update_from_dict(updateSchema.dict())
    await rs.save()


# Moral Action Retrieve
## Moral Action Retrieve by PK
async def DL_MoralAction_Retrieve_By_PK(action_id: int) -> MoralActionSchema:
    result = await MoralAction.filter(action_id=action_id).first()
    return MoralActionSchema(**result.__dict__)


## Moral Action Retrieve ALL
async def DL_MoralAction_Retrieve_action_on(isOn=True) -> List[MoralActionSchema]:
    if isOn:
        result = await MoralAction.filter(action_on=True).all()
        return [MoralActionSchema(**item.__dict__) for item in result]
    else:
        result = await MoralAction.all()
        return [MoralActionSchema(**item.__dict__) for item in result]


# ------- Moral Record ----------
# Moral Record Create
## Moral Action Create Schema

class MoralRecordCreateSchema(BaseModel):
    # rec_id: int # Create 模式不能使用主键
    action_id: int
    action_score: float
    rec_username: str
    rec_urls: str
    rec_msg: Optional[str]
    rec_status: int
    chk_username: str
    chk_commit: Optional[str]


async def DL_MoralRecord_Create(moralRecord: MoralRecordCreateSchema):
    await MoralRecord.create(**moralRecord.dict())


# Moral Record Delete
async def DL_MoralRecord_Delete_By_PK(rec_id: int):
    result = await MoralRecord.filter(rec_id=rec_id).first()
    await result.delete()


# Moral Record Update
async def DL_MoralRecord_Update_By_PK(rec_id: int, updateSchema: MoralRecordCreateSchema):
    result = await MoralRecord.filter(rec_id=rec_id).first()
    rs = await result.update_from_dict(updateSchema.dict())
    await rs.save()


# Moral Record Retrieve
## Moral Record Retrieve by PK
async def DL_MoralRecord_Retrieve_By_PK(rec_id: int, rec_username: str) -> MoralRecordSchema:
    result = await MoralRecord.filter(rec_id=rec_id, rec_username=rec_username).first()
    return MoralRecordSchema(**result.__dict__)


# Moral Record Retrieve ALL
async def DL_MoralRecord_Retrieve_All() -> List[MoralRecordSchema]:
    result = await MoralRecord.all()
    return [MoralRecordSchema(**item.__dict__) for item in result]


# =========== Logic Layer
class MoralRecordApplySchema(BaseModel):
    action_id: int
    rec_username: str
    rec_urls: str
    rec_msg: Optional[str]


async def LL_MoralRecordApply_By_ApplySchema(apply: MoralRecordApplySchema):
    applyAction = await DL_MoralAction_Retrieve_By_PK(apply.action_id)
    newSchema = MoralRecordCreateSchema(
        action_id=applyAction.action_id,
        action_score=applyAction.action_score,
        rec_username=apply.rec_username,
        rec_urls=apply.rec_urls,
        rec_msg=apply.rec_msg,
        rec_status=1,
        chk_username="未审核，无审核人"
    )
    await DL_MoralRecord_Create(newSchema)


async def LL_RetrieveUserMoralRecord_By_username(username: str) -> List[MoralRecordSchema]:
    resultList = await MoralRecord.filter(rec_username=username).all()
    return [MoralRecordSchema(**item.__dict__) for item in resultList]


async def LL_RetrieveMoralRecord_Unchecked(status: int = 1) -> List[MoralRecordSchema]:
    resultList = await MoralRecord.filter(rec_status=status).all()
    return [MoralRecordSchema(**item.__dict__) for item in resultList]


class MoralRecordCheckerSchema(BaseModel):
    rec_id: int
    rec_status: int
    chk_username: str
    chk_commit: Optional[str]


async def LL_UpdateOrCheckMoralRecord_CheckSchema(updateRecord: MoralRecordCheckerSchema):
    rec = await MoralRecord.filter(rec_id=updateRecord.rec_id).first()
    rec.rec_status = updateRecord.rec_status
    rec.chk_username = updateRecord.chk_username
    rec.chk_commit = updateRecord.chk_commit
    await rec.save()


class UserCurrentMoralScoreSchema(BaseModel):
    datetime: datetime
    total: float
    uncheck: float
    reduce: float
    checked: float
    reject: float


async def LL_GetUserCurrentMoralScore_By_username(username: str) -> UserCurrentMoralScoreSchema:
    resultList = await MoralRecord.filter(rec_username=username).all()
    uncheck: float = 0.0
    checked: float = 0.0
    reduce: float = 0.0
    reject: float = 0.0
    for resultItem in resultList:
        if resultItem.rec_status == 1:
            uncheck += resultItem.action_score
        elif resultItem.rec_status == 2:
            checked += resultItem.action_score
        elif resultItem.rec_status == 3:
            reject += resultItem.action_score
        elif resultItem.rec_status == 4:
            reduce += resultItem.action_score
        else:
            pass
    total = checked + reduce
    return UserCurrentMoralScoreSchema(
        datetime=datetime.now(), total=total, uncheck=uncheck,
        reduce=reduce, checked=checked, reject=reject
    )
