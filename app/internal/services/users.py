"""Service for manage users."""

from typing import List

from app.internal.repository.postgresql.users import UserRepository
from app.pkg.models.exceptions.repository import EmptyResult
from app.pkg.models.exceptions.users import UserWasNotFound
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
    ) -> models.UserResponse:
        return await self.__user_repository.create(cmd=cmd)

    async def read_user(
        self,
        query: models.ReadUserQuery,
    ) -> models.UserResponse:
        try:
            return await self.__user_repository.read(query=query)
        except EmptyResult as e:
            raise UserWasNotFound from e

    async def read_all_users(self) -> List[models.UserResponse]:
        try:
            return await self.__user_repository.read_all()
        except EmptyResult:
            return []

    async def update_user(
        self,
        cmd: models.UpdateUserCommand,
    ) -> models.UserResponse:
        try:
            return await self.__user_repository.update(cmd=cmd)
        except EmptyResult as e:
            raise UserWasNotFound from e

    async def delete_user(
        self,
        cmd: models.DeleteUserCommand,
    ) -> models.UserResponse:
        try:
            return await self.__user_repository.delete(cmd=cmd)
        except EmptyResult as e:
            raise UserWasNotFound from e
