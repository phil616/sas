from .BaseTimestampMixin import TimestampMixin
from tortoise import fields
from pydantic import BaseModel
from typing import Optional
import datetime


class MoralAction(TimestampMixin):
    action_id = fields.IntField(pk=True, description="主键")
    action_on = fields.BooleanField(null=False, default=True, description="是否启用")
    action_grant = fields.CharField(null=False, default="系统创建", max_length=255, description="发起授权人")
    action_reduce = fields.BooleanField(null=False, default=False, description="是否为扣分项目")
    action_date = fields.DatetimeField(null=True, auto_now=True, description="活动时间")
    action_score = fields.FloatField(null=False, description="分值")
    action_type = fields.IntField(null=False, default=1, description="主键")
    action_title = fields.CharField(null=False, max_length=255, description="活动标题")
    action_detail = fields.CharField(null=True, max_length=255, description="活动详情")

    class Meta:
        table_description = "德育分活动表"
        table = "moral_action"


class MoralActionSchema(BaseModel):
    action_id: int
    action_on: bool = True
    action_grant: str = "系统创建"
    action_reduce: bool = False
    action_date: Optional[datetime.datetime]
    action_score: float
    action_title: str
    action_type: int = 1
    action_detail: Optional[str]

    class Config:
        orm_mode = True


class MoralActionResponseSchema(MoralActionSchema):
    action_id: int


class MoralRecord(TimestampMixin):
    rec_id = fields.IntField(pk=True, description="主键")
    action_id = fields.IntField(description="关联主键")
    action_score = fields.FloatField(null=False, description="分值")
    rec_username = fields.CharField(null=False, max_length=255, description="申请人")
    rec_urls = fields.CharField(null=False, max_length=255, description="附件列表")
    rec_msg = fields.CharField(null=True, max_length=255, description="申请留言")
    rec_status = fields.IntField(null=False, description="状态")
    chk_username = fields.CharField(null=False, default="尚未审核", max_length=255, description="审核人")
    chk_commit = fields.CharField(null=True, max_length=255, description="审核信息")

    class Meta:
        table_description = "德育分记录表"
        table = "moral_record"


class MoralRecordSchema(BaseModel):
    rec_id: int
    action_id: int
    action_score: float
    rec_username: str
    rec_urls: str
    rec_msg: Optional[str]
    rec_status: int
    chk_username: str
    chk_commit: Optional[str]

    class Config:
        orm_mode = True

