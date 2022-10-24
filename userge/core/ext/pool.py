# pylint: disable=missing-module-docstring
# All rights reserved.

__all__ = ['submit_thread', 'run_in_thread']

import asyncio
import atexit
from concurrent.futures import ThreadPoolExecutor, Future
from functools import wraps, partial
from typing import Any, Callable

from userbot import logging, config

_LOG = logging.getLogger(__name__)
_EXECUTOR = ThreadPoolExecutor(config.WORKERS)
# pylint: disable=protected-access
_MAX = _EXECUTOR._max_workers


def submit_thread(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Future:
    """ submit thread to thread pool """
    return _EXECUTOR.submit(func, *args, **kwargs)


def run_in_thread(func: Callable[..., Any]) -> Callable[..., Any]:
    """ run in a thread """
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(_EXECUTOR, partial(func, *args, **kwargs))
    return wrapper


def _stop():
    _EXECUTOR.shutdown()
    _LOG.info(f"Stopped Pool : {_MAX} Workers")


atexit.register(_stop)
_LOG.info(f"Started Pool : {_MAX} Workers")
