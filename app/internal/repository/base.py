"""Abstract repository interface."""

from abc import ABC
from typing import List, TypeVar

from app.pkg.models.base import Model

__all__ = ["Repository", "BaseRepository"]

BaseRepository = TypeVar("BaseRepository", bound="Repository")


class Repository(ABC):
    """Base repository interface."""

    async def create(self, cmd: Model) -> Model:
        """Create model."""

        raise NotImplementedError

    async def read(self, query: Model) -> Model:
        """Read model."""

        raise NotImplementedError

    async def read_all(self) -> List[Model]:
        """Read all rows."""

        raise NotImplementedError

    async def update(self, cmd: Model) -> Model:
        """Update model."""

        raise NotImplementedError

    async def delete(self, cmd: Model) -> Model:
        """Delete model."""

        raise NotImplementedError
