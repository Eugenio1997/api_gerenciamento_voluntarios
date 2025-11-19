from fastapi import FastAPI
from app.routers.volunteer_router import router as volunteer_router

app = FastAPI(
    title="API de Gerenciamento de Voluntários",
    version="1.0.0"
)

app.include_router(volunteer_router)