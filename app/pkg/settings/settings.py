"""Module for load settings form `.env` or if server running with parameter
`dev` from `.env.dev`"""

import pathlib
from functools import lru_cache
from typing import Optional

from dotenv import find_dotenv
from pydantic import BaseSettings, validator
from pydantic.types import PositiveInt, SecretStr

from app.pkg.models.core.logger import LoggerLevel

__all__ = ["Settings", "get_settings"]


class _Settings(BaseSettings):
    """Base settings for all settings."""

    class Config:
        """Configuration of settings."""

        #: str: env file encoding.
        env_file_encoding = "utf-8"
        #: str: allow custom fields in model.
        arbitrary_types_allowed = True
        #: bool: case-sensitive for env variables.
        case_sensitive = True
        #: str: delimiter for nested env variables.
        env_nested_delimiter = "__"


class PostgreSQL(_Settings):
    """PostgreSQL settings."""

    #: str: Postgresql host.
    POSTGRES_HOST: str
    #: PositiveInt: positive int (x > 0) port of postgresql.
    POSTGRES_PORT: PositiveInt
    #: str: Postgresql user.
    POSTGRES_USER: str
    #: SecretStr: Postgresql password.
    POSTGRES_PASSWORD: SecretStr
    #: str: Postgresql database name.
    POSTGRES_DATABASE_NAME: str


class Logging(_Settings):
    """Logging settings."""

    LEVEL: LoggerLevel = LoggerLevel.DEBUG
    FOLDER_PATH: pathlib.Path = pathlib.Path("./src/logs")

    @validator("FOLDER_PATH")
    def __create_dir_if_not_exist(  # pylint: disable=unused-private-member, no-self-argument
        cls,
        v: pathlib.Path,
    ):
        """Create directory if not exist."""

        if not v.exists():
            v.mkdir(exist_ok=True, parents=True)
        return v


class APIServer(_Settings):
    """API settings."""

    # --- API SETTINGS ---
    #: str: Name of API service
    INSTANCE_APP_NAME: str = "user_api"
    #: str: API host.
    HOST: str = "localhost"
    #: PositiveInt: positive int (x > 0) port of API.
    PORT: PositiveInt = 8000
    #: bool: Debug mode flag
    DEBUG_MODE: Optional[bool] = False

    # --- SECURITY SETTINGS ---
    #: SecretStr: Secret key for token auth.
    X_API_TOKEN: SecretStr = SecretStr("secret")

    # --- OTHER SETTINGS ---
    #: Logging: Logging settings.
    LOGGER: Logging


class Settings(_Settings):
    """Server settings."""

    #: APIServer: API settings. Contains all settings for API.
    API: APIServer

    #: PostgreSQL: Postgresql settings.
    POSTGRESQL: PostgreSQL


@lru_cache
def get_settings(env_file: str = ".env") -> Settings:
    """Create settings instance."""

    a = Settings(_env_file=find_dotenv(env_file))
    return a
