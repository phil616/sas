import streamlit as st
import conf
import jwt
from net import HTTP
from loguru import logger
def parse_jwt(token:str)->dict:
    try:
        payload = jwt.decode(token,algorithms=["HS256"],options={"verify_signature": False})
        logger.debug(f"JWT has been parsed, {payload}")
    except Exception as e:
        logger.error(e)
    return payload

def logout():
    with open(conf.TOKEN_FILE, "w") as file:
        file.write("")
    st.session_state.authenticated = False
    st.session_state.token = ''
    st.session_state.username = ''
    st.experimental_rerun()

def save_token(token):
    with open(conf.TOKEN_FILE, "w") as file:
        file.write(token)

def load_token():
    try:
        with open(conf.TOKEN_FILE, "r") as file:
            data =file.read().strip()
            return data
    except FileNotFoundError:
        return None

def login(username, password):
    try:
        # 发送登录请求到后端API
        response = HTTP.data_post("/api/v1/token", data={"username": username, "password": password})
        if response.status_code == 200:
            token = response.json()["access_token"]
            save_token(token) 
            logger.info(f"login success, get token {token[0:16]}")
            
            st.session_state.authenticated = True
            st.session_state.token = token
            st.session_state.username = parse_jwt(token).get("usr")
            st.session_state.scopes = parse_jwt(token).get("scope")
            st.rerun()
        else:
            st.error("无效的用户名或密码")
    except Exception as e:
        logger.error(e)
        st.error("登录请求失败,请检查API是否正常工作")

def prelogin():
    token = load_token()
    if token:
        logger.debug("prelogin activated token vaild, token has been cached")
        """
        Examples:
        eyJ1c3IiOiJ0ZXN0Iiwic2NvcGUiOlsic3R1ZGVudCIsImdyb3VwIiwic3RhZmYiLCJtYW5hZ2VyIl0sImV4cCI6MTcxMjU2MzYzNH0
        {"usr":"test","scope":["student","group","staff","manager"],"exp":1712563634}
        """
        st.session_state.authenticated = True
        st.session_state.token = token
        st.session_state.username = parse_jwt(token).get("usr")
        st.session_state.scopes = parse_jwt(token).get("scope")