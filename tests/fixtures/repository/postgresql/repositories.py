"""All fixtures for postgresql repositories."""

import pytest

from app.internal.repository.postgresql.users import UserRepository


@pytest.fixture()
async def user_repository() -> UserRepository:
    return UserRepository()
