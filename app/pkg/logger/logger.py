"""Methods for working with logger."""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.pkg.settings import settings

LOG_FORMAT = (
    "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%("
    "funcName)s(%(lineno)d) - %(message)s "
)


def get_file_handler(file_name: str) -> RotatingFileHandler:
    """Get file handler for logger."""

    Path(file_name).absolute().parent.mkdir(exist_ok=True, parents=True)
    file_handler = RotatingFileHandler(
        filename=file_name,
        maxBytes=5242880,
        backupCount=10,
    )
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    return file_handler


def get_stream_handler():
    """Get stream handler for logger."""

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    return stream_handler


def get_logger(name):
    """Get logger."""

    logger = logging.getLogger(name)
    file_path = str(
        Path(
            settings.FOLDER_PATH,
            f"{settings.API_INSTANCE_APP_NAME}.log",
        ).absolute(),
    )
    logger.addHandler(get_file_handler(file_name=file_path))
    logger.addHandler(get_stream_handler())
    logger.setLevel(settings.LOGGING_LEVEL.upper())
    return logger
