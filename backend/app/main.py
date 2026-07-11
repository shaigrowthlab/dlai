from fastapi import FastAPI

app = FastAPI(
    title="DigitalLinks AI API",
    description="White Label AI Chatbot Platform",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to DigitalLinks AI",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }