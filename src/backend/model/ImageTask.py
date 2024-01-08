from .BaseTimestampMixin import TimestampMixin
from tortoise import fields
from pydantic import BaseModel
from typing import Optional
import datetime


class ImageTaskAction(TimestampMixin):
    act_id = fields.IntField(pk=True, description="唯一主键")
    act_grant = fields.CharField(max_length=255, default="系统授权", null=False, description="活动发起人")
    act_title = fields.CharField(max_length=255, null=False, description="标题")
    act_desc = fields.CharField(max_length=255, null=True, description="详情")
    act_range = fields.CharField(max_length=255, null=True, default="全体", description="范围")
    act_on = fields.BooleanField(null=False, default=True, description="是否启用")

    class Meta:
        table_description = "照片材料活动表"
        table = "image_task_action"


class ImageTaskRecord(TimestampMixin):
    id = fields.IntField(pk=True, description="唯一主键")
    act_id = fields.IntField(null=False, description="关联的活动ID")
    act_username = fields.CharField(max_length=255, null=False, description="申请人")
    act_clazz = fields.CharField(max_length=255, null=False, description="申请人班级")
    act_url = fields.CharField(max_length=255, null=False, description="活动的链接")

    class Meta:
        table_description = "照片材料记录表"
        table = "image_task_record"


class ImageTaskActionSchema(BaseModel):
    act_id: int
    act_grant: str
    act_title: str
    act_desc: Optional[str]
    act_range: Optional[str] = "全体"
    act_on: bool = True

    class Config:
        orm_mode = True


class ImageTaskRecordSchema(BaseModel):
    id: int
    act_id: int
    act_username: str
    act_clazz: str
    act_url: str

    class Config:
        orm_mode = True
