"""Postgresql connector."""

from contextlib import asynccontextmanager

import aiopg
import pydantic
from aiopg import Connection

from .base import BaseConnector

__all__ = ["Postgresql"]


class Postgresql(BaseConnector):
    def __init__(
        self,
        username: str,
        password: pydantic.SecretStr,
        host: pydantic.PositiveInt,
        port: pydantic.PositiveInt,
        database_name: str,
    ):
        """Settings for create postgresql dsn."""

        self.pool = None
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database_name = database_name

    def get_dsn(self):
        """Description of ``BaseConnector.get_dsn``."""

        return (
            f"postgresql://"
            f"{self.username}:"
            f"{self.password.get_secret_value()}@"
            f"{self.host}:{self.port}/"
            f"{self.database_name}"
        )

    @asynccontextmanager
    async def get_connect(self) -> Connection:
        """Create pool of connectors to a Postgres database."""
        if self.pool is None:
            self.pool = aiopg.create_pool(dsn=self.get_dsn())

        async with self.pool as pool:
            async with pool.acquire() as conn:
                yield conn
