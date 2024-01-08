from fastapi import APIRouter, File, UploadFile
from model.Doc import RichDocSchema, MessageDocSchema
from curd.doc import DL_DocMessage_Retrieve_By_name, DL_DocMessage_Update_By_RAWSchema, MessageDocCreateSchema, \
    DL_RichDoc_Retrieve_By_name, DL_RichDoc_Create, RichDocCreateSchema
from database import redis
from response.exceptions import E404
import pickle

docTransactionRouter = APIRouter(tags=['文档信息事务'], deprecated=True)


@docTransactionRouter.on_event("startup")
async def startup():
    docTransactionRouter.redis = await redis.doc_cache()


@docTransactionRouter.get(
    path="/get/latestNew",
    name="最新通知",
    description="获取最新通知字符串"
)
async def UG_GET_LatestNews():
    ret = await DL_DocMessage_Retrieve_By_name("latest_new")
    print(ret)
    if ret:
        return ret
    else:
        E404()


@docTransactionRouter.post(
    path="/update/latestNew",
    name="更新最新通知",
    description="更新最新通知字符串"
)
async def UG_GET_LatestNews(msg: MessageDocCreateSchema):
    await DL_DocMessage_Update_By_RAWSchema(msg)


@docTransactionRouter.get(
    path="/get/richdoc",
    name="获取富文本",
    description="根据文档名获取富文本",
)
async def UG_GET_RichDoc_By_name(name: str):
    ret = await DL_RichDoc_Retrieve_By_name(name)
    return ret


@docTransactionRouter.post(
    path="/post/richdoc",
    name="通过文件创建一个富文本",
    description="通过文件对象创建一个富文本",
)
async def UG_GET_RichDoc_By_file(name: str, file: UploadFile = File(...)):
    fileString = await file.read()
    await DL_RichDoc_Create(RichDocCreateSchema(name=name, richtext=fileString.decode("utf8")))
