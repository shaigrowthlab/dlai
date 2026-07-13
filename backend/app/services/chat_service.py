from app.ai.factory import get_ai_provider

from app.chat.memory import (
    add_message,
    get_messages,
)

from app.knowledge.rag_service import (
    RAGService
)

from app.schemas.chat import ChatResponse


provider = get_ai_provider()
rag = RAGService()


def process_chat(
    session_id: str,
    message: str
):

    add_message(
        session_id,
        "user",
        message
    )


    knowledge = rag.search(
        message
    )


    context = "\n\n".join(
        knowledge
    )


    messages = [
        {
            "role": "system",
            "content": (
                "Answer using the following "
                "DigitalLinks knowledge:\n\n"
                + context
            ),
        }
    ]


    messages.extend(
        get_messages(session_id)
    )


    reply = provider.chat(
        messages
    )


    add_message(
        session_id,
        "assistant",
        reply
    )


    return ChatResponse(
        reply=reply
    )