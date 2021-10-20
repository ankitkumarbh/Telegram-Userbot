import asyncio
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import ChatAdminRights
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError, PeerIdInvalidError 


from . import *

@telebot.on(admin_cmd(pattern="schd ?(.*)"))
@telebot.on(sudo_cmd(pattern="schd ?(.*)", allow_sudo=True))
async def schd(event):
    a = event.pattern_match.group(1)
    b = a.split(" ")
    wwait = b[0]
    times = int(b[1])
    idds = b[2]
    previous_message = await event.get_reply_message()
    if previous_message:
        previous_message = await event.get_reply_message()
        idds = previous_message.id
    if idds:
        idds = int(b[2])
    kk = await event.reply("`Schedule Broadcasting Msg...`")
    er = 0
    done = 0
    count = 0
    chatidd = await event.get_chat()
    chatidd = chatidd.id
    while count != times:
        count += 1
        er = 0
        done = 0
        await asyncio.sleep(int(wwait))
        await kk.edit("`Broadcasting...`")
        msg = await borg.get_messages(chatidd, ids=idds)
        async for x in event.client.iter_dialogs():
            if x.is_group:
                chat = x.id
                try:
                    done += 1
                    await borg.send_message(chat, msg)
                except BaseException:
                    er += 1
        await kk.edit(f"Done in {done} chats, error in {er} chat(s)")
    await kk.reply("`Schedule Broadcast Finished...`")
