""" manage your userbot :) """
# All rights reserved.

from userbot import userbot, Message, config


@userbot.on_cmd("status", about={
    'header': "list plugins, commands, filters status",
    'flags': {
        '-p': "plugin",
        '-c': "command",
        '-f': "filter"},
    'usage': "{tr}status [flags] [name]",
    'examples': [
        "{tr}status", "{tr}status -p",
        "{tr}status -p gdrive", "{tr}status -c {tr}gls"]}, del_pre=True, allow_channels=False)
async def status(message: Message) -> None:
    """ view current status """
    name_ = message.filtered_input_str
    type_ = list(message.flags)
    if not type_:
        out_str = f"""📊 **--Userbot Status--** 📊

🗃 **Plugins** : `{len(userbot.manager.plugins)}`
        ✅ **Loaded** : `{len(userbot.manager.loaded_plugins)}`
        ❎ **Unloaded** : `{len(userbot.manager.unloaded_plugins)}`

⚔ **Commands** : `{len(userbot.manager.commands)}`
        ✅ **Loaded** : `{len(userbot.manager.loaded_commands)}`
        ❎ **Unloaded** : `{len(userbot.manager.unloaded_commands)}`

⚖ **Filters** : `{len(userbot.manager.filters)}`
        ✅ **Loaded** : `{len(userbot.manager.loaded_filters)}`
        ❎ **Unloaded** : `{len(userbot.manager.unloaded_filters)}`
"""
    elif 'p' in type_:
        if name_:
            if name_ in userbot.manager.plugins:
                plg = userbot.manager.plugins[name_]
                out_str = f"""🗃 **--Plugin Status--** 🗃

🔖 **Name** : `{plg.name}`
📝 **Doc** : `{plg.doc}`
✅ **Loaded** : `{plg.is_loaded}`

⚔ **Commands** : `{len(plg.commands)}`
        `{'`,    `'.join((cmd.name for cmd in plg.commands))}`
        ✅ **Loaded** : `{len(plg.loaded_commands)}`
        ❎ **Unloaded** : `{len(plg.unloaded_commands)}`
        `{'`,    `'.join((cmd.name for cmd in plg.unloaded_commands))}`

⚖ **Filters** : `{len(plg.filters)}`
        ✅ **Loaded** : `{len(plg.loaded_filters)}`
        ❎ **Unloaded** : `{len(plg.unloaded_filters)}`
        `{'`,    `'.join((flt.name for flt in plg.unloaded_filters))}`
"""
            else:
                await message.err(f"plugin : `{name_}` not found!")
                return
        else:
            out_str = f"""🗃 **--Plugins Status--** 🗃

🗂 **Total** : `{len(userbot.manager.plugins)}`
✅ **Loaded** : `{len(userbot.manager.loaded_plugins)}`
❎ **Unloaded** : `{len(userbot.manager.unloaded_plugins)}`
        `{'`,    `'.join((cmd.name for cmd in userbot.manager.unloaded_plugins))}`
"""
    elif 'c' in type_:
        if name_:
            if not name_.startswith(config.CMD_TRIGGER):
                n_name_ = config.CMD_TRIGGER + name_
            if name_ in userbot.manager.commands:
                cmd = userbot.manager.commands[name_]
            elif n_name_ in userbot.manager.commands:
                cmd = userbot.manager.commands[n_name_]
            else:
                await message.err(f"command : {name_} not found!")
                return
            out_str = f"""⚔ **--Command Status--** ⚔

🔖 **Name** : `{cmd.name}`
📝 **Doc** : `{cmd.doc}`
🤖 **Via Bot** : `{cmd.allow_via_bot}`
✅ **Loaded** : `{cmd.loaded}`
"""
        else:
            out_str = f"""⚔ **--Commands Status--** ⚔

🗂 **Total** : `{len(userbot.manager.commands)}`
✅ **Loaded** : `{len(userbot.manager.loaded_commands)}`
❎ **Unloaded** : `{len(userbot.manager.unloaded_commands)}`
        `{'`,    `'.join((cmd.name for cmd in userbot.manager.unloaded_commands))}`
"""
    elif 'f' in type_:
        if name_:
            if name_ in userbot.manager.filters:
                flt = userbot.manager.filters[name_]
                out_str = f"""⚖ **--Filter Status--** ⚖

🔖 **Name** : `{flt.name}`
📝 **Doc** : `{flt.doc}`
🤖 **Via Bot** : `{flt.allow_via_bot}`
✅ **Loaded** : `{flt.loaded}`
"""
            else:
                await message.err(f"filter : {name_} not found!")
                return
        else:
            out_str = f"""⚖ **--Filters Status--** ⚖

🗂 **Total** : `{len(userbot.manager.filters)}`
✅ **Loaded** : `{len(userbot.manager.loaded_filters)}`
❎ **Unloaded** : `{len(userbot.manager.unloaded_filters)}`
        `{'`,    `'.join((flt.name for flt in userbot.manager.unloaded_filters))}`
"""
    else:
        await message.err("invalid input flag!")
        return
    await message.edit(out_str.replace("        ``\n", ''), del_in=0)


@userbot.on_cmd('load', about={
    'header': "load plugins, commands, filters",
    'flags': {
        '-p': "plugin",
        '-c': "command",
        '-f': "filter"},
    'usage': "{tr}load [flags] [name | names]",
    'examples': [
        "{tr}load -p gdrive", "{tr}load -c gls gup"]}, del_pre=True, allow_channels=False)
async def load(message: Message) -> None:
    """ load plugins, commands, filters """
    if not message.filtered_input_str:
        await message.err("name required!")
        return
    await message.edit("`Loading...`")
    names_ = message.filtered_input_str.split(' ')
    type_ = list(message.flags)
    if 'p' in type_:
        found = set(names_).intersection(set(userbot.manager.plugins))
        if found:
            out = await userbot.manager.load_plugins(list(found))
            if out:
                out_str = "**--Loaded Plugin(s)--**\n\n"
                for plg_name, cmds in out.items():
                    out_str += f"**{plg_name}** : `{'`,    `'.join(cmds)}`\n"
            else:
                out_str = f"already loaded! : `{'`,    `'.join(names_)}`"
        else:
            await message.err(f"plugins : {', '.join(names_)} not found!")
            return
    elif 'c' in type_:
        for t_name in names_:
            if not t_name.startswith(config.CMD_TRIGGER):
                names_.append(config.CMD_TRIGGER + t_name)
        found = set(names_).intersection(set(userbot.manager.commands))
        if found:
            out = await userbot.manager.load_commands(list(found))
            if out:
                out_str = "**--Loaded Command(s)--**\n\n"
                out_str += f"`{'`,    `'.join(out)}`"
            else:
                out_str = f"already loaded! : `{'`,    `'.join(names_)}`"
        else:
            await message.err(f"commands : {', '.join(names_)} not found!")
            return
    elif 'f' in type_:
        found = set(names_).intersection(set(userbot.manager.filters))
        if found:
            out = await userbot.manager.load_filters(list(found))
            if out:
                out_str = "**--Loaded Filter(s)--**\n\n"
                out_str += f"`{'`,    `'.join(out)}`"
            else:
                out_str = f"already loaded! : `{'`,    `'.join(names_)}`"
        else:
            await message.err(f"filters : {', '.join(names_)} not found!")
            return
    else:
        await message.err("invalid input flag!")
        return
    await message.edit(out_str, del_in=0, log=True)


@userbot.on_cmd('unload', about={
    'header': "unload plugins, commands, filters",
    'flags': {
        '-p': "plugin",
        '-c': "command",
        '-f': "filter"},
    'usage': "{tr}unload [flags] [name | names]",
    'examples': [
        "{tr}unload -p gdrive", "{tr}unload -c gls gup"]}, del_pre=True, allow_channels=False)
async def unload(message: Message) -> None:
    """ unload plugins, commands, filters """
    if not message.flags:
        await message.err("flag required!")
        return
    if not message.filtered_input_str:
        await message.err("name required!")
        return
    await message.edit("`UnLoading...`")
    names_ = message.filtered_input_str.split(' ')
    type_ = list(message.flags)
    if 'p' in type_ and names_:
        found = set(names_).intersection(set(userbot.manager.plugins))
        if found:
            out = await userbot.manager.unload_plugins(list(found))
            if out:
                out_str = "**--Unloaded Plugin(s)--**\n\n"
                for plg_name, cmds in out.items():
                    out_str += f"**{plg_name}** : `{'`,    `'.join(cmds)}`\n"
            else:
                out_str = f"already unloaded! : `{'`,    `'.join(names_)}`"
        else:
            await message.err(f"plugins : {', '.join(names_)} not found!")
            return
    elif 'c' in type_ and names_:
        for t_name in names_:
            if not t_name.startswith(config.CMD_TRIGGER):
                names_.append(config.CMD_TRIGGER + t_name)
        found = set(names_).intersection(set(userbot.manager.commands))
        if found:
            out = await userbot.manager.unload_commands(list(found))
            if out:
                out_str = "**--Unloaded Command(s)--**\n\n"
                out_str += f"`{'`,    `'.join(out)}`"
            else:
                out_str = f"already unloaded! : `{'`,    `'.join(names_)}`"
        else:
            await message.err(f"commands : {', '.join(names_)} not found!")
            return
    elif 'f' in type_ and names_:
        found = set(names_).intersection(set(userbot.manager.filters))
        if found:
            out = await userbot.manager.unload_filters(list(found))
            if out:
                out_str = "**--Unloaded Filter(s)--**\n\n"
                out_str += f"`{'`,    `'.join(out)}`"
            else:
                out_str = f"already unloaded! : `{'`,    `'.join(names_)}`"
        else:
            await message.err(f"filters : {', '.join(names_)} not found!")
            return
    else:
        await message.err("invalid input flag!")
        return
    await message.edit(out_str, del_in=0, log=True)


@userbot.on_cmd('reload', about={'header': "Reload all plugins"}, allow_channels=False)
async def reload_(message: Message) -> None:
    """ Reload all plugins """
    await message.edit("`Reloading All Plugins`")
    await message.edit(
        f"`Reloaded {await userbot.reload_plugins()} Plugins`", del_in=3, log=True)


@userbot.on_cmd('clear_unloaded', about={'header': "clear saved unloaded data in DB"},
               allow_channels=False)
async def clear_(message: Message) -> None:
    """ clear all save filters in DB """
    await message.edit("`Clearing Unloaded Data...`")
    await message.edit(
        f"**Cleared Unloaded** : `{await userbot.manager.clear_unloaded()}`",
        del_in=3, log=True)
