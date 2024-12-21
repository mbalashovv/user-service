"""Models for users."""

import datetime
from typing import Optional

from pydantic import Field, PositiveInt

from app.pkg.models.base import BaseModel

__all__ = [
    "User",
    "CreateUserCommand",
    "ReadUserQuery",
    "UpdateUserCommandPayload",
    "UpdateUserCommand",
    "DeleteUserCommand",
]


class UserFields:
    """Fields for user models."""

    id = Field(
        description="Users's id as int",
        example="1",
    )
    username = Field(
        description="User's name",
        example="Steve",
    )
    password = Field(
        description="User's passowrd",
        example="123456",
    )
    created_at = Field(
        description="Date of user registration",
        example="2024-12-01 15:30:00.100000",
    )
    deleted_at = Field(
        default=None,
        description="Date of user deletion",
        example="2024-12-01 15:30:00.100000",
    )


class User(BaseModel):
    """Base user model."""

    id: PositiveInt = UserFields.id
    username: str = UserFields.username
    password: str = UserFields.password
    created_at: datetime.datetime = UserFields.created_at
    deleted_at: datetime.datetime = UserFields.deleted_at


# Model queries


class ReadUserQuery(BaseModel):
    id: PositiveInt = UserFields.id


# Model commands


class CreateUserCommand(BaseModel):
    username: str = UserFields.username
    password: str = UserFields.password


class UpdateUserCommandPayload(BaseModel):
    username: Optional[str] = UserFields.username
    password: Optional[str] = UserFields.password


class UpdateUserCommand(UpdateUserCommandPayload):
    id: PositiveInt


class DeleteUserCommand(BaseModel):
    id: PositiveInt = UserFields.id
