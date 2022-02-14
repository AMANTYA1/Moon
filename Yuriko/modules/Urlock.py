import asyncio

from pyrogram import filters
from pyrogram.errors import RPCError

from Yuriko import BOT_ID
from Yuriko.db.mongo_helpers.lockurl import add_chat, get_session, remove_chat
from Yuriko.function.pluginhelpers import (
    admins_only,
    edit_or_reply,
    get_url,
    member_permissions,
)
from Yuriko import pbot


@pbot.on_message(
    filters.command("urllock") & ~filters.edited & ~filters.bot & ~filters.private
)
@admins_only
async def hmm(_, message):
    global daisy_chats
    try:
        user_id = message.from_user.id
    except:
        return
    if not "can_change_info" in (await member_permissions(message.chat.id, user_id)):
        await message.reply_text("**You don't have enough permissions**")
        return
    if len(message.command) != 2:
        await message.reply_text(
            "I only recognize `/urllock on` and `/urllock off` only"
        )
        return
    status = message.text.split(None, 1)[1]
    message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("URL Block Already Activated In This Chat")
            return
        await lel.edit(
            f"URL Block Successfully Added For Users In The Chat {message.chat.id}"
        )

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("URL Block Was Not Activated In This Chat")
            return
        await lel.edit(
            f"URL Block Successfully Deactivated For Users In The Chat {message.chat.id}"
        )
    else:
        await message.reply_text(
            "I only recognize `/urllock on` and `/urllock off` only"
        )


@pbot.on_message(
    filters.incoming & filters.text & ~filters.private & ~filters.channel & ~filters.bot
)
async def hi(client, message):
    if not get_session(int(message.chat.id)):
        message.continue_propagation()
    try:
        user_id = message.from_user.id
    except:
        return
    try:
        if not len(await member_permissions(message.chat.id, user_id)) < 1:
            message.continue_propagation()
        if len(await member_permissions(message.chat.id, BOT_ID)) < 1:
            message.continue_propagation()
        if not "can_delete_messages" in (
            await member_permissions(message.chat.id, BOT_ID)
        ):
            message.continue_propagation()
    except RPCError:
        return
    try:

        lel = get_url(message)
    except:
        return

    if lel:
        try:
            await message.delete()
            sender = message.from_user.mention()
            lol = await client.send_message(
                message.chat.id,
                f"{sender}, Your message was deleted as it contain a link(s). \n ❗️ Links are not allowed here",
            )
            await asyncio.sleep(10)
            await lol.delete()
        except:
            message.continue_propagation()
    else:
        message.continue_propagation()
