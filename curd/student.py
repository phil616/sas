from typing import Union
import jwt

from config import app_cfg
from model.Student import Student, StudentSchema, AES_required
from libs.crypt import crypter

"""
开发目标： Student的CURD
开发标准：
数据层：DataLayer_TargetModel_CURD_By_Param()->
逻辑层：LogicLayer_Name_By_Param()->
开发进度：
Student
逻辑：
1. 根据加密需求进行加密
2. 根据解密需求进行解密
"""

ALLOW_ACCESS_SCOPE = ['manager', 'system', 'staff']


# Student Create
async def DL_Student_Create(newStudent: StudentSchema):
    # 遍历newStudent的kv,如果k在AES_require里面，则使用AES加密，否则略过
    data = _SYNC_LL_StudentEncryptAES_By_Dict(newStudent.dict())
    print(data)
    await Student.create(**data)


# Student Delete
async def DL_Student_Delete(username: str) -> bool:
    pass


# Student Update
async def DL_Student_Update(newStudent: StudentSchema):
    student = await Student.filter(username=newStudent.username).first()
    await student.update_from_dict(_SYNC_LL_StudentEncryptAES_By_Dict(student.__dict__))
    await student.save()


# Student Retrieve
async def DL_Student_Retrieve_By_username(username: str) -> Union[None, StudentSchema]:
    student = await Student.filter(username=username).first()
    if student:
        return StudentSchema(**_SYNC_LL_StudentDecryptAES_By_Dict(student.__dict__))
    else:
        return None


def _SYNC_LL_StudentEncryptAES_By_Dict(oriDict: dict) -> dict:
    cp_dict = oriDict.copy()
    for infoItem in cp_dict.items():
        if infoItem[0] in AES_required:
            epd = crypter.encrypt_AES(infoItem[1])
            cp_dict.update({infoItem[0]: epd})
    return cp_dict


def _SYNC_LL_StudentDecryptAES_By_Dict(oriDict: dict) -> dict:
    cp_dict = oriDict.copy()
    for infoItem in cp_dict.items():
        if infoItem[0] in AES_required:
            epd = crypter.decrypt_AES(infoItem[1])
            cp_dict.update({infoItem[0]: epd})
    return cp_dict


def SYNC_LL_VerifyBearer2Student(token: str, ret_username: str) -> bool:
    try:
        payload = jwt.decode(token, app_cfg.JWT_SECRET_KEY, algorithms=[app_cfg.JWT_ALGORITHM])
        username = payload.get("usr")
        if username == ret_username:
            return True
        else:  # 判断scope是否拥有足够的权限
            scope = payload.get("scope")
            for allow_scope in ALLOW_ACCESS_SCOPE:
                if allow_scope in scope:
                    return True
            return False
    except:
        return False
