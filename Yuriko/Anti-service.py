

from pyrogram import filters
from Yuriko import pbot as app
from Yuriko.utils.permissions import adminsOnly
from Yuriko.utils.dbfunctions import (antiservice_off, antiservice_on,
                                   is_antiservice_on)


@app.on_message(filters.command("antiservice") & ~filters.private)
@adminsOnly("can_change_info")
async def anti_service(_, message):
    if len(message.command) != 2:
        return await message.reply_text(
            "Usage: /antiservice [enable | disable]"
        )
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "enable":
        await antiservice_on(chat_id)
        await message.reply_text(
            "Enabled AntiService System. I will Delete Service Messages from Now on."
        )
    elif status == "disable":
        await antiservice_off(chat_id)
        await message.reply_text(
            "Disabled AntiService System. I won't Be Deleting Service Message from Now on."
        )
    else:
        await message.reply_text(
            "Unknown Suffix, Use /antiservice [enable|disable]"
        )


@app.on_message(filters.service, group=11)
async def delete_service(_, message):
    chat_id = message.chat.id
    try:
        if await is_antiservice_on(chat_id):
            return await message.delete()
    except Exception:
        pass

__mod_name__ = "Anti-Service"
__help__ = """
I Can Remove Service Message In Groups 
Like Users Join Messages, Leave Messages, Pinned Allert Messages, 
Voice Chat Invite Members Allerts ETC..

- /antiservice [enable|disable]

*✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: Tᴇᴀᴍ DᴇCᴏᴅᴇ!*
"""

__lovely_tools__
