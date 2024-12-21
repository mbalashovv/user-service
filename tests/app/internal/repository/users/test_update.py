"""Module for testing update method of user repository."""

import pytest

from app.internal.repository.postgresql.users import UserRepository
from app.pkg import models


@pytest.mark.postgresql
@pytest.mark.slow
async def test_update(
    user_repository: UserRepository,
    user_generator,
):
    cmd = user_generator().migrate(models.CreateUserCommand)
    created_user = await user_repository.create(cmd=cmd)

    await user_repository.update(
        cmd=models.UpdateUserCommand(
            id=created_user.id,
            username=created_user.username + "a",
        ),
    )

    updated_user = await user_repository.read(
        query=models.ReadUserQuery(id=created_user.id),
    )

    assert updated_user != created_user
