"""
开发目标： User表和UserWechat表的增删改查
开发标准：
数据层：DataLayer_TargetModel_CURD_By_Param()->
逻辑层：LogicLayer_Name_By_Param()->
开发进度：
User表
UserWechat表
逻辑层：
1.用户通过用户名密码鉴权
2.用户通过用户名和Openid绑定
"""

from model.User import User, UserSchema, UserWechat, UserWechatSchema
from typing import Union, List
from libs.crypt import crypter
from core.logger import logger


# -----User-----
# User Create

async def DL_User_Create_By_Schema(user: UserSchema) -> bool:
    try:
        user.password = crypter.encrypt_b(user.password)
        await User.create(**user.dict())
        return True
    except Exception as e:
        logger.exception(e)
        return False


# User Delete
async def DL_User_Del_By_username(username: str) -> bool:
    pass


# User Update
async def DL_User_Update_By_Schema(user: UserSchema) -> bool:
    try:
        oldUser = await User.filter(username=user.username).first()
        rs = await oldUser.update_from_dict(user.dict())
        await rs.save()
        return True
    except Exception as e:
        logger.exception(e)
        return False


# User Retrieve
async def DL_User_Retrieve_By_username(username: str) -> Union[None, User]:
    try:
        user = await User.filter(username=username).first()
        return user
    except Exception as e:
        logger.exception(e)
        return None
async def DL_User_Retrieve_ALL()->List[User]:
    users = await User.all()
    return users

async def DL_User_Retrieve_By_openid(openid: str) -> Union[None, User]:
    user = await UserWechat.filter(openid=openid).first()
    if user:
        result = await DL_User_Retrieve_By_username(user.username)
        return result
    else:
        return None
async def DL_Users_Retrieve_By_user_clazz(clazz:str)->List[UserSchema]:
    users = await User.filter(user_clazz=clazz).all()
    user_list = []
    for user in users:
        user_list.append(UserSchema(**user.__dict__))
    return user_list

# -------UserWechat-------
# UserWechat Create
async def DL_UserWechat_Create_By_Schema(uwx: UserWechatSchema) -> bool:
    pass


# UserWechat Delete
async def DL_UserWechat_Del_By_username() -> bool:
    pass


async def DL_UserWechat_Del_By_openid() -> bool:
    pass


# UserWechat Update
async def DL_UserWechat_Update_By_Schema() -> bool:
    pass


# UserWechat Retrieve
async def DL_UserWechat_Retrieve_By_openid() -> bool:
    pass


async def DL_UserWechat_Retrieve_By_username(username: str) -> Union[None, UserWechat]:
    pass


# -----------Logic Layer Functions----------

async def LL_AuthenticateUser_By_username(username: str, password: str) -> Union[None, User]:
    user = await User.filter(username=username).first()
    if not user:
        return None
    if crypter.verify_b(password, user.password):
        return user
    else:
        return None


async def LL_BindUserWechat_By_username_openid(username: str, openid: str) -> bool:
    try:
        await UserWechat.create(username=username, openid=openid)
        return True
    except Exception as e:
        logger.exception(e)
        return False

async def LL_UpdatePassword2NewPwd_By_NewAndOld(username:str,newPassword:str,oldPassword:str)->bool:
    user = await User.filter(username=username).first()
    if crypter.verify_b(oldPassword,user.password):
        user.password = crypter.encrypt_b(newPassword)
        await user.save()
        return True
    else:
        return False

