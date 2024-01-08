from typing import Optional

from model.Doc import MessageDoc, MessageDocSchema, RichDocSchema, RichDoc

from pydantic import BaseModel


# Doc Message Create schema
class MessageDocCreateSchema(BaseModel):
    name: str
    message: Optional[str]


async def DL_DocMessage_Create(msg: MessageDocCreateSchema):
    await MessageDoc.create(**msg.dict())


async def DL_DocMessage_Delete_by_name():
    pass


async def DL_DocMessage_Delete_by_id():
    pass


async def DL_DocMessage_Update_By_RAWSchema(msg: MessageDocCreateSchema):
    ret = await MessageDoc.filter(name=msg.name).first()
    if ret:
        await ret.update_from_dict(msg.dict())
        await ret.save()
    else:
        print("update success")
        await DL_DocMessage_Create(msg)


async def DL_DocMessage_Retrieve_By_name(name: str):
    ret = await MessageDoc.filter(name=name).first()
    return ret


# ------ RichDoc
# Rich Doc Create Schema
class RichDocCreateSchema(BaseModel):
    name: str
    richtext: str


async def DL_RichDoc_Create(doc: RichDocCreateSchema):
    await RichDoc.create(**doc.dict())
    pass


async def DL_RichDoc_Delete_By_id():
    pass


async def DL_RichDoc_Delete_By_name():
    pass


async def DL_RichDoc_Retrieve_By_name(name: str):
    doc = await RichDoc.filter(name=name).first()
    return doc
