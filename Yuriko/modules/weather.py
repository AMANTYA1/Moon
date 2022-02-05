# Copyright (C) 2020-2021 @DeshadeethThisarana

# This file is part of Shadow (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import io
import time

import aiohttp
from telethon.tl import functions, types
from telethon.tl.types import *

from Yuriko.confing import get_int_key, get_str_key
from Yuriko.events import register
from Yuriko import telethn as tbot

#OPENWEATHERMAP_ID = get_str_key("OPENWEATHERMAP_ID", "7181b8a4580be607eddacd56777bf64b")
OWNER_ID = get_int_key("OWNER_ID")


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerChat):
        ui = await tbot.get_peer_id(user)
        ps = (
            await tbot(functions.messages.GetFullChatRequest(chat.chat_id))
        ).full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


@register(pattern="^/not (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        elif event.chat_id == iid and event.sender_id == OWNER_ID:
            pass
        else:
            return
    sample_url = (
        "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    )
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(
            sample_url.format(input_str, OPENWEATHERMAP_ID)
        )
    response_api = await response_api_zero.json()
    if response_api["cod"] == 200:
        country_code = response_api["sys"]["country"]
        country_time_zone = int(response_api["timezone"])
        sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
        sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
        await event.reply(
            """
**Location**: {}
**Temperature ☀️**: {}°С
    __minimium__: {}°С
    __maximum__ : {}°С
**Humidity 🌤**: {}%
**Wind** 💨: {}m/s
**Clouds** ☁️: {}hpa
**Sunrise** 🌤: {} {}
**Sunset** 🌝: {} {}""".format(
                input_str,
                response_api["main"]["temp"],
                response_api["main"]["temp_min"],
                response_api["main"]["temp_max"],
                response_api["main"]["humidity"],
                response_api["wind"]["speed"],
                response_api["clouds"]["all"],
                # response_api["main"]["pressure"],
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_rise_time)),
                country_code,
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_set_time)),
                country_code,
            )
        )
    else:
        await event.reply(response_api["message"])


@register(pattern="^/weatherimg (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        elif event.chat_id == iid and event.sender_id == OWNER_ID:
            pass
        else:
            return
    sample_url = "https://wttr.in/{}.png"
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str))
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await event.reply(file=out_file)

__mod_name__ = "Wᴇᴀᴛʜᴇʀ"

__help__ = """
Available Commands:

✗ /weatherimg (city name) - `Gives weather image`

*✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: Tᴇᴀᴍ DᴇCᴏᴅᴇ!*
"""
