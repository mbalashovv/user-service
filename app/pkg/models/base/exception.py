"""Base exception for API."""

from typing import Optional, Union

from fastapi import HTTPException
from starlette import status

__all__ = ["BaseAPIException"]


class BaseAPIException(HTTPException):
    """Base internal API Exception."""

    message: Optional[str] = "Base API Exception"
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, message: Optional[Union[str, Exception]] = None):
        if message is not None:
            self.message = message

        if isinstance(message, Exception):
            self.message = str(message)

        super().__init__(status_code=self.status_code, detail=self.message)

    @classmethod
    def generate_openapi(cls):
        return {
            cls.status_code: {
                "description": cls.message,
                "content": {
                    "application/json": {
                        "example": {
                            "message": cls.message,
                        },
                    },
                },
            },
        }
