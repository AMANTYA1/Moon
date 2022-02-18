import asyncio


from pymongo import MongoClient
from pyrogram import filters

from Yuriko.confing import get_str_key
from Yuriko import pbot

MONGO_DB_URI = get_str_key("MONGO_URI")
client = MongoClient(MONGO_DB_URI)
dbd = client["missjuliarobot"]
approved_users = dbd.approve
db = dbd
chnldb = db.antichnldb


@pbot.on_message(filters.command(["antichannel"]) & filters.group)
async def locks_dfunc(_, message):
    lol = await message.reply("**Processing...**")
    if len(message.command) != 2:
        return await lol.edit("Expected on or off 👀")
    parameter = message.text.strip().split(None, 1)[1].lower()

    if (
        parameter == "on"
        or parameter == "ON"
        or parameter == "enable"
        or parameter == "Enable"
    ):
        if not message.from_user:
            return
        chat_id = str(message.chat.id)
        isittrue = chnldb.find_one({f"antichnl": chat_id})
        if not isittrue:
            chnldb.insert_one({f"antichnl": chat_id})
            return await lol.edit(
                f"**Anti Channel Guard enabled**\n\n`I will delete all message when someone send messages with channel names`"
            )
        else:
            return await lol.edit(
                f"Anti Channel Guard already enabled for this chat (`{message.chat.title}`)"
            )
    if parameter == "off" or parameter == "OFF":
        if not message.from_user:
            return
        chat_id = str(message.chat.id)
        isittrue = chnldb.find_one({f"antichnl": chat_id})
        if isittrue:
            chnldb.delete_one({f"antichnl": chat_id})
            return await lol.edit("Anti Channel Guard removed")
        else:
            return await lol.edit(
                f"Anti Channel Guard already disabled for this chat (`{message.chat.title}`)"
            )
    else:
        await lol.edit("I only recognize on & off 👀")


@pbot.on_message(
    filters.group
    & ~filters.incoming
    & ~filters.sticker
    & ~filters.document
    & ~filters.video
    & ~filters.animation
    & ~filters.text
    & ~filters.photo
)
async def anti_channel_guard(client, message):
    try:
        message.chat.title
        chat_id = str(message.chat.id)
    except:
        return message.continue_propagation()
    try:
        guardian = chnldb.find_one({f"antichnl": chat_id})
        if guardian:
            chat = message.sender_chat
            chnl_id = message.sender_chat.id
            if chat.type == "channel":
                try:
                    lel = await client.get_chat(chat_id)
                    lol = lel.linked_chat.id
                except:
                    await message.delete()
                    sed = await client.send_message(
                        chat_id=chat_id,
                        text="Anti-channel message detected. I deleted it..!",
                    )
                    await asyncio.sleep(5)
                    await sed.delete()
                    return
                if lol == chnl_id:
                    return message.continue_propagation()
                else:
                    await message.delete()
                    sed = await client.send_message(
                        chat_id=chat_id,
                        text="Anti-channel message detected. I deleted it..!",
                    )
                    await asyncio.sleep(5)
                    await sed.delete()
            else:
                return message.continue_propagation()
    except:
        return message.continue_propagation()

__mod_name__ = "Aɴᴛɪ-Cʜᴀɴɴᴇʟ"

__help__ = """
Due to new telegram update users can send messages to groups as channel. It is huge problem because admins can't recognize who sent that message                

When this feature enabled Daisy can delete messages sent by channels in your group 

Commands
✗ /antichannel `[on/off]: Enable/Disable antichannel guard`

Note: Messages of linked channel won't be deleted

*✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: Tᴇᴀᴍ DᴇCᴏᴅᴇ!*
"""
