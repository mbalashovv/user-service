from fastapi import Security
from fastapi.security import APIKeyHeader
from pydantic import StrictStr

from app.pkg.logger import get_logger
from app.pkg.models.exceptions.validation import InvalidCredentials
from app.pkg.settings import settings

logger = get_logger(__name__)

X_API_KEY_HEADER = APIKeyHeader(name="X-ACCESS-TOKEN")

__all__ = ("validate_access_key",)


async def validate_access_key(
    api_key_header: StrictStr = Security(X_API_KEY_HEADER),
):
    if api_key_header != settings.API.X_API_TOKEN.get_secret_value():
        raise InvalidCredentials
