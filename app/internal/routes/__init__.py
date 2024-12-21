"""Global point for collected routers."""

from app.internal.routes.healthcheck import healthcheck_router
from app.internal.routes.users import users_router
from app.pkg.models.core.routes import Routes

__all__ = [
    "__routes__",
]


__routes__ = Routes(
    routers=(
        healthcheck_router,
        users_router,
    ),
)
