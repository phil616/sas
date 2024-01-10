from fastapi import APIRouter, Request, Depends
from sys import version_info

from core.runtime import GlobalState, get_global_state
from model.User import User

resource_router = APIRouter(prefix="/resources")


@resource_router.get("/secure")
async def DN_ResourcesSecure(req: Request):
    return {"success": req.app.state.user}


@resource_router.get("/systeminfo/version")
async def SN_resourcesGetSysteminfoVersion(state: GlobalState = Depends(get_global_state)):
    u = await state.cache.get("username")
    return {"v": version_info, "s": state.v, "u": u}


@resource_router.get("/get/user/info")
async def SN_resourceGetUserInfo(username: str, state: GlobalState = Depends(get_global_state)):
    await state.cache.set("username", username)



@resource_router.get("/get/global/counter")
async def SN_resourceglobalcounter(counter: int, state: GlobalState = Depends(get_global_state)):
    state.rm.global_counter = counter


@resource_router.get("/get/global/boolean")
async def SN_resourceglobalboolnter(bl: bool, state: GlobalState = Depends(get_global_state)):
    state.rm.global_switch = bl


@resource_router.get("/get/global/state")
async def SN_resourceglobalstate(state: GlobalState = Depends(get_global_state)):
    return {"state": state.runtime.global_switch, "ct": state.runtime.global_counter}

@resource_router.get("/get/crt/state")
async def SN_resourceget_crt_state(r:str,state: GlobalState = Depends(get_global_state)):
    r = await state.runtime.crt(r)
    return {"state": r}
