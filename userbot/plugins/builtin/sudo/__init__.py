# All rights reserved.

"""manage sudo cmds and users"""


from typing import Set

USERS: Set[int] = set()
COMMANDS: Set[str] = set()


class Dynamic:
    ENABLED = False
