from typing import Union
from response.exceptions import E401
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from fastapi import Request, Depends
from datetime import timedelta, datetime
from pydantic import ValidationError
from config import app_cfg
from curd.user import DL_User_Retrieve_By_username
import jwt
import json
from aiohttp import ClientSession


from response.schemas.authorize_schema import WechatLoginServerSchema

user_scopes = {
    "student": "学生权限",
    "group": "班委和班级负责人权限",
    "staff": "学生组织权限",
    "manager": "组织负责人权限",
    "system": "系统权限"
}

OAuth2 = OAuth2PasswordBearer("/api/v1/token", scopes=user_scopes)


def create_access_token(data: dict) -> str:
    token_data = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=app_cfg.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)  # JWT过期分钟
    token_data.update({"exp": expire})
    jwt_token = jwt.encode(token_data, app_cfg.JWT_SECRET_KEY, algorithm=app_cfg.JWT_ALGORITHM)  # 加入token
    return jwt_token


def scope_mapping(scope: int) -> Union[None, list]:
    if scope == 0:
        return None
    role_scope = []
    if scope & 0b0001:
        role_scope.append("student")
    if scope & 0b0010:
        role_scope.append("group")
    if scope & 0b0100:
        role_scope.append("staff")
    if scope & 0b1000:
        role_scope.append("manager")
    if scope == 255:
        role_scope.append("system")
    return role_scope


async def check_permissions(security_scopes: SecurityScopes, token=Depends(OAuth2)):
    username = None
    user_scope = []
    try:
        payload = jwt.decode(token, app_cfg.JWT_SECRET_KEY, algorithms=[app_cfg.JWT_ALGORITHM])
        if payload:
            username = payload.get("usr", None)  # 用户id
            user_scope = payload.get("scope", None)  # 用户scope
            if username is None:
                E401("凭证无法使用", {"WWW-Authenticate": f"Bearer {token}"})
        else:
            E401("无效凭证", {"WWW-Authenticate": f"Bearer {token}"})
    except jwt.ExpiredSignatureError:
        E401("凭证已证过期", {"WWW-Authenticate": f"Bearer {token}"})
    except jwt.InvalidTokenError:
        E401("凭证无法正确解析", {"WWW-Authenticate": f"Bearer {token}"})
    except (jwt.PyJWTError, ValidationError):
        E401("凭证解析失败", {"WWW-Authenticate": f"Bearer {token}"})

    check_user = await DL_User_Retrieve_By_username(username)
    if not check_user or check_user.user_scope == 0:
        E401("用户不存在或已经被管理员禁用", {"WWW-Authenticate": f"Bearer {token}"})
    if security_scopes.scopes:
        req_scopes = security_scopes.scopes
        if not set(req_scopes).issubset(set(user_scope)):  # 集合方法来验证是否拥有足够的权限
            E401(f"您没有足够的权限", {"WWW-Authenticate": f"Bearer {token}"})


async def wechat_request(code: str) -> WechatLoginServerSchema:
    errormsg = {  # 翻译
        "40029": "js_code无效",
        "45011": "API 调用太频繁，请稍候再试",
        "40226": "高风险等级用户，小程序登录拦截",
        "-1": "系统繁忙，此时请开发者稍候再试"
    }
    url = app_cfg.WX_MINI_URL + "&js_code=" + str(code) + str("&grant_type=authorization_code")
    async with ClientSession() as session:
        async with session.get(url) as response:
            res = await response.text()
    d = dict(json.loads(res))
    try:
        return WechatLoginServerSchema(**d)
    except:
        E401(d.get('errmsg'))
