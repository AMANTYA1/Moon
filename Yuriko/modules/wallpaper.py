"""
MIT License

Copyright (c) 2022 Aʙɪsʜɴᴏɪ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import random

import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Yuriko import pgram as pbot


@pbot.on_message(filters.command(["wall", "wallpaper"]))
async def wall(_, message: Message):
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = None
    if not text:
        return await message.reply_text("**Invalid Command Syntax**\n\n`/wall [name]`")
    m = await message.reply_text("`sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴡᴀʟʟᴘᴀᴘᴇʀ...`")
    try:
        url = requests.get(f"https://api.safone.me/wall?query={text}").json()["results"]
        ran = random.randint(0, 3)
        await message.reply_photo(
            photo=url[ran]["imageUrl"],
            caption=f"💕 **Request By ʙʏ :**\n👉 {message.from_user.mention}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🤗Link🤗", url=url[ran]["imageUrl"])],
                ]
            ),
        )
        await m.delete()
    except Exception:
        await m.edit_text(
            f"`No Wallpaper found : `{text}`",
        )


# ᴛʜᴀɴᴋs https://github.com/TheAnonymous2005/FallenRobot/blob/master/FallenRobot/modules/wallpaper.py
