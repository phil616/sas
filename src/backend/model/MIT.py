from .BaseTimestampMixin import TimestampMixin
from tortoise import fields
from pydantic import BaseModel
from typing import Optional


class MIT(TimestampMixin):
    id = fields.IntField(pk=True, description="主键")
    username = fields.CharField(null=False, unique=True, max_length=127, description="用户名")
    mit_status = fields.IntField(null=False, default=0, description="当年医保状态")
    mit_attachments = fields.CharField(null=True, max_length=255, description="医保信息附件url")
    mit_info = fields.JSONField(null=True, description="医保系统使用的信息")
    mit_choice = fields.IntField(null=False, default=0, description="参保状态")
    mit_on = fields.BooleanField(null=False, default=True, description="允许编辑")
    mit_msgmap = fields.CharField(null=True, max_length=255, description="状态码对应的信息")

    class Meta:
        table_description = "医保登记表"
        table = "mit"


class MITSchema(BaseModel):
    id: int
    username: str
    mit_status: int
    mit_attachments: Optional[str]
    mit_info: Optional[dict]  # 正常情况下留空
    mit_choice: int = 0
    mit_on: bool = True
    mit_msgmap: Optional[str]

    class Config:
        orm_mode = True
