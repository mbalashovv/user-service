"""Base business models.

All models **must** inherit from them.
"""

from app.pkg.models.base.enum import BaseEnum
from app.pkg.models.base.exception import BaseAPIException
from app.pkg.models.base.model import BaseModel, Model

__all__ = [
    "BaseEnum",
    "BaseAPIException",
    "BaseModel",
    "Model",
]
