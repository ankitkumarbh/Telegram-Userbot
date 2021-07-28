# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.



import os
from datetime import datetime as dt
from random import choice
from shutil import rmtree
from telebot.google_images_download import googleimagesdownload

import pytz
import requests
from bs4 import BeautifulSoup as b

from . import *

@telebot.on(admin_cmd(
    pattern=r"dob ?(.*)",
))
async def hbd(event):
    if not event.pattern_match.group(1):
        await eor(event, "`Put input in dd/mm/yyyy format`")
        return
    if event.reply_to_msg_id:
        kk = await event.get_reply_message()
        nam = await ultroid_bot.get_entity(kk.from_id)
        name = nam.first_name
    else:
        a = await ultroid_bot.get_me()
        name = a.first_name
    zn = pytz.timezone("Asia/Kolkata")
    abhi = dt.now(zn)
    n = event.text
    q = n[5:]
    p = n[5:7]
    r = n[8:10]
    s = n[11:]
    day = int(p)
    month = r
    paida = q
    jn = dt.strptime(paida, "%d/%m/%Y")
    jnm = zn.localize(jn)
    zinda = abhi - jnm
    barsh = (zinda.total_seconds()) / (365.242 * 24 * 3600)
    saal = int(barsh)
    mash = (barsh - saal) * 12
    mahina = int(mash)
    divas = (mash - mahina) * (365.242 / 12)
    din = int(divas)
    samay = (divas - din) * 24
    ghanta = int(samay)
    pehl = (samay - ghanta) * 60
    mi = int(pehl)
    sec = (pehl - mi) * 60
    slive = int(sec)
    y = int(s) + int(saal) + 1
    m = int(r)
    brth = dt(y, m, day)
    cm = dt(abhi.year, brth.month, brth.day)
    ish = (cm - abhi.today()).days + 1
    dan = ish
    if dan == 0:
        hp = "`Happy BirthDay To U🎉🎊`"
    elif dan < 0:
        okk = 365 + ish
        hp = f"{okk} Days Left 🥳"
    elif dan > 0:
        hp = f"{ish} Days Left 🥳"
    if month == "12":
        sign = "Sagittarius" if (day < 22) else "Capricorn"
    elif month == "01":
        sign = "Capricorn" if (day < 20) else "Aquarius"
    elif month == "02":
        sign = "Aquarius" if (day < 19) else "Pisces"
    elif month == "03":
        sign = "Pisces" if (day < 21) else "Aries"
    elif month == "04":
        sign = "Aries" if (day < 20) else "Taurus"
    elif month == "05":
        sign = "Taurus" if (day < 21) else "Gemini"
    elif month == "06":
        sign = "Gemini" if (day < 21) else "Cancer"
    elif month == "07":
        sign = "Cancer" if (day < 23) else "Leo"
    elif month == "08":
        sign = "Leo" if (day < 23) else "Virgo"
    elif month == "09":
        sign = "Virgo" if (day < 23) else "Libra"
    elif month == "10":
        sign = "Libra" if (day < 23) else "Scorpion"
    elif month == "11":
        sign = "Scorpio" if (day < 22) else "Sagittarius"
    sign = f"{sign}"
    params = (("sign", sign), ("today", day))
    response = requests.post("https://aztro.sameerkumar.website/", params=params)
    json = response.json()
    dd = json.get("current_date")
    ds = json.get("description")
    lt = json.get("lucky_time")
    md = json.get("mood")
    cl = json.get("color")
    ln = json.get("lucky_number")
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"""
    Name -: {name}

D.O.B -:  {paida}

Lived -:  {saal}yr, {mahina}m, {din}d, {ghanta}hr, {mi}min, {slive}sec

Birthday -: {hp}

Zodiac -: {sign}

**Horoscope On {dd} -**

`{ds}`

    Lucky Time :-        {lt}
    Lucky Number :-   {ln}
    Lucky Color :-        {cl}
    Mood :-                   {md}
    """,
        reply_to=event.reply_to_msg_id,
    )


@telebot.on(admin_cmd(pattern="sticker ?(.*)"))
async def _(event):
    x = event.pattern_match.group(1)
    if not x:
        return await eor(event, "`Give something to search`")
    uu = await eor(event, "`Processing...`")
    z = requests.get("https://combot.org/telegram/stickers?q=" + x).text
    xx = b(z, "lxml")
    title = xx.find_all("div", "sticker-pack__title")
    link = xx.find_all("a", {"class": "sticker-pack__btn"})
    if not link:
        return await uu.edit("Found Nothing")
    a = "SᴛɪᴄᴋEʀs Aᴡᴀɪʟᴀʙʟᴇ ~"
    for xxx, yyy in zip(title, link):
        v = xxx.get_text()
        w = yyy["href"]
        d = f"\n\n[{v}]({w})"
        if d not in a:
            a += d
    await uu.edit(a)


@telebot.on(admin_cmd(pattern="wall ?(.*)"))
async def wall(event):
    inp = event.pattern_match.group(1)
    if not inp:
        return await eor(event, "`Give me something to search..`")
    nn = await eor(event, "`Processing Keep Patience...`")
    query = f"hd {inp}"
    gi = googleimagesdownload()
    args = {
        "keywords": query,
        "limit": 10,
        "format": "jpg",
        "output_directory": "./resources/downloads/",
    }
    gi.download(args)
    xx = choice(os.listdir(os.path.abspath(f"./resources/downloads/{query}/")))
    await event.client.send_file(event.chat_id, f"./resources/downloads/{query}/{xx}")
    rmtree(f"./resources/downloads/{query}/")
    await nn.delete()


CMD_HELP.update(
    {
        "specialtools" : "`wspr <username>` \nSend secret message..\n `sticker <query>`\n \n Search Stickers as Per ur Wish..\n \n `getaudio <reply to an audio>` \n Download Audio To put in ur Desired Video/Gif. \n `addaudio <reply to Video/gif>` \n It will put the above audio to the replied video/gif. \n `dob <date of birth>` \n Put in dd/mm/yy Format only(eg .dob 01/01/1999). \n `wall <query>`"
    }
)
