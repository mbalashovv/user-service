"""This package contains all the handlers for the application.

In this package, you can store handlers that help you inherit and extend
native python logic.
"""

from app.pkg.handlers.recursive_attr import rec_getattr, rec_setattr

__all__ = ["rec_getattr", "rec_setattr"]
