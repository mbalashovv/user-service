from dependency_injector import containers, providers

from .users import UserRepository

__all__ = ["Repository"]


class Repository(containers.DeclarativeContainer):
    users = providers.Factory(UserRepository)
