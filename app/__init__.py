"""Main factory builder of FastAPI server."""

from fastapi import FastAPI

from app.configuration import __containers__
from app.configuration.server import Server
from app.internal.pkg.middlewares.validation import validate_access_key
from app.pkg.settings import settings


def create_app() -> FastAPI:
    """Create FastAPI application."""

    fastapi_kwargs = {}
    if not settings.API.DEBUG_MODE:
        fastapi_kwargs["docs_url"] = None
        fastapi_kwargs["redoc_url"] = None
        fastapi_kwargs["openapi_url"] = None

    app = FastAPI(
        **fastapi_kwargs,
    )

    __containers__.wire_packages(app=app)
    return Server(app).get_app()
