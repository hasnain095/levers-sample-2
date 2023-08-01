import os
import secrets

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    PROJECT_NAME: str = "app1"

    RABBITMQURL: str = os.getenv(
        "RABBITMQURL", "amqp://guest:guest@rabbitmq:5672")

    class Config:
        case_sensitive = True


settings = Settings()
