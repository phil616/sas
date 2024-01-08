from fastapi.exceptions import HTTPException
from starlette import status
from typing import Optional, Any


def E401(details: Optional[Any] = None, headers: Optional[dict[str, Any]] = None) -> None:
    # TODO log here
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=details,
        headers=headers
    )


def E404(details: Optional[Any] = None, headers: Optional[dict[str, Any]] = None):
    # TODO log here
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=details,
        headers=headers
    )


def E500(details: Optional[Any] = None):
    # TODO log here
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=details,
    )
