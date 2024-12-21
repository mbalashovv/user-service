"""Module for testing update method of user repository."""

from datetime import datetime

import pytest

from app.internal.repository.postgresql.users import UserRepository
from app.pkg import models
from app.pkg.models.exceptions.repository import EmptyResult


@pytest.mark.postgresql
@pytest.mark.slow
async def test_delete(
    user_repository: UserRepository,
    user_inserter,
):
    result, _ = await user_inserter()
    cmd = result.migrate(model=models.DeleteUserCommand)

    await user_repository.delete(cmd=cmd)

    user = await user_repository.read(
        query=models.ReadUserQuery(id=result.id),
    )
    assert isinstance(user.deleted_at, datetime)


@pytest.mark.postgresql
async def test_not_found(
    user_repository: UserRepository,
    create_model,
):
    cmd = await create_model(models.DeleteUserCommand)

    with pytest.raises(EmptyResult):
        await user_repository.delete(cmd=cmd)
