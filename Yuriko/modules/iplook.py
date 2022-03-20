from pyrogram import filters
from pyrogram.types import Message
import aiohttp
from Yuriko import pbot as bot
from pyrogram.errors import RPCError

import functools
from typing import Callable, Coroutine, Dict, List, Tuple, Union

def is_admin(func):
    @functools.wraps(func)
    async def oops(client,message):
        is_admin = False
        try:
            user = await message.chat.get_member(message.from_user.id)
            admin_strings = ("creator", "administrator")
            if user.status not in admin_strings:
                is_admin = False
            else:
                is_admin = True

        except ValueError:
            is_admin = True
        if is_admin:
            await func(client,message)
        else:
            await message.reply("Only Admins can execute this command!")
    return oops

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@bot.on_message(
    filters.command("getip") & ~filters.private & ~filters.bot)
@is_admin
async def cool_ip(client, message):
    input_str = get_text(message)
    msg = await message.reply( "`Please Wait.`")
    if not input_str:
        return await msg.edit("`Give Me IP As Input.`")
    url = f"https://ipapi.com/ip_api.php?ip={input_str}"    
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as resp:
          r = await resp.json()
    if not r.get("hostname"):
        return await msg.edit("<code>Invalid IP. Please Check Hostname.</code>")
    ok = f"""<b>IP :</b> <code>{r.get("ip")}</code> \n<b>Hostname :</b> <code>{r.get("hostname")}</code> \n<b>Type :</b> <code>{r.get("type")}</code> \n<b>Country Name :</b> <code>{r.get("country_name")} {r.get("location").get("country_flag_emoji")}</code> \n<b>Region Name :</b> <code>{r.get("region_name")}</code> \n<b>City :</b> <code>{r.get("city")}</code> \n<b>Zip :</b> <code>{r.get("zip")}</code> \n<b>Latitude :</b> <code>{r.get("latitude")}</code> \n<b>Longitude :</b> <code>{r.get("longitude")}</code> \n<b>Current Time :</b> <code>{r.get("time_zone").get("current_time")}</code> \n<b>Currency :</b> <code>{r.get("currency").get("name")}</code> \n<b>ISP :</b> <code>{r.get("connection").get("isp")}</code> \n<b>Is Proxy :</b> <code>{bool_to_emoji(r.get("security").get("is_proxy"))}</code> \n<b>Is Crawler :</b> <code>{bool_to_emoji(r.get("security").get("is_crawler"))}</code> \n<b>Treat Level :</b> <code>{r.get("security").get("threat_level")}</code>"""
    await msg.edit(ok)
     


def bool_to_emoji(bool_: bool):
    return "✅" if bool_ else "❌"


@bot.on_message(filters.private & filters.command(["getip"]))
async def cool_ip(client, message):
    input_str = get_text(message)
    msg = await message.reply( "`Please Wait.`")
    if not input_str:
        return await msg.edit("`Give Me IP As Input.`")
    url = f"https://ipapi.com/ip_api.php?ip={input_str}"    
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as resp:
          r = await resp.json()
    if not r.get("hostname"):
        return await msg.edit("<code>Invalid IP. Please Check Hostname.</code>")
    ok = f"""<b>IP :</b> <code>{r.get("ip")}</code> \n<b>Hostname :</b> <code>{r.get("hostname")}</code> \n<b>Type :</b> <code>{r.get("type")}</code> \n<b>Country Name :</b> <code>{r.get("country_name")} {r.get("location").get("country_flag_emoji")}</code> \n<b>Region Name :</b> <code>{r.get("region_name")}</code> \n<b>City :</b> <code>{r.get("city")}</code> \n<b>Zip :</b> <code>{r.get("zip")}</code> \n<b>Latitude :</b> <code>{r.get("latitude")}</code> \n<b>Longitude :</b> <code>{r.get("longitude")}</code> \n<b>Current Time :</b> <code>{r.get("time_zone").get("current_time")}</code> \n<b>Currency :</b> <code>{r.get("currency").get("name")}</code> \n<b>ISP :</b> <code>{r.get("connection").get("isp")}</code> \n<b>Is Proxy :</b> <code>{bool_to_emoji(r.get("security").get("is_proxy"))}</code> \n<b>Is Crawler :</b> <code>{bool_to_emoji(r.get("security").get("is_crawler"))}</code> \n<b>Treat Level :</b> <code>{r.get("security").get("threat_level")}</code>"""
    await msg.edit(ok)

__mod_name__ = "Iᴘ"

__help__ = """
Commands
✗ /getip - `[Your-Ip] Get ip information.`

*✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ!*
"""
__lovely_tools__ = __help__
