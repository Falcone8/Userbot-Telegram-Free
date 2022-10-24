# pylint: disable=missing-module-docstring
#
# All rights reserved.

from pyrogram import StopPropagation
from pyrogram.raw.base import Message
from pyrogram.raw.types import MessageService, MessageActionContactSignUp

from userbot import userbot


@userbot.on_raw_update(-5)
async def _on_raw(_, m: Message, *__) -> None:
    if isinstance(m, MessageService) and isinstance(m.action, MessageActionContactSignUp):
        raise StopPropagation
