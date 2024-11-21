from typing import Dict
from fastapi import UploadFile

class AnalysisService:
    async def analyze_image(self, image: UploadFile) -> Dict:
        pass

analysis_service = AnalysisService() 
