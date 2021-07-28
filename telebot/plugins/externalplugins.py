import os
from pathlib import Path

import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument
from telebot.telebotConfig import Config, Var
from telebot.utils import load_module
# from . import BOTLOG, BOTLOG_CHATID

BOTLOG = True
PRIVATE_GROUP_ID = Var.PRIVATE_GROUP_ID
if Config.PLUGIN_CHANNEL:

    async def install():
        documentss = await bot.get_messages(
            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"telebot/plugins/{plugin_name}"):
                return
            downloaded_file_name = await bot.download_media(
                await bot.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),
                "telebot/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))

    bot.loop.create_task(install())
if BOTLOG:
    async def sus():
        await bot.send_message(
            PRIVATE_GROUP_ID,
            f"Successfully installed All Plugins from Channel",
        )
    bot.loop.create_task(sus())
