# pylint: disable=missing-module-docstring
# All rights reserved.


class StopConversation(Exception):
    """ raise if conversation has terminated """


class ProcessCanceled(Exception):
    """ raise if thread has terminated """


class UserBotNotFound(Exception):
    """ raise if userbot bot not found """
