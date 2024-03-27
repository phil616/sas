from fastapi import APIRouter

from .localfile import staticDirectory
from .user import login
from .debug import privilages,resource_test
from .system import resources
from .file import upload
from .moral import MoralTransaction
from .student import studentTransaction
from .mit import mitTransaction
from .imageTask import ImageTaskTransaction
from .doc import docTransaction
from .gpa import gpa_manage
v1_router = APIRouter(prefix="/v1")
v1_router.include_router(login.token_router)
v1_router.include_router(privilages.debug)
v1_router.include_router(resources.system)
v1_router.include_router(upload.upload_route)
v1_router.include_router(resource_test.resourceTestRouter)
v1_router.include_router(MoralTransaction.moralTransactionRouter)
v1_router.include_router(studentTransaction.studentTransactionRouter)
v1_router.include_router(mitTransaction.mitTransactionRouter)
v1_router.include_router(ImageTaskTransaction.imageTaskTransactionRouter)
v1_router.include_router(docTransaction.docTransactionRouter)
v1_router.include_router(staticDirectory.staticDirectoryRouter)
v1_router.include_router(gpa_manage.gpa_router)
