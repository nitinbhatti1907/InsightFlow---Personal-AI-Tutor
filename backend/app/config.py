from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "Data Analysis with Python Learning Assistant API"
    app_version: str = "1.0.0"
    database_url: str = f"sqlite:///{BASE_DIR / 'learning_assistant.db'}"
    frontend_origin: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
