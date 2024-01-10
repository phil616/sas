"""
filename: main.py
describe: 主应用文件
author: 费东旭
date: 2023年11月13日
licence: CCUGTOSL v1.0
doc:https://www.yuque.com/yhwh/rpic/is71kuledns6czan
"""

from fastapi import FastAPI, staticfiles, HTTPException
from config import appcfg
from core.events import startup, stopping
from core.exceptions import http_error_handler
from core.middlewares import BaseMiddleware
from fastapi.middleware.cors import CORSMiddleware
from endpoints.api import api_router


# 创建主要APP对象
application = FastAPI(
    debug=appcfg.APP_DEBUG,
    title=appcfg.APP_TITLE,
    version=appcfg.APP_VERSION,
    description=appcfg.APP_DESC,
    summary=appcfg.APP_SUMMARY
)
# 添加一个基本中间件，这个中间件是一个代码框架，没有任何功能，依赖实现
application.add_middleware(BaseMiddleware)
application.add_middleware(
    CORSMiddleware,
    allow_origins=appcfg.CORS_ORIGINS,
    allow_credentials=appcfg.CORS_ALLOW_CREDENTIALS,
    allow_methods=appcfg.CORS_ALLOW_METHODS,
    allow_headers=appcfg.CORS_ALLOW_HEADERS,
)

# HTTP错误捕获
application.add_exception_handler(HTTPException,http_error_handler)

# 启动和关闭事件触发器
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))

# 挂载一个静态文件夹
application.mount("/static", staticfiles.StaticFiles(directory="static"), name="static")


# 注册总路由
application.include_router(api_router)

