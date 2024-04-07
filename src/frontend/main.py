import streamlit as st
from authencation import login,logout,prelogin
from p_admin import admin_page

from p_user import user_page

def main():
    prelogin()
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'token' not in st.session_state:
        st.session_state.token = ''
    if 'username' not in st.session_state:
        st.session_state.username = ''
        
    if not st.session_state.authenticated:
        login_container = st.container()
        with login_container:
            st.title("登录页面")
            username = st.text_input("用户名")
            password = st.text_input("密码", type="password")
            if st.button("登录"):
                login(username, password)
    else:
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            st.title(f"欢迎 {st.session_state.username}")
        with col3:
            if st.button("退出登录"):
                logout()
        
        # 在这里添加根据用户角色显示不同页面的逻辑
        # 你可以在登录成功后,从后端获取用户角色信息
        # 这里只是一个示例,假设管理员用户名为'admin'
        if "manager" in st.session_state.scopes:
            admin_page()
        elif "staff" in st.session_state.scopes:
            user_page()
        elif "group" in st.session_state.scopes:
            user_page()
        elif "student" in st.session_state.scopes:
            user_page()
        else:
            user_page()
if __name__ == "__main__":
    main()