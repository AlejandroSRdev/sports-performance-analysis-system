from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    OPENAI_API_KEY: str = ""
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8080
    LOG_LEVEL: str = "INFO"


settings = Settings()
