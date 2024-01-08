# doc https://www.yuque.com/cst3/orwkic/qmfs4lrkqdvdu98z
import pickle

import jwt
from fastapi import APIRouter, Header, Security
from pydantic import BaseModel
from starlette.requests import Request

from config import app_cfg
from core.authorize import check_permissions
from curd.student import SYNC_LL_VerifyBearer2Student, DL_Student_Retrieve_By_username, DL_Student_Update, \
    DL_Student_Create
from response.exceptions import E401, E404
from model.Student import StudentSchema
from response.schemas.stdresp import StdResp
from database import redis
studentTransactionRouter = APIRouter(tags=['学生信息事务'])

@studentTransactionRouter.on_event("startup")
async def startup():
    studentTransactionRouter.redis = await redis.info_cache()
    pass

#SIP1
@studentTransactionRouter.get(
    path="/get/studentInfo",
    name="获取学生信息",
    description="通过token获取学生信息",
    response_model=StudentSchema,
    dependencies=[Security(check_permissions, scopes=["student"])]
)
async def UMG_StudentInfo_By_username(username: str, req: Request):
    token = req.headers.get('Authorization')
    if token is None:
        E401()
    if SYNC_LL_VerifyBearer2Student(token.split(" ")[1], username):
        cacheInfo = await studentTransactionRouter.redis.get(username)
        if cacheInfo:
            return pickle.loads(cacheInfo)
        ret = await DL_Student_Retrieve_By_username(username)
        if ret is not None:
            await studentTransactionRouter.redis.set(username, pickle.dumps(ret))
            return ret
        else:
            E404(f"未能查询到{username}的相关信息")
    else:
        E401()
#SIP2
@studentTransactionRouter.post(
    path="/update/studentInfo",
    name="修改学生信息",
    description="通过token修改学生信息",
    response_model=StdResp,
    dependencies=[Security(check_permissions, scopes=["student"])]
)
async def UMG_StudentInfoUpdate_By_ROWSchema(student:StudentSchema,req:Request):
    token = req.headers.get('Authorization')
    if token is None:
        E401()
    if SYNC_LL_VerifyBearer2Student(token.split(" ")[1], student.username):
        await DL_Student_Update(student)
        await studentTransactionRouter.redis.set(student.username, pickle.dumps(student))
        return StdResp()
    else:
        E401()
#SIP3
@studentTransactionRouter.post(
    path="/post/studentInfo",
    name="创建学生信息",
    description="创建一个完整的学生信息",
    response_model=StdResp
)
async def MP_StudentInfoCreateNew_By_ROWSchema(student: StudentSchema):
    await DL_Student_Create(student)
    await studentTransactionRouter.redis.set(student.username,pickle.dumps(student))
    return StdResp()
# SIP4
@studentTransactionRouter.get(
    path="/post/studentInfo",
    name="删除学生信息",
    description="删除一个学生的档案信息",
    response_model=StdResp
)
async def MG_StudentInfoDelete_By_username(username:str):
    pass

class TokenSchema(BaseModel):
    token:str

@studentTransactionRouter.post(
    path="/get/userManagerRole",
    name="获取学生的角色信息",
    description="通过token获取一个学生的信息",
    dependencies=[Security(check_permissions, scopes=["student"])]
)
async def UG_StudentUsernameGetUserScopes_By_TokenSchema(token:TokenSchema):
    payload = jwt.decode(token.token, app_cfg.JWT_SECRET_KEY, algorithms=[app_cfg.JWT_ALGORITHM])
    if payload:
        user_scope = payload.get("scope", None)  # 用户scope
        return user_scope
