"""Module for testing read method of user repository."""

import pytest

from app.internal.repository.postgresql.users import UserRepository
from app.pkg import models
from app.pkg.models.exceptions.repository import EmptyResult


@pytest.mark.postgresql
@pytest.mark.slow
async def test_read(
    user_repository: UserRepository,
    user_generator,
):
    cmd = user_generator().migrate(models.CreateUserCommand)
    result = await user_repository.create(cmd=cmd)

    assert await user_repository.read(models.ReadUserQuery(id=result.id)) == result


@pytest.mark.postgresql
@pytest.mark.slow
async def test_read_not_found(
    user_repository: UserRepository,
    user_generator,
):
    cmd = user_generator().migrate(models.CreateUserCommand)
    result = await user_repository.create(cmd=cmd)

    with pytest.raises(EmptyResult):
        await user_repository.read(models.ReadUserQuery(id=result.id + 1))
