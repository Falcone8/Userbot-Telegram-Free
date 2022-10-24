# pylint: disable=missing-module-docstring
# All rights reserved.

__all__ = ['Restart']

from loader.userbot.api import restart
from userbot import logging
from ...ext import RawClient

_LOG = logging.getLogger(__name__)


class Restart(RawClient):  # pylint: disable=missing-class-docstring
    @staticmethod
    async def restart(hard: bool = False, **_) -> None:
        """ Restart the userbot """
        _LOG.info(f"Restarting userbot [{'HARD' if hard else 'SOFT'}]")
        restart(hard)
