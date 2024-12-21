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


class PostgreSQL(_Settings):
    """PostgreSQL settings."""

    #: str: Postgresql host.
    POSTGRESQL_HOST: str
    #: PositiveInt: positive int (x > 0) port of postgresql.
    POSTGRESQL_PORT: PositiveInt
    #: str: Postgresql user.
    POSTGRESQL_USER: str
    #: SecretStr: Postgresql password.
    POSTGRESQL_PASSWORD: SecretStr
    #: str: Postgresql database name.
    POSTGRESQL_DATABASE_NAME: str


class Logging(_Settings):
    """Logging settings."""

    LOGGING_LEVEL: LoggerLevel = LoggerLevel.DEBUG
    FOLDER_PATH: pathlib.Path = pathlib.Path("./src/logs")

    # pylint: disable=unused-private-member, no-self-argument
    @validator("FOLDER_PATH")
    def __create_dir_if_not_exist(
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
    API_INSTANCE_APP_NAME: str = "user_api"
    #: bool: Debug mode flag
    API_DEBUG_MODE: Optional[bool] = False

    # --- SECURITY SETTINGS ---
    #: SecretStr: Secret key for token auth.
    API_X_API_TOKEN: SecretStr = SecretStr("secret")


class Settings(APIServer, PostgreSQL, Logging):
    """All server settings."""


@lru_cache
def get_settings(env_file: str = ".env.example") -> Settings:
    """Create settings instance."""

    return Settings(_env_file=find_dotenv(env_file))
