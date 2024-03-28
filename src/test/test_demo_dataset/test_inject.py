import requests
import unittest
import json
import sys
import os
from loguru import logger
# 获取当前文件的路径
current_file_path = os.path.abspath(__file__)
# 获取当前文件的上级目录的路径
parent_dir = os.path.dirname(current_file_path)
# 获取上级目录的上级目录，也就是testconf.py所在的目录
grandparent_dir = os.path.dirname(parent_dir)

# 把这个路径添加到sys.path里
sys.path.insert(0, grandparent_dir)

# 现在你可以安全地导入testconf
import testconf
import pymysql

def execute_sql(sql:str):
    connection = pymysql.connect(**testconf.DBCONFIG)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            logger.info(f"EXECUTING SQL: {sql}")
            connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        # 关闭数据库连接
        connection.close()
    
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        tables = ["user","student_info",'image_task_action',"gpa_score"]
        for table in tables:
            execute_sql(f"DELETE FROM `{table}`;")
        ## clear tables
        with open("userdataset.json","r+",encoding="utf8") as f:
            testdata = json.load(f)
        self.users = testdata.get("users")
        self.students = testdata.get("students")
        with open("authdataset.json","r+",encoding="utf8") as f:
            authdataset = json.load(f)
        self.auth_users = authdataset.get("users")
        self.auth_students = authdataset.get("students")
        with open("imagetaskdataset.json","r+",encoding="utf8") as f:
            image_task = json.load(f)
        self.images_tasks = image_task  # : list [items]
        with open("scorelistdataset.json","r+",encoding="utf8") as f:
            scores = json.load(f)
        self.scorelists = scores
    def setUp(self):
        logger.info("Setting Up test")
    def test_basic_connection(self):
        response = requests.get(testconf.V1URL+"/get/basic/info")
        self.assertEqual(response.status_code, 200)
    def test_create_user(self):
        for user in self.users:
            response = requests.post(testconf.V1URL+"/create/user",json=user)
            self.assertEqual(response.status_code, 200)
            logger.info(f"{user.get('username')} Insert SUCCESS")
    def test_create_student(self):
        for student in self.students:
            response = requests.post(testconf.V1URL+"/post/studentInfo",json=student)
            self.assertEqual(response.status_code, 200)
            logger.info(f"{student.get('stu_name')} Insert SUCCESS")
    def test_token_login(self):
        for user in self.auth_users:
            response = requests.post(testconf.V1URL+"/create/user",json=user)
            self.assertEqual(response.status_code, 200)
            logger.info(f"AUTH : {user.get('username')} Insert SUCCESS")
        for student in self.auth_students:
            response = requests.post(testconf.V1URL+"/post/studentInfo",json=student)
            self.assertEqual(response.status_code, 200)
            logger.info(f"AUTH : {student.get('stu_name')} Insert SUCCESS")
        for user in self.auth_users:
            response = requests.post(
                headers={"Content-Type":"application/x-www-form-urlencoded","accept":"application/json"},
                url=testconf.V1URL+"/token",
                data={
                    "grant_type":"",
                    "username":user.get("username"),
                    "password":user.get("password"),
                    "scope":"",
                    "client_id":"",
                    "client_secret":""
                }
            )
            self.assertEqual(response.status_code, 200)
            logger.info(f"AUTH RESP : {response.json()}")
    def test_create_image_task(self):
        for task in self.images_tasks:
            response = requests.post(url=testconf.V1URL+"/post/ImageTaskAction",json=task)
            self.assertEqual(response.status_code, 200)
            logger.info(f"taskname {task.get('act_title')} insert success")
    def test_create_score_list(self):
        for scores in self.scorelists:
            response = requests.post(url=testconf.V1URL+"/gpa/new/user/score",json=scores)
            self.assertEqual(response.status_code, 200)
            logger.info(f"score for {scores.get('username')} - {scores.get('gpa_type')} insert success")
if __name__ == '__main__':
    unittest.main()