import streamlit as st
import requests
from net import HTTP
from conf import BASEURL as API_URL
"""
USER fields:
{
  "username": "string",
  "password": "string",
  "user_scope": 0,
  "user_clazz": "string",
  "user_phone": "string",
  "user_info": {}
}
"""
def get_users():
    response = HTTP.get("/api/v1/get/users")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("获取学生数据失败")
        return []

def add_user(user):
    response = HTTP.json_post("/api/v1/create/user", json=user)
    if response.status_code == 200:
        st.success("学生添加成功")
    else:
        st.error("学生添加失败")

def update_user(student_id, updated_student):
    response = HTTP.json_post("/api/v1/update/{student_id}", json=updated_student)
    if response.status_code == 200:
        st.success("学生信息更新成功")
    else:
        st.error("学生信息更新失败")

def delete_user(student_id):
    response = requests.delete(f"{API_URL}/api/v1/delete/user/{student_id}")
    if response.status_code == 204:
        st.success("学生删除成功")
    else:
        st.error("学生删除失败")
def inline_user_curd():
    st.header("学生信息管理")
    users = get_users()
    if users:
        for user in users:
            # exclude field: password,update_time
            user.pop("password")
            user.pop("update_time")
        st.write("\n使用 st.table() 展示用户信息:")
        st.table(users)
        # 添加学生
    st.subheader("添加学生")
    with st.form(key='add_student_form'):
        username = st.text_input("用户名")
        password = st.text_input("密码")
        user_scope = st.number_input("用户权限", min_value=0, max_value=15, step=1)
        user_clazz = st.text_input("班级")
        user_phone = st.text_input("手机号")
        user_info = st.text_input("用户信息")

        if st.form_submit_button(label='添加'):
            user = {"username": username, "password": password, "user_scope": user_scope, "user_clazz": user_clazz, "user_phone": user_phone, "user_info": user_info}
            add_user(user)
        
    # 更新用户信息
    st.subheader("更新用户信息")
    with st.form(key='update_user_form'):
        student_id = st.number_input("学生ID", min_value=1, step=1)
        username = st.text_input("用户名")
        password = st.text_input("密码")
        user_scope = st.number_input("用户权限", min_value=0, max_value=15, step=1)
        user_clazz = st.text_input("班级")
        user_phone = st.text_input("手机号")
        user_info = st.text_input("用户信息")

        if st.form_submit_button(label='更新'):
            updated_user = {"username": username, "password": password, "user_scope": user_scope, "user_clazz": user_clazz, "user_phone": user_phone, "user_info": user_info}
            update_user(student_id, updated_user)
        
        
    # 删除学生
    st.subheader("删除用户")
    with st.form(key='delete_student_form'):
        user_id = st.number_input("用户ID", min_value=1, step=1)
        if st.form_submit_button(label='删除'):
            delete_user(user_id)
    st.write("这里是学生信息管理页面")