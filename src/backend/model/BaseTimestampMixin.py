from tortoise import fields
from tortoise.models import Model


class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")
    create_by = fields.CharField(null=True, default="系统创建", max_length=255, description="创建人")
    update_by = fields.CharField(null=True, default="系统修改", max_length=255, description="修改人")

    class Meta:
        abstract = True
