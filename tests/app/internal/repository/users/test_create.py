"""Module for testing create method of user repository."""

import pytest

from app.internal.repository.postgresql.users import UserRepository
from app.pkg import models


@pytest.mark.postgresql
async def test_create(
    user_repository: UserRepository,
    user_generator,
):
    cmd = user_generator().migrate(models.CreateUserCommand)
    result = await user_repository.create(cmd=cmd)
    assert result == cmd.migrate(
        model=models.User,
        extra_fields={"id": result.id, "created_at": result.created_at},
    )
