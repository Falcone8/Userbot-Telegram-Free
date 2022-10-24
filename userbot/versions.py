# pylint: disable=missing-module-docstring
# All rights reserved.

from sys import version_info

from pyrogram import __version__ as __pyro_version__  # noqa

from loader import __version__ as __loader_version__  # noqa
from loader.userbot import api

__major__ = 1
__minor__ = 0
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_version() -> str:
    return f"{__major__}.{__minor__}.{__micro__}"


async def get_full_version() -> str:
    core = await api.get_core()
    ver = f"{get_version()}-build.{core.count}"

    return ver + '@' + core.branch
