from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
async def generate_dataset():
    pass

@router.post("/analyze")
async def analyze_image():
    pass
