"""
开发目标：MIT表的CURD
开发标准：
数据层：DataLayer_TargetModel_CURD_By_Param()->
逻辑层：LogicLayer_Name_By_Param()->
开发进度：
MIT
逻辑：

"""
from typing import Optional, Union

from model.MIT import MIT, MITSchema
from pydantic import BaseModel


# ------MIT Data ----
# MIT Create
## MIT Create Schema
class MITCreateSchema(BaseModel):
    #  id: int  # Not in Create
    username: str
    mit_status: int
    mit_attachments: Optional[str]
    mit_info: Optional[str]
    mit_choice: int = 0
    mit_on: bool = True
    mit_msgmap: Optional[str]


# MIT Create func
async def DL_MIT_Create(mit: MITCreateSchema):
    await MIT.create(**mit.dict())


# MIT Delete func
async def DL_MIT_Delete_By_pk():
    pass


async def DL_MIT_Delete_By_username(username: str):
    pass


# MIT Update Full
async def DL_MIT_Update_By_RawSchema(mit: MITSchema):
    result = await MIT.filter(username=mit.username).first()
    await result.update_from_dict(mit.dict())
    await result.save()


# MIT Update On
async def DL_MIT_Update_ON_By_CreateSchema(mit: MITCreateSchema):
    result = await MIT.filter(username=mit.username).first()
    if result.mit_on is False:
        # not allow to access or modify
        return False
    else:
        await result.update_from_dict(mit.dict())
        await result.save()


# MIT Retrieve username
async def DL_MIT_Retrieve_By_username(username: str) -> Union[None, MITSchema]:
    result = await MIT.filter(username=username).first()
    if result:
        return MITSchema(**result.__dict__)
    else:
        return None


# MIT Retrieve pk
async def DL_MIT_Retrieve_By_pk(pk: int):
    pass


# MIT Retrieve all List
async def DL_MIT_Retrieve_All():
    result = await MIT.all()
    return [MITSchema(**item.__dict__) for item in result]


# MIT Retrieve choice List
async def DL_MIT_Retrieve_By_choice(choice: int):
    results = await MIT.filter(mit_choice=choice).all()
    return [MITSchema(**item.__dict__) for item in results]


async def DL_MIT_Retrieve_By_statusCode(status: int):
    results = await MIT.filter(mit_status=status).all()
    return [MITSchema(**item.__dict__) for item in results]

# ----- MIT Logic Layer

# doc https://www.yuque.com/cst3/orwkic/kw0khrg9kvyblep6

STATUS_CODE_MAPPING = {
    0: '空状态',
    1: '未录入-未知状态-未提交',
    2: '未录入-不参保-未提交',
    3: '未录入-不参保-已提交',
    4: '未录入-参保-未提交',
    5: '未录入-参保-已提交',
    6: '已录入-未知状态-未提交',
    7: '已录入-参保-未提交',
    8: '已录入-参保-已提交',
    9: '已录入-不参保-未提交',
    10: '已录入-不参报-已经提交',
    90: '个人信息问题',
    91: '录入失效问题',
    92: '附件问题',
    93: '其他问题'
}