from fastapi import APIRouter, Depends

from app.schemas.chat import ChatRequest, ChatResponse
from app.security.api_key import verify_api_key
from app.services.chat_service import process_chat

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    _: bool = Depends(verify_api_key),
):
    return process_chat(
        request.session_id,
        request.message,
    )