from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine

# Import models so SQLAlchemy registers them
import app.models

from app.routers.user import router as user_router
from app.routers.auth import router as auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DigitalLinks AI API",
    description="White Label AI Chatbot Platform",
    version="0.1.0",
)

# Register routers
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to DigitalLinks AI",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected",
    }