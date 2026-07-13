from app.core.config import settings


def get_ai_provider():
    provider = settings.AI_PROVIDER.lower()

    if provider == "ollama":
        from app.ai.ollama_provider import OllamaProvider
        return OllamaProvider()

    if provider == "openai":
        from app.ai.openai_provider import OpenAIProvider
        return OpenAIProvider()

    raise ValueError(f"Unsupported AI provider: {provider}")