# pylint: disable=missing-module-docstring
# All rights reserved.

__all__ = ['GetLogger']

import inspect

from userbot import logging


class GetLogger:  # pylint: disable=missing-class-docstring
    @staticmethod
    def getLogger(name: str = '') -> logging.Logger:  # pylint: disable=invalid-name
        """ This returns new logger object """
        if not name:
            name = inspect.currentframe().f_back.f_globals['__name__']

        return logging.getLogger(name)
