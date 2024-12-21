"""All user exceptions."""

from fastapi import status

from app.pkg.models.base import BaseAPIException

__all__ = ["UserWasNotFound"]


class UserWasNotFound(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    message = "User was not found."
