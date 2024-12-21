from fastapi import APIRouter, status

from app.pkg import models

healthcheck_router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
)


@healthcheck_router.get(
    "",
    status_code=status.HTTP_200_OK,
    description="Healthcheck of the API service.",
)
async def get_healthcheck():
    return models.HEALTHCHECK_STATUS
