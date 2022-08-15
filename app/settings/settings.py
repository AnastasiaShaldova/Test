from dotenv import find_dotenv
import pydantic


class _Settings(pydantic.BaseSettings):
    class Config:
        env_file_encoding = "utf-8"


class Settings(_Settings):
    # Auth
    X_API_TOKEN: pydantic.SecretStr
    SIGNUP_API_TOKEN: pydantic.SecretStr

    # PostgresQL
    POSTGRES_HOSTNAME: str
    POSTGRES_DATABASE: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: pydantic.SecretStr
    POSTGRES_PORT: pydantic.PositiveInt

    # Secret key for JWT
    SECRET_KEY: pydantic.SecretStr

    # Server mode
    DEBUG: bool


def _get_settings() -> Settings:
    settings = Settings(_env_file=find_dotenv(".env"))
    return settings
