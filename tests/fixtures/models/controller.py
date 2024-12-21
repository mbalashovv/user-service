"""Model controller fixtures."""

import typing
from typing import Any, Callable, Coroutine

import pydantic
import pytest
from jsf import JSF

from app.pkg.models.base import Model


@pytest.fixture()
def create_model() -> Callable[..., Coroutine[Any, Any, Model]]:
    """Create model with random data."""

    async def _create_model(model: typing.Type[Model], **kwargs) -> Model:
        """Create model with random data."""

        mock_model = JSF(model.schema()).generate()

        if kwargs:
            mock_model.update(kwargs)

        return pydantic.parse_obj_as(model, mock_model)

    return _create_model
