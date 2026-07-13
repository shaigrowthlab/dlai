import httpx

from app.ai.provider import AIProvider
from app.core.config import settings


class OllamaProvider(AIProvider):

    def chat(self, messages: list[dict]) -> str:
        url = f"{settings.OLLAMA_URL}/api/chat"

        payload = {
            "model": settings.OLLAMA_MODEL,
            "messages": messages,
            "stream": False,
        }

        response = httpx.post(
            url,
            json=payload,
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]