from pydantic import BaseModel as BaseSettings
from typing import List


class Config():
    DEBUG = True
    # TODO 文档信息，标题，简介Swagger信息
    # 跨域请求
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]

    # Jwt
    JWT_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"  #
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60

    MYSQL_TABLE_AUTOGEN = True

    # Wechat
    # WX_MINI_APPID = "wx03c5f3aab382a122"  # Debug
    WX_MINI_APPID = "wxe1c0c0fe6041bc8f"


    WX_MINI_SECRET = "***"
    WX_MINI_URL = f"https://api.weixin.qq.com/sns/jscode2session?appid={WX_MINI_APPID}&secret={WX_MINI_SECRET}"

    # Email server
    EMAIL_USERNAME: str = ""
    EMAIL_PASSWORD: str = ""
    EMAIL_HOST_SERVER: str = "smtp.163.com"


class DataConfig():
    # -----------------MySQL-----------
    DB_ORM_CONFIG: dict = {
        "connections": {
            "base": {  # 名为base的基本数据库
                'engine': 'tortoise.backends.mysql',
                "credentials": {
                    'host': 'localhost',
                    'user': 'root',
                    'password': '123456',
                    'port': 3306,
                    'database': 'sas_beta_api',  # 数据库名称
                }
            },
        },
        "apps": {
            "base": {
                "models": [  # 列表应该包含所有的ORM映射文件
                    "model.File",
                    "model.User",
                    "model.Moral",
                    "model.Student",
                    "model.MIT",
                    "model.ImageTask",
                    "model.Doc"
                ],
                "default_connection": "base"  # 链接的数据源
            },
        },
        'use_tz': False,
        'timezone': 'Asia/Shanghai'
    }
    MYSQL_TABLE_AUTOGEN: bool = True
    # -----------------Redis-----------
    CACHE_CONFIG: dict = {
        "CACHE_HOST": "localhost",  # Redis连接
        "CACHE_PORT": 6379,  # Redis端口
        "CACHE_CP": "utf-8",  # Redis CodePage （编码）
        "CACHE_decode_responses": True  # 与Redis的连接编码，True会将结果返回为字符串
    }
    CACHE_URL: str = f"redis://{CACHE_CONFIG['CACHE_HOST']}:{CACHE_CONFIG['CACHE_PORT']}"
    CACHE_DB_IDX: dict = {
        "system": 0,
        "code": 1,
        "log": 2,
        "access": 3,
        "info": 4,
        "doc": 5
    }
    # -------------DISK--------------
    SINGLE_FILE_STORAGE_PATH: List = [".", "storage", "single"]
    META_FILE_STORAGE_PATH: List = [".", "storage", "meta"]
    # -------------AES---------------
    encrypted_items = [
        'student_card_id', 'student_nation', 'student_polical', 'student_home', 'student_origin',
        'student_source', 'student_phone', 'student_email', 'student_dormitory',
    ]
    # ------------- Mongo DB --------
    mongodbinfo = {
        'host': 'localhost',
        'port': 27017,
        'username': 'admin',
        'password': '123456',
        'db': 'sas_beta',
        'authentication_source': 'admin'
    }

class DeployConfig():
    APP_DEBUG: bool = True
    APP_RELOAD: bool = False
    APP_RUN_PORT: int = 8000
    APP_RUN_HOST: str = "127.0.0.1"
    APP_WORKERS: int = 4
    APP_SSL_ENABLE: bool = False
    APP_ENCRYPT_SECRET: str = "ccu_sas"


app_cfg = Config()
data_cfg = DataConfig()
run_cfg = DeployConfig()
