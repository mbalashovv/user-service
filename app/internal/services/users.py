"""Service for manage users."""

from typing import List

from app.internal.repository.postgresql.users import UserRepository
from app.pkg import models

__all__ = ["UserService"]


class UserService:
    """Service for manage users."""

    __user_repository: UserRepository

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def create_user(
        self,
        cmd: models.CreateUserCommand,
    ) -> models.User:
        return await self.__user_repository.create(cmd=cmd)

    async def read_user(
        self,
        query: models.ReadUserQuery,
    ) -> models.User:
        return await self.__user_repository.read(query=query)

    async def read_all_users(self) -> List[models.User]:
        return await self.__user_repository.read_all()

    async def update_user(
        self,
        cmd: models.UpdateUserCommand,
    ) -> models.User:
        return await self.__user_repository.update(cmd=cmd)

    async def delete_user(
        self,
        cmd: models.DeleteUserCommand,
    ) -> models.User:
        return await self.__user_repository.delete(cmd=cmd)
