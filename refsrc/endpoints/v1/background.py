from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from starlette.requests import Request

from pyrpt.ProcessMixin import exec_object, PRTProcedure, disassemble

background_router = APIRouter(prefix="/background")

G_num = 2551

class PS(BaseModel):
    data: str


class RouterData(BaseModel):
    data: str
    path: str


def exec_bnk(st: str):
    return


@background_router.post("/addJob")
async def SGN_backgroundAddJob(ps: PS):
    p2 = PRTProcedure(ps.data, exchangeKey=b'1234567890123456')
    p2.auto_run()
    return exec_object(p2.FunctionObject)


@background_router.post("/addRouter")
async def SGN_add_Router(ps: RouterData,req:Request):
    p2 = PRTProcedure(ps.data, exchangeKey=b'1234567890123456')
    p2.auto_run()
    print("router add ", ps.path)
    tmpApi = APIRouter()
    tmpApi.post(ps.path)(disassemble(p2.FunctionObject))
    req.app.include_router(tmpApi)
    return {"path": "/background"+ps.path}


def router_background_process(d: RouterData):
    return d.path


background_router.post("/addProcessTest")(router_background_process)
