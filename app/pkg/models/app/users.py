"""Models for users."""

import datetime

from typing import Optional
from pydantic import Field, StrictStr

from app.pkg.models.base import BaseModel

__all__ = [
    "User",
    "UserResponse",
    "CreateUserCommand",
    "ReadUserQuery",
    "UpdateUserCommandPayload",
    "UpdateUserCommand",
    "DeleteUserCommand",
]


class UserFields:
    """Fields for user models."""

    id: StrictStr = Field(
        description="Users's id as int",
        example="9821d845-faed-4316-b68f-ee2ea5e79821",
    )
    username: StrictStr = Field(
        description="User's name",
        example="Steve",
    )
    password: StrictStr = Field(
        description="User's passowrd",
        example="123456",
    )
    created_at: datetime.datetime = Field(
        description="Date of user registration",
        example="2024-12-01 15:30:00.100000",
    )
    deleted_at: datetime.datetime = Field(
        default=None,
        description="Date of user deletion",
        example="2024-12-01 15:30:00.100000",
    )


class User(BaseModel):
    """Base user model."""

    id: StrictStr = UserFields.id
    username: StrictStr = UserFields.username
    password: StrictStr = UserFields.password
    created_at: datetime.datetime = UserFields.created_at
    deleted_at: datetime.datetime = UserFields.deleted_at


# Used to be sent to WEB
class UserResponse(BaseModel):
    id: StrictStr = UserFields.id
    username: StrictStr = UserFields.username
    created_at: datetime.datetime = UserFields.created_at


# Model queries


class ReadUserQuery(BaseModel):
    id: StrictStr = UserFields.id


# Model commands


class CreateUserCommand(BaseModel):
    username: StrictStr = UserFields.username
    password: StrictStr = UserFields.password


class UpdateUserCommandPayload(BaseModel):
    username: Optional[StrictStr] = UserFields.username
    password: Optional[StrictStr] = UserFields.password


class UpdateUserCommand(UpdateUserCommandPayload):
    id: StrictStr = UserFields.id


class DeleteUserCommand(BaseModel):
    id: StrictStr = UserFields.id
