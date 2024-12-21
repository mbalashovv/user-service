"""All defined repositories should be there."""

from dependency_injector import containers, providers

from app.internal.repository import postgresql

__all__ = ["Repositories"]


class Repositories(containers.DeclarativeContainer):
    """Container for repositories."""

    postgresql = providers.Container(postgresql.Repository)
