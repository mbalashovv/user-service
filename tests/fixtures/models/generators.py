"""Generators for models."""

from typing import Any, Callable, Type

import pydantic
import pytest
from jsf import JSF

from app.pkg import models
from app.pkg.models.base import Model


def __generator(model: Type[Model], **kwargs) -> Callable[..., Model]:
    mock = JSF(model.schema())

    def generate() -> Any:
        mock_generate = mock.generate()
        mock_generate.update(kwargs)
        return pydantic.parse_obj_as(model, mock_generate)

    return generate()


@pytest.fixture()
def user_generator() -> Callable[[], Any]:
    return lambda **kwargs: __generator(models.User, **kwargs)
