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
        username=configuration.POSTGRESQL_USER,
        password=configuration.POSTGRESQL_PASSWORD,
        host=configuration.POSTGRESQL_HOST,
        port=configuration.POSTGRESQL_PORT,
        database_name=configuration.POSTGRESQL_DATABASE_NAME,
    )
