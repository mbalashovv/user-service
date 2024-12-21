"""Module for testing read_all method of user repository."""

import pytest

from app.internal.repository.postgresql.users import UserRepository


@pytest.mark.postgresql
@pytest.mark.slow
async def test_read_all(
    user_repository: UserRepository,
    user_inserter,
):
    result, _ = await user_inserter()

    assert await user_repository.read_all() == [result]


# @pytest.mark.postgresql
# @pytest.mark.slow
# async def test_read_all_empty(
#     user_repository: UserRepository,
# ):
#     result = await user_repository.read_all()
#     assert all([user.deleted_at for user in result]) is True
