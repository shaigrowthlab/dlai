from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "DigitalLinks AI"
    APP_VERSION: str = "0.1.0"

    DATABASE_URL: str = (
        "postgresql://dladmin:change_this_password@postgres:5432/digitallinks_ai"
    )

    # JWT Settings
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # AI Settings
    AI_PROVIDER: str = "ollama"
    OLLAMA_URL: str = "http://host.docker.internal:11434"
    OLLAMA_MODEL: str = "qwen2.5:7b"
    OLLAMA_EMBEDDING_MODEL: str = "nomic-embed-text"


    # OpenAI Settings
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-5.5"

    # Qdrant
    QDRANT_URL: str = "http://qdrant:6333"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()