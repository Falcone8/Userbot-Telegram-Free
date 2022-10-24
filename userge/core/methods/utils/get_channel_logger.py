# pylint: disable=missing-module-docstring
# All rights reserved.

__all__ = ['GetCLogger']

import inspect

from ... import types
from ...ext import RawClient


class GetCLogger(RawClient):  # pylint: disable=missing-class-docstring
    # pylint: disable=invalid-name
    def getCLogger(self, name: str = '') -> 'types.new.ChannelLogger':
        """ This returns new channel logger object """
        if not name:
            name = inspect.currentframe().f_back.f_globals['__name__']

        return types.new.ChannelLogger(self, name)
