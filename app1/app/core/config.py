import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, EmailStr, HttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    PROJECT_NAME: str = "app1"

    RABBITMQURL:str="amqp://guest:guest@rabbitmq:5672"

    class Config:
        case_sensitive = True


# settings = Settings()
settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
