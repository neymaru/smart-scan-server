from typing import List, Dict
from fastapi import UploadFile

class DatasetService:
    async def generate_sample_images(self, count: int) -> List[Dict]:
        pass


class AnalysisService:
    async def analyze_image(self, image: UploadFile) -> Dict:
        pass


dataset_service = DatasetService()
analysis_service = AnalysisService()
