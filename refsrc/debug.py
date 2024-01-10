import datetime

from pyrpt.ProcessMixin import *


def myhello():
    return "hello world"


def noy():
    import subprocess
    import sys
    subprocess.run([sys.executable, "-m", "pip", "install", "openpyxl"], capture_output=True, text=True)


def run_command():
    import openpyxl
    r = openpyxl.Workbook()
    return {"r": str(r)}


def myrouter(say: str):
    global G_num

    return {"hello": say, "g": G_num}


def relave(n):
    return (n)


n = PRTProcedure(assemble(relave, [5]), exchangeKey=b'1234567890123456')
n.auto_run()
print(n.b64string)



class State:
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__.get(item)
