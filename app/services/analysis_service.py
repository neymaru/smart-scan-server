from typing import Dict, List
from fastapi import UploadFile

class AnalysisService:
    async def analyze_images(self, images: List[UploadFile]) -> Dict:
        result = []
        for image in images:
            # 이미지 정보 수집
            file_info = {
                "filename": image.filename,
                "content_type": image.content_type,
                "size": len(await image.read())
            }
            result.append(file_info)
            
            # 파일 포인터 리셋
            await image.seek(0)
            
        return {"analyzed_images": result}

analysis_service = AnalysisService() 
