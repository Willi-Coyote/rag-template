import logging
import os
from _contextvars import ContextVar
from logging import Logger
from typing import Optional

session_id_context: ContextVar[Optional[str]] = ContextVar('session_id', default=None)


class SessionIDLogFilter(logging.Filter):
    def filter(self, record):
        session_id = session_id_context.get()
        record.session_id = session_id if session_id is not None else 'unknown'
        return True


def setup_logger() -> Logger:
    default_logger = logging.getLogger("default")

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - [Session ID: %(session_id)s] - %(message)s')
    handler.setFormatter(formatter)
    handler.addFilter(SessionIDLogFilter())
    default_logger.addHandler(handler)

    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    default_logger.setLevel(level)

    return default_logger


logger: Logger = setup_logger()
