from fastapi import APIRouter, File, UploadFile

from core.presistence import write_to_path
import os

staticDirectoryRouter = APIRouter(tags=['静态文件管理'])
STATIC_PATH = os.path.join(".", "static")


@staticDirectoryRouter.get(
    path="/get/walk",
    name="获取静态文件库的目录",
)
async def MG_Get_WalkOfStaticFolder():
    pass


@staticDirectoryRouter.post(
    path="/pot/html",
    name="将HTML文件加入到静态文件库中",
)
async def MG_Post_StaticHTMLFile_to_static(file: UploadFile = File(...)):
    filename = file.filename
    filebytes = await file.read()
    filePath = os.path.join(STATIC_PATH, filename)
    await write_to_path(filebytes, filePath)
