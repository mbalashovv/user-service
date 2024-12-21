from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.internal.pkg.middlewares.validation import validate_access_key
from app.internal.services import Services
from app.internal.services.users import UserService
from app.pkg import models

users_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@users_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    description="Create new user.",
    dependencies=[
        Depends(validate_access_key),
    ],
    response_model=models.User,
)
@inject
async def create_user(
    cmd: models.CreateUserCommand,
    users_service: UserService = Depends(
        Provide[Services.users_service],
    ),
):
    return await users_service.create_user(cmd=cmd)


@users_router.get(
    "/{user_id:int}",
    status_code=status.HTTP_200_OK,
    description="Get an user.",
    dependencies=[
        Depends(validate_access_key),
    ],
    response_model=models.User,
)
@inject
async def read_user(
    user_id: int,
    users_service: UserService = Depends(
        Provide[Services.users_service],
    ),
):
    return await users_service.read_user(
        query=models.ReadUserQuery(id=user_id),
    )


@users_router.get(
    "",
    status_code=status.HTTP_200_OK,
    description="Get all users.",
    dependencies=[
        Depends(validate_access_key),
    ],
    response_model=List[models.User],
)
@inject
async def read_all_users(
    users_service: UserService = Depends(
        Provide[Services.users_service],
    ),
):
    return await users_service.read_all_users()


@users_router.patch(
    "/{user_id:int}",
    status_code=status.HTTP_200_OK,
    description="Update an user.",
    dependencies=[
        Depends(validate_access_key),
    ],
    response_model=models.User,
)
@inject
async def update_user(
    user_id: str,
    cmd: models.UpdateUserCommand,
    users_service: UserService = Depends(
        Provide[Services.users_service],
    ),
):
    cmd.id = user_id
    return await users_service.update_user(
        cmd=cmd,
    )


@users_router.delete(
    "/{user_id:int}",
    status_code=status.HTTP_200_OK,
    description="Delete an user.",
    dependencies=[
        Depends(validate_access_key),
    ],
    response_model=models.User,
)
@inject
async def delete_user(
    user_id: str,
    users_service: UserService = Depends(
        Provide[Services.users_service],
    ),
):
    return await users_service.delete_user(
        cmd=models.DeleteUserCommand(
            id=user_id,
        ),
    )
