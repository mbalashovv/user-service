"""All connectors in declarative container."""

from dependency_injector import containers, providers

from app.pkg.connectors.postgresql import Postgresql
from app.pkg.settings import settings

__all__ = ["Connectors", "Postgresql"]


class Connectors(containers.DeclarativeContainer):
    """Declarative container with all connectors."""

    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    #: Postgresql: Connector to postgresql.
    postgresql = providers.Factory(
        Postgresql,
        username=configuration.POSTGRESQL.POSTGRES_USER,
        password=configuration.POSTGRESQL.POSTGRES_PASSWORD,
        host=configuration.POSTGRESQL.POSTGRES_HOST,
        port=configuration.POSTGRESQL.POSTGRES_PORT,
        database_name=configuration.POSTGRESQL.POSTGRES_DATABASE_NAME,
    )
