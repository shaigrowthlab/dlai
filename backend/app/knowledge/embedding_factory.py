from app.core.config import settings


def get_embedding_provider():

    provider = settings.AI_PROVIDER.lower()

    if provider == "ollama":
        from app.knowledge.ollama_embeddings import (
            OllamaEmbeddingProvider
        )

        return OllamaEmbeddingProvider()

    raise ValueError(
        f"Unsupported embedding provider: {provider}"
    )