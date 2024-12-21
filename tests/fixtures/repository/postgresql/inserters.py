"""Inserters for PostgreSQL repository."""

from typing import Type

import pytest

from app.internal.repository.base import Repository
from app.pkg import models
from app.pkg.models.base import Model


async def __inserter(
    repository: Repository,
    generator,
    cmd_model: Type[Model],
    **kwargs,
) -> tuple[Model, Model]:
    """Insert generic model to database."""

    cmd = generator(**kwargs).migrate(model=cmd_model)

    return await repository.create(cmd=cmd), cmd


@pytest.fixture()
async def user_inserter(user_repository, user_generator):
    """Insert users into database."""

    return lambda **kwargs: __inserter(
        repository=user_repository,
        generator=user_generator,
        cmd_model=models.User,
        **kwargs,
    )
