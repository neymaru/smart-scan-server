from typing import List, Dict
from fastapi import UploadFile
import random
import os
import cv2
import numpy as np

class DatasetService:
    def __init__(self):
        self.save_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'storage', 'samples')
        
        storage_dir = os.path.dirname(self.save_dir)
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
            
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        
        self.chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    def generate_random_text(self, length: int) -> str:
        """랜덤 텍스트 생성"""
        return ''.join(random.choice(self.chars) for _ in range(length))

    def add_random_texts(self, image):
        """이미지에 랜덤 개수의 랜덤 텍스트 추가"""
        height, width = image.shape[:2]
        
        # 랜덤하게 1~10개의 텍스트 추가
        text_count = random.randint(1, 10)
        text_infos = []
        
        for _ in range(text_count):
            # 랜덤 위치 선택
            x = random.randint(0, width - 200)  # 텍스트 공간 확보
            y = random.randint(50, height - 50)  # 여백 확보
            
            # 랜덤 텍스트 생성 (5~15자)
            text = self.generate_random_text(random.randint(5, 15))
            
            # 랜덤 폰트 크기
            font_scale = random.uniform(0.5, 2.0)
            
            # 랜덤 색상 (검정~회색)
            color = random.randint(0, 100)
            
            # 텍스트 추가
            cv2.putText(
                image, 
                text,
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                font_scale,
                (color, color, color),
                2
            )
            
            text_infos.append({
                "text": text,
                "position": (x, y),
                "font_size": font_scale,
                "color": color
            })
        
        return image, text_infos

    async def generate_sample_images(self, file: UploadFile, count: int) -> List[Dict]:
        try:
            file_bytes = await file.read()
            nparr = np.frombuffer(file_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if image is None:
                raise Exception("Failed to decode image")
            
            for i in range(count):
                current_image = image.copy()
                current_image, text_infos = self.add_random_texts(current_image)
                
                direction = random.choice([1, -1])
                angle = random.uniform(0.1, 0.5) * direction
                
                height, width = current_image.shape[:2]
                center = (width/2, height/2)
                rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
                rotated_image = cv2.warpAffine(current_image, rotation_matrix, (width, height))
                
                new_filename = f"sample_{str(i+1).zfill(4)}.jpg"
                save_path = os.path.join(self.save_dir, new_filename)
                
                success = cv2.imwrite(save_path, rotated_image)
                if not success:
                    raise Exception(f"Failed to save image: {save_path}")
                
        except Exception as e:
            print(f"에러 발생: {str(e)}")
            raise e
        print('끝!')

dataset_service = DatasetService()
