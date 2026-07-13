from openai import OpenAI

from app.ai.provider import AIProvider
from app.core.config import settings


class OpenAIProvider(AIProvider):

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def chat(self, message: str) -> str:
        response = self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=message,
        )

        return response.output_text