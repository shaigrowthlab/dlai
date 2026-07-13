from app.ai.factory import get_ai_provider
from app.chat.memory import add_message, get_messages
from app.schemas.chat import ChatResponse

provider = get_ai_provider()


def process_chat(session_id: str, message: str) -> ChatResponse:
    message = message.strip()

    if not message:
        return ChatResponse(reply="Please enter a message.")

    add_message(session_id, "user", message)

    reply = provider.chat(get_messages(session_id))

    add_message(session_id, "assistant", reply)

    return ChatResponse(reply=reply)