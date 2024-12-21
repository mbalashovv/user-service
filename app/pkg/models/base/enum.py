"""Base enum in api server."""

from enum import Enum

__all__ = ["BaseEnum"]


class BaseEnum(Enum):
    """Base enum model."""

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.value)
