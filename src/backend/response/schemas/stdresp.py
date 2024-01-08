from pydantic import BaseModel
from typing import Optional, List, Any


class StdResp(BaseModel):
    code: int = 200
    data: Optional[str] = "success"
    msg: Optional[str] = None
