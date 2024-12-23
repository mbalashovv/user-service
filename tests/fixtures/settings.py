"""Settings for tests."""

import pytest

from app.pkg.settings import settings as _settings


@pytest.fixture()
async def settings():
    if _settings.POSTGRES_DATABASE_NAME.startswith("test_"):
        return _settings

    _settings.POSTGRES_DATABASE_NAME = f"test_{_settings.POSTGRES_DATABASE_NAME}"
    return _settings
