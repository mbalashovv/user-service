"""PostgreSQL repository for users."""

from typing import List

from app.internal.repository.base import Repository
from app.internal.repository.postgresql.connection import get_connection
from app.internal.repository.postgresql.handlers.collect_response import (
    collect_response,
)
from app.pkg import models

__all__ = ["UserRepository"]


class UserRepository(Repository):
    """User repository implementation."""

    @collect_response
    async def create(self, cmd: models.CreateUserCommand) -> models.User:
        q = """
            insert into users(
                username, password
            ) values (
                %(username)s, %(password)s
            )
            returning id, username, password, created_at, deleted_at;
        """

        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()

    @collect_response
    async def read(self, query: models.ReadUserQuery) -> models.User:
        q = """
            select id, username, password, created_at, deleted_at from users
                where id = %(id)s and deleted_at is null;
        """
        async with get_connection() as cur:
            await cur.execute(q, query.to_dict())
            return await cur.fetchone()

    @collect_response
    async def read_all(self) -> List[models.User]:
        q = """
            select id, username, password, created_at, deleted_at from users
                where deleted_at is null;
        """
        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()

    @collect_response
    async def update(self, cmd: models.UpdateUserCommand) -> models.User:  # nosec
        q = f"""
            update users set {self.__build_update_statement(cmd=cmd)}
                where id = %(id)s and deleted_at is null
            returning id, username, password, created_at, deleted_at;
        """

        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()

    @collect_response
    async def delete(self, cmd: models.DeleteUserCommand) -> models.User:
        q = """
            update users set deleted_at = now()
                where id = %(id)s and deleted_at is null
            returning id, username, password, created_at, deleted_at;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()

    @staticmethod
    def __build_update_statement(cmd: models.UpdateUserCommand) -> str:
        update_statements = []

        if cmd.username is not None:
            update_statements.append(
                """
                    username = %(username)s
                """,
            )
        if cmd.password is not None:
            update_statements.append(
                """
                    password = %(password)s
                """,
            )

        return (", ".join(update_statements)) if update_statements else ""
