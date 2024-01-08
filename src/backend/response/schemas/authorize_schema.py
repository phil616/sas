from pydantic import BaseModel
from typing import Optional


class OAuth2ResponseSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"


class OAuth2WechatInfoResponseSchema(OAuth2ResponseSchema):
    openid: str


class WechatLoginServerSchema(BaseModel):
    openid: str
    session_key: str
    unionid: Optional[str]
    errcode: Optional[int]
    errmsg: Optional[str]
