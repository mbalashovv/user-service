"""Base model for all models."""

from __future__ import annotations

import time
from datetime import date, datetime
from typing import Any, Dict, List, Tuple, TypeVar

import pydantic
from jsf import JSF

__all__ = ["BaseModel", "Model"]

Model = TypeVar("Model", bound="BaseModel")
_T = TypeVar("_T")


class BaseModel(pydantic.BaseModel):
    """Base model for all models."""

    def to_dict(
        self,
        show_secrets: bool = False,
        values: dict[Any, Any] = None,
        **kwargs,
    ) -> dict[Any, Any]:
        """Make transfer model to Dict object."""

        values = self.dict(**kwargs).items() if not values else values.items()
        r = {}
        for k, v in values:
            v = self.__cast_values(v=v, show_secrets=show_secrets)
            r[k] = v
        return r

    def delete_attribute(self, attr: pydantic.StrictStr) -> BaseModel:
        """Delete `attr` field from model."""

        delattr(self, attr)
        return self

    def __cast_values(self, v: _T, show_secrets: bool, **kwargs) -> _T:
        """Cast value for dict object."""

        if isinstance(v, (List, Tuple)):
            return [
                self.__cast_values(v=ve, show_secrets=show_secrets, **kwargs)
                for ve in v
            ]

        elif isinstance(v, (pydantic.SecretBytes, pydantic.SecretStr)):
            return self.__cast_secret(v=v, show_secrets=show_secrets)

        elif isinstance(v, Dict) and v:
            return self.to_dict(show_secrets=show_secrets, values=v, **kwargs)

        elif isinstance(v, datetime):
            return v.timestamp()

        return v

    @staticmethod
    def __cast_secret(v, show_secrets: bool) -> pydantic.StrictStr:
        """Cast secret value to str."""

        if isinstance(v, pydantic.SecretBytes):
            return v.get_secret_value().decode() if show_secrets else str(v)
        elif isinstance(v, pydantic.SecretStr):
            return v.get_secret_value() if show_secrets else str(v)

    def migrate(
        self,
        model: type[BaseModel],
        random_fill: bool = False,
        match_keys: dict[str, str] | None = None,
        extra_fields: dict[str, Any] | None = None,
    ) -> Model:
        """Migrate one model to another ignoring missmatch."""

        self_dict_model = self.to_dict(show_secrets=True)

        if not match_keys:
            match_keys = {}
        if not extra_fields:
            extra_fields = {}

        for key, value in match_keys.items():
            self_dict_model[key] = self_dict_model.pop(value)

        for key, value in extra_fields.items():
            self_dict_model[key] = value

        if not random_fill:
            return pydantic.parse_obj_as(model, self_dict_model)

        faker = JSF(model.schema()).generate()
        faker.update(self_dict_model)
        return pydantic.parse_obj_as(model, faker)

    class Config:
        """Pydantic config class."""

        #: Boolean: Use enum values.
        use_enum_values = True

        #: Dict[object, Callable]: custom json encoder.
        json_encoders = {
            pydantic.SecretStr: lambda v: v.get_secret_value() if v else None,
            pydantic.SecretBytes: lambda v: v.get_secret_value() if v else None,
            bytes: lambda v: v.decode() if v else None,
            datetime: lambda v: int(v.timestamp()) if v else None,
            date: lambda v: int(time.mktime(v.timetuple())) if v else None,
        }

        # Allow creating new fields in model.
        allow_population_by_field_name = True

        # Allow validate assignment.
        validate_assignment = True

        # Remove trailing whitespace
        anystr_strip_whitespace = True
