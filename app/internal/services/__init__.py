"""Service layer."""

from dependency_injector import containers, providers

from app.internal.repository import Repositories, postgresql
from app.internal.services.users import UserService


class Services(containers.DeclarativeContainer):
    """Containers with services."""

    repositories: postgresql.Repository = providers.Container(
        Repositories.postgresql,
    )

    users_service = providers.Factory(
        UserService,
        user_repository=repositories.users,
    )
