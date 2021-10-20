from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import ChatAdminRights
# from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError, PeerIdInvalidError 


from . import *

@telebot.on(admin_cmd(pattern="gcast ?(.*)"))
@telebot.on(sudo_cmd(pattern="gcast ?(.*)", allow_sudo=True))
async def gcast(event):
    previous_message = await event.get_reply_message()
    if not previous_message:
        return await event.reply("`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[6:]
    kk = await event.reply("`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await borg.send_message(chat, previous_message)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")

# -------------------------------------

@telebot.on(admin_cmd(pattern="gucast ?(.*)"))
@telebot.on(sudo_cmd(pattern="gucast ?(.*)", allow_sudo=True))
async def gucast(event):
    xx = await event.get_reply_message()
    if not xx:
        return await event.reply("`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[7:]
    kk = await event.reply("`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await borg.send_message(chat, xx)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")

# -------------------------------------
