from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router as api_router

app = FastAPI(
    title="Smart Scan API",
    description="API for generating and analyzing essay answer sheets"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 클라이언트 주소 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(api_router)
