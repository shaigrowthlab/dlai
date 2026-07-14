from app.core.config import settings


def get_embedding_provider():

    provider = settings.EMBEDDING_PROVIDER.lower()

    if provider == "ollama":
        from app.knowledge.ollama_embeddings import (
            OllamaEmbeddingProvider
        )

        return OllamaEmbeddingProvider()

    if provider == "openai":
        from app.knowledge.openai_embeddings import (
            OpenAIEmbeddingProvider
        )

        return OpenAIEmbeddingProvider()

    raise ValueError(
        f"Unsupported embedding provider: {provider}"
    )