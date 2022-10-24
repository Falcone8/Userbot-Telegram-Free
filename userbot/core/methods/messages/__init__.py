# pylint: disable=missing-module-docstring
# All rights reserved.

__all__ = ['Messages']

from .send_message import SendMessage
from .edit_message_text import EditMessageText
from .send_as_file import SendAsFile


class Messages(SendMessage, EditMessageText, SendAsFile):
    """ methods.messages """
