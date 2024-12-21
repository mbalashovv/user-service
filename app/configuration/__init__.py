"""Server configuration."""

from app.internal.repository.postgresql import Repository
from app.internal.services import Services
from app.pkg.connectors import Connectors
from app.pkg.models.core import Container, Containers

__all__ = ["__containers__"]


__containers__ = Containers(
    pkg_name=__name__,
    containers=[
        Container(container=Services),
        Container(container=Connectors),
        Container(container=Repository),
    ],
)
