from groq import Groq

from app.core.config import settings


class GroqProvider:
    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        # Fast, excellent model for chatbots
        self.model = "llama-3.3-70b-versatile"

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.3,
            max_tokens=600,
        )

        return response.choices[0].message.content