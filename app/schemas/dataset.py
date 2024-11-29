from pydantic import BaseModel
from typing import List, Optional

class ImageInfo(BaseModel):
    id: str
    width: int
    height: int
    url: str

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[List[ImageInfo]] = None
