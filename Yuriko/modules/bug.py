# Copyright (c) 2022 Shiinobu Project

from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from Yuriko import pbot as Client
from Yuriko import (
    OWNER_ID as owner,
    SUPPORT_CHAT as log,
)
from Yuriko.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command("bug"))
@capture_err
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username} / `{msg.chat.id}`")
    else:
        chat_username = (f"Private Group / `{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    thumb = "https://telegra.ph/file/db6425a997e17f6b6eafc.jpg"
    
    bug_report = f"""
**#BUG : ** **[Master](https://t.me/Shubhanshutya)**
**From User : ** **{mention}**
**User ID : ** **{user_id}**
**Group : ** **{chat_username}**
**Bug Report : ** **{bugs}**
**Event Stamp : ** **{datetimes}**"""

    
    if msg.chat.type == "private":
        await msg.reply_text("❎ <b>This command only works in groups.</b>")
        return

    if user_id == owner:
        if bugs:
            await msg.reply_text(
                f"❎ <b>How can be owner bot reporting bug idiot??</b>",
            )
            return
        else:
            await msg.reply_text(
                f"❎ <b>Owner noob!</b>",
            )
    elif user_id != owner:
        if bugs:
            await msg.reply_text(
                f"<b>Bug Report : {bugs}</b>\n\n"
                "✅ <b>The bug was successfully reported to the support group!</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴄʟᴏsᴇ", callback_data=f"close_reply")
                        ]
                    ]
                )
            )
            await Client.send_photo(
                log,
                photo=thumb,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "➡ ᴠɪᴇᴡ ʙᴜɢ", url=f"{msg.link}")
                        ],
                        [
                            InlineKeyboardButton(
                                "ᴄʟᴏsᴇ", callback_data=f"close_send_photo")
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"❎ <b>No bug to Report!</b>",
            )
        
    

@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(Client, CallbackQuery):
    await CallbackQuery.message.delete()

__help__ = """
   
` Bug Report Is a module for reporting bugs on KIGO bots`
  
`So that the bot can be fixed as soon as possible`
    
`✗ /bug <reason>` - `To Report Bugs`

**✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ!**
"""
__button__ = []
__buttons__ = []
  
__mod_name__ = "Bᴜɢ-Rᴇᴘᴏʀᴛ"
