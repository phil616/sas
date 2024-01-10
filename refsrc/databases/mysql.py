from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import appcfg


async def mysql_connect_test():
    # 我还是怀疑tortoise这个库没有提供直接的用来测试数据库连接的方法
    # 有可能认为所有web都需要MySQL，连不上自然就报错不启动
    ...


async def register_mysql(app: FastAPI):
    """
    注册mysql数据库，自动建表，从config中读取信息
    :param app:
    :return:
    """
    register_tortoise(
        app,
        config=appcfg.DB_ORM_CONFIG,
        generate_schemas=appcfg.MYSQL_TABLE_AUTOGEN,
        add_exception_handlers=False,
    )
