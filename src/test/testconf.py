import json
import pymysql
BASEURL = "http://localhost"
BASEPORT = 80
V1PREFIX = "/api/v1"
V1URL = f"{BASEURL}:{BASEPORT}{V1PREFIX}"
STDSUCCESS_RESP = {
  "code": 200,
  "data": "success",
  "msg": None
}
STD_RESP = json.dumps(STDSUCCESS_RESP)

DBCONFIG = {
    'host': 'localhost',  # 数据库主机地址
    'user': 'root',  # 数据库用户名
    'password': '123456',  # 数据库密码
    'database': 'sas_beta_api',  # 数据库名
    'charset': 'utf8mb4',  # 字符编码
    'cursorclass': pymysql.cursors.DictCursor
}