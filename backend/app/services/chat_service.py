from pathlib import Path
import time

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


def load_system_prompt():
    prompt_file = (
        Path(__file__).parent.parent
        / "prompts"
        / "sales_assistant.txt"
    )

    return prompt_file.read_text(encoding="utf-8")


def process_chat(
    session_id: str,
    message: str,
):
    start = time.perf_counter()

    add_message(
        session_id,
        "user",
        message,
    )

    t1 = time.perf_counter()

    knowledge = rag.search(message)

    t2 = time.perf_counter()

    context = "\n\n".join(knowledge)

    system_prompt = load_system_prompt()

    messages = [
        {
            "role": "system",
            "content": (
                system_prompt
                + "\n\nRelevant DigitalLinks Knowledge:\n\n"
                + context
            ),
        }
    ]

    messages.extend(
        get_messages(session_id)
    )

    reply = provider.chat(messages)

    t3 = time.perf_counter()

    add_message(
        session_id,
        "assistant",
        reply,
    )

    end = time.perf_counter()

    print("=" * 50)
    print(f"Memory      : {(t1 - start):.3f} sec")
    print(f"RAG Search  : {(t2 - t1):.3f} sec")
    print(f"AI Response : {(t3 - t2):.3f} sec")
    print(f"Total Time  : {(end - start):.3f} sec")
    print("=" * 50)

    return ChatResponse(
        reply=reply
    )