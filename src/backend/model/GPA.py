from .BaseTimestampMixin import TimestampMixin
from tortoise import fields
from pydantic import BaseModel
from typing import Optional,Dict


class GPA(TimestampMixin):
    gpa_id = fields.IntField(pk=True, description='主键id')
    username = fields.CharField(max_length=255, null=False, description='用户的名称')
    gpa_type = fields.CharField(max_length=255, null=False, description='类型')
    gpa_score = fields.CharField(max_length=255, null=False, description='分数')
    gpa_time = fields.CharField(max_length=255, null=False, description='事件')
    class Meta:
        table_description = "成绩表"
        table = "gpa_score"

class GPASchema(BaseModel):
    username:str
    gpa_type:str
    gpa_score:str
    gpa_time:str