# pylint: disable=missing-module-docstring
# All rights reserved.

__all__ = ['GetUserDict']

from typing import Dict, Union

from ...ext import RawClient


class GetUserDict(RawClient):  # pylint: disable=missing-class-docstring
    async def get_user_dict(self, user_id: Union[int, str]) -> Dict[str, str]:
        """This will return user `Dict` which contains
        `id`(chat id), `fname`(first name), `lname`(last name),
        `flname`(full name), `uname`(username) and `mention`.
        """
        user_obj = await self.get_users(user_id)
        fname = (user_obj.first_name or '').strip()
        lname = (user_obj.last_name or '').strip()
        username = (user_obj.username or '').strip()
        if fname and lname:
            full_name = fname + ' ' + lname
        elif fname or lname:
            full_name = fname or lname
        else:
            full_name = "user"
        mention = f"[{username or full_name}](tg://user?id={user_id})"
        return {'id': user_obj.id, 'fname': fname, 'lname': lname,
                'flname': full_name, 'uname': username, 'mention': mention}
