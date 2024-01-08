from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config import data_cfg


async def register_mysql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,
        config=data_cfg.DB_ORM_CONFIG,
        generate_schemas=data_cfg.MYSQL_TABLE_AUTOGEN,
        add_exception_handlers=False,
    )
