from fastapi import FastAPI
from router import router as api_router

app = FastAPI(
    title="Smart Scan API",
    description="API for generating and analyzing essay answer sheets"
)

app.include_router(api_router)
