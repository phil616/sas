from tortoise import fields
from .BaseTimestampMixin import TimestampMixin
from typing import List, Optional
from pydantic import BaseModel


class MessageDoc(TimestampMixin):
    id = fields.IntField(pk=True, description='主键id')
    name = fields.CharField(max_length=255, null=False, unique=True, description="消息名称")
    message = fields.CharField(max_length=2047, null=True, description='消息内容')

    class Meta:
        table_description = "消息表"
        table = "message_doc"


class RichDoc(TimestampMixin):
    id = fields.IntField(pk=True, description='主键id')
    name = fields.CharField(max_length=255, null=False, unique=True, description="文档名称")
    richtext = fields.TextField(max_length=16777215, description="文档主体")

    class Meta:
        table_description = "文档表"
        table = "rich_doc"


class MessageDocSchema(BaseModel):
    id: int
    name: str
    message: Optional[str]

    class Config:
        orm_mode = True


class RichDocSchema(BaseModel):
    id: int
    name: str
    richtext: Optional[str]

    class Config:
        orm_mode = True
