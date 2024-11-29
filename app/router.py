from fastapi import APIRouter, UploadFile, File, Form
from typing import Annotated

from services.dataset_service import dataset_service
from services.analysis_service import analysis_service
from schemas.dataset import ApiResponse

router = APIRouter()

def create_response(success: bool, message: str, data=None) -> ApiResponse:
    return ApiResponse(
        success=success,
        message=message,
        data=data
    )

@router.post("/generate", response_model=ApiResponse)
async def generate_dataset(
    file: Annotated[UploadFile, File()],
    count: Annotated[int, Form()] = 1
) -> ApiResponse:
    try:
        count = int(count)
        await dataset_service.generate_sample_images(file, count)
        return create_response(True, "이미지 생성 완료")
    except Exception as e:
        return create_response(False, str(e))

@router.post("/analyze", response_model=ApiResponse)    
async def analyze_image(
    images: Annotated[list[UploadFile], File()]
) -> ApiResponse:
    try:
        result = await analysis_service.analyze_images(images)
        return create_response(True, "이미지 분석 완료", result)
    except Exception as e:
        return create_response(False, str(e))
