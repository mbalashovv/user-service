"""Server configuration."""


from fastapi import FastAPI

from app.internal.pkg.middlewares.handle_http_exceptions import (
    handle_api_exceptions,
)
from app.internal.routes import __routes__
from app.pkg.models.base import BaseAPIException
from app.pkg.models.types.fastapi import FastAPITypes

__all__ = ["Server"]


class Server:
    """Register all requirements for the correct work of server instance."""

    __app: FastAPI

    def __init__(self, app: FastAPI):
        """Initialize server instance.

        Register all requirements for the correct work of server
        instance.
        """

        self.__app = app
        self._register_routes(app)
        self._register_http_exceptions(app)

    def get_app(self) -> FastAPI:
        """Getter of the current application instance."""

        return self.__app

    @staticmethod
    def _register_routes(app: FastAPITypes.instance) -> None:
        """Include routers."""

        __routes__.register_routes(app)

    @staticmethod
    def _register_http_exceptions(app: FastAPITypes.instance) -> None:
        """Register http exceptions."""

        app.add_exception_handler(BaseAPIException, handle_api_exceptions)
