from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "DigitalLinks AI"
    APP_VERSION: str = "0.1.0"

    # Database
    DATABASE_URL: str = (
        "postgresql://dladmin:change_this_password@postgres:5432/digitallinks_ai"
    )

    # JWT Settings
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # AI Provider
    AI_PROVIDER: str = "groq"

    # Groq Settings
    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    # Embeddings
    EMBEDDING_PROVIDER: str = "openai"

    # Ollama Settings (optional - keep for future local testing)
    OLLAMA_URL: str = "http://host.docker.internal:11434"
    OLLAMA_MODEL: str = "qwen2.5:7b"
    OLLAMA_EMBEDDING_MODEL: str = "nomic-embed-text"

    # OpenAI Settings (optional)
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4.1-mini"

    # Qdrant Vector Database
    QDRANT_URL: str = "http://qdrant:6333"

    # Pydantic Settings Configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()