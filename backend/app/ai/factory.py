from app.ai.groq_provider import GroqProvider
from app.core.config import settings


def get_ai_provider():

    if settings.AI_PROVIDER == "groq":
        return GroqProvider()

    raise ValueError(
        f"Unsupported AI provider: {settings.AI_PROVIDER}"
    )