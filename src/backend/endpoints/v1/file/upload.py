import os
from fastapi import APIRouter, UploadFile, File
from starlette.responses import FileResponse

from core.utils import random_str, gen_file_hash
from core.presistence import write_to_path
from config import data_cfg
from model.File import FileMetaInfo, FileInfo, FileList, FileStorageResp
from response.exceptions import E401

upload_route = APIRouter(tags=["文件操作"])


@upload_route.post("/upload/new")
async def upload_new_file(fileMIME: str, fileSize: int, fileName: str, file: bytes = File(...)):
    fileBytes = file
    fileHash = gen_file_hash(fileBytes)
    fileId = random_str()
    filePath = os.path.join(*data_cfg.SINGLE_FILE_STORAGE_PATH, fileId)
    info = FileMetaInfo(
        **(FileInfo(
            file_id=fileId,
            file_name=fileName,
            file_size=fileSize,
            file_mime_type=fileMIME,
            file_path=filePath
        ).dict())
        ,
        file_hash=fileHash
    )
    await write_to_path(fileBytes, filePath)
    newFile = await FileList.create(**info.dict())
    resp = FileStorageResp(file_id=newFile.pk, file_uid=fileId, file_name=fileName, file_shared=False)
    return resp


@upload_route.post("/upload/file")
async def upload_new_fileObject(file: UploadFile,filename:str):
    fileBytes = await file.read()
    fileHash = gen_file_hash(fileBytes)
    if filename:
        fileName = filename
    else:
        fileName = file.filename
    file.file.seek(0, 2)
    fileSize = file.file.tell()
    fileMIME = file.content_type
    fileId = random_str()
    filePath = os.path.join(*data_cfg.SINGLE_FILE_STORAGE_PATH, fileId)
    info = FileMetaInfo(
        **(FileInfo(
            file_id=fileId,
            file_name=fileName,
            file_size=fileSize,
            file_mime_type=fileMIME,
            file_path=filePath
        ).dict())
        ,
        file_hash=fileHash
    )
    await write_to_path(fileBytes, filePath)
    newFile = await FileList.create(**info.dict())
    resp = FileStorageResp(file_id=newFile.pk, file_uid=fileId, file_name=fileName, file_shared=False)
    return resp


def abstract_file_gen(file: FileList):
    filePath = file.file_path
    fileName = file.file_name
    fileType = file.file_mime_type
    return FileResponse(filePath, media_type=fileType, filename=fileName)


@upload_route.get("/download/uid")
async def download_by_uid(uid: str):
    file = await FileList.filter(file_id=uid).first()
    if file is None:
        E401("未查询到文件")
    return abstract_file_gen(file)
