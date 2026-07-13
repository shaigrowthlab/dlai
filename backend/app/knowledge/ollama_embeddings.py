import httpx

from app.knowledge.embedding_provider import EmbeddingProvider
from app.core.config import settings


class OllamaEmbeddingProvider(EmbeddingProvider):

    def embed(self, text: str) -> list[float]:
        url = f"{settings.OLLAMA_URL}/api/embeddings"

        payload = {
            "model": settings.OLLAMA_EMBEDDING_MODEL,
            "prompt": text,
        }

        response = httpx.post(
            url,
            json=payload,
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return data["embedding"]