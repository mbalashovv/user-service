"""Configuration for pytest."""

import pytest

from app.configuration import __containers__
from app.pkg.connectors.postgresql import Postgresql

pytest_plugins = [
    "tests.fixtures.repository.postgresql.repositories",
    "tests.fixtures.repository.postgresql.postgresql",
    "tests.fixtures.repository.postgresql.inserters",
    "tests.fixtures.models.controller",
    "tests.fixtures.models.generators",
    "tests.fixtures.handlers.equals",
    "tests.fixtures.settings",
    # path to module with fixtures.
]

pytestmark = pytest.mark.anyio


def pytest_sessionstart(session):
    _ = session

    __containers__.set_environment(
        connectors=[Postgresql],
        pkg_name="tests",
        testing=True,
    )
