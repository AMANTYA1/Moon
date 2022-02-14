import asyncio

from pyrogram import filters
from pyrogram.types import *

from Yuriko.db.mongo_helpers.antichannel import (
    add_anti_chnl,
    add_ban_chnl,
    add_dlt_chnl,
    anti_chnl,
    ban_chnl,
    dlt_chnl,
    rem_anti_chnl,
    rem_ban_chnl,
    rem_dlt_chnl,
)
from Yuriko import pbot


## ----------- BUTTONS -------------------------------------------------- BUTTONS ----------------------------------------------------------
## ------------------------------------- BUTTONS -------------------------------------------------- BUTTONS --------------------------------
def no_restrict(user_id, chat_id):
    NO_ANY = [[InlineKeyboardButton("Enable Anti-Channel ✅", callback_data=f"_enable_anti_chnl|{user_id}|{chat_id}")]]
    NO_ANY += [[InlineKeyboardButton("Close 🗑", callback_data="chnl_close")]]
    return NO_ANY


def unban_btn(anti_id, user_id, chat_id):
    LOL = [[InlineKeyboardButton("Ban ❌", callback_data=f"_ban|{anti_id}|{user_id}|{chat_id}")]]
    LOL += [[InlineKeyboardButton("Close 🗑", callback_data="chnl_close")]]
    return LOL


def chnl_ban_btn(anti_id, user_id, chat_id):
    LEL = [[InlineKeyboardButton("Unban ✅", callback_data=f"_unban_|{anti_id}|{user_id}|{chat_id}")]]
    LEL += [[InlineKeyboardButton("Close 🗑", callback_data="chnl_close")]]
    return LEL


def disable_chnl(user_id, chat_id):
    SEDD = [[InlineKeyboardButton("Disable Anti-Channel ❌", callback_data=f"_disable_anti_chnl|{user_id}|{chat_id}")]]
    SEDD += [[InlineKeyboardButton("Close 🗑", callback_data="chnl_close")]]
    return SEDD


def ban_btn(user_id, chat_id):
    BAN_BTNS = [[InlineKeyboardButton( "Ban ✔️", callback_data=f"_enable_ban|{user_id}|{chat_id}"), InlineKeyboardButton("Delete ✖️", callback_data=f"_enable_delete|{user_id}|{chat_id}")]]
    BAN_BTNS += [[InlineKeyboardButton("Disable Anti-Channel ❌", callback_data=f"_disable_anti_chnl|{user_id}|{chat_id}")]]
    BAN_BTNS += [[InlineKeyboardButton("Close 🗑", callback_data="chnl_close")]]
    return BAN_BTNS


def dlt_btn(user_id, chat_id):
    DLT_BTNS = [[InlineKeyboardButton("Ban ✖️", callback_data=f"_enable_ban|{user_id}|{chat_id}"), InlineKeyboardButton("Delete ✔️", callback_data=f"_enable_delete|{user_id}|{chat_id}")]]
    DLT_BTNS += [[InlineKeyboardButton("Disable Anti-Channel ❌", callback_data=f"_disable_anti_chnl|{user_id}|{chat_id}")]]
    DLT_BTNS += [[InlineKeyboardButton("Close 🗑", callback_data=f"chnl_close")]]
    return DLT_BTNS


def select_restrict(user_id, chat_id):
    SELECT = [[InlineKeyboardButton("Ban", callback_data=f"_enable_ban|{user_id}|{chat_id}"), InlineKeyboardButton("Delete", callback_data=f"_enable_delete|{user_id}|{chat_id}")]]
    SELECT += [[InlineKeyboardButton("Close 🗑", callback_data="chnl_close")]]
    return SELECT


## -----------------------------------------------------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------------------------------------------------


@pbot.on_message(filters.command(["antichannel"]) & filters.group)
async def locks_dfunc(_, message):
    chat_id = message.chat.id
    chat_title = message.chat.title
    user_id = message.from_user.id
    guardian = await anti_chnl(chat_id)
    anti_ban_chnl = await ban_chnl(chat_id)
    anti_dlt_chnl = await dlt_chnl(chat_id)
    user = await _.get_chat_member(chat_id, message.from_user.id)
    if user.status == "creator" or user.status == "administrator":
        pass
    else:
        return await message.reply("You aren't allowed!")
    lol = await message.reply("**Processing...**")
    if guardian:
        main = f"**Anti Channel is currently enabled for this chat!** (`{chat_title}`)"
        if anti_ban_chnl:
            text = "`Ban the anti-channel`"
            btn = ban_btn(user_id, chat_id)
        if anti_dlt_chnl:
            text = "`Delete the anti-channel's message`"
            btn = dlt_btn(user_id, chat_id)
        await lol.edit(
            main + "\n\nRestriction: " + text, reply_markup=InlineKeyboardMarkup(btn)
        )
    else:
        await lol.edit(
            f"**Anti Channel is currently disabled for this chat!** (`{chat_title}`)",
            reply_markup=InlineKeyboardMarkup(no_restrict(user_id, chat_id)),
        )


@pbot.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data.startswith("_"):
        try:
            chat_id = data.split("|")[-1]
            user_id = data.split("|")[-2]
            guardian = await anti_chnl(chat_id)
            anti_ban_chnl = await ban_chnl(chat_id)
            anti_dlt_chnl = await dlt_chnl(chat_id)
            user = await client.get_chat_member(chat_id, query.from_user.id)
        except Exception as e:
            return await query.message.edit(f"An error occured!\n\n=> {e}")

        if user.status == "creator" or user.status == "administrator":
            pass
        else:
            return await query.answer("You aren't allowed!")

        if data.startswith("_enable_anti_chnl"):
            try:
                if guardian:
                    if anti_ban_chnl:
                        btn = ban_btn(user_id, chat_id)
                        await query.message.edit(
                            "**Anti Channel is currently enabled for this chat!**\n\nRestriction: `Ban the anti-channel`",
                            reply_markup=InlineKeyboardMarkup(btn),
                        )
                    if anti_dlt_chnl:
                        btn = dlt_btn(user_id, chat_id)
                        await query.message.edit(
                            "**Anti Channel is currently enabled for this chat!**\n\nRestriction: `Delete the anti-channel's message`",
                            reply_markup=InlineKeyboardMarkup(btn),
                        )
                    else:
                        buttons = select_restrict(user_id, chat_id)
                        await query.message.edit(
                            "**Select the restriction method...**\n\n`Ban`: Will __ban the anti-channel__ & __delete its message__\n`Delete`: __Only delete anti-channel's messsgae__",
                            reply_markup=InlineKeyboardMarkup(buttons),
                        )
                else:
                    try:
                        buttons = select_restrict(user_id, chat_id)
                        await query.message.edit(
                            "**Select the restriction method...**\n\n`Ban`: Will __ban the anti-channel__ & __delete its message__\n`Delete`: __Only delete anti-channel's messsgae__",
                            reply_markup=InlineKeyboardMarkup(buttons),
                        )
                    except:
                        return
            except Exception as e:
                return await query.message.edit(f"An error occured!\n\n=> {e}")

        if data.startswith("_disable_anti_chnl"):
            try:
                if guardian:
                    try:
                        main = f"**Anti-Channel Guard successfully disabled in this chat!**"
                        if anti_ban_chnl:
                            text = "Ban the anti-channel"
                            buttons = no_restrict(user_id, chat_id)
                            sed = await rem_ban_chnl(chat_id)
                        if anti_dlt_chnl:
                            text = "Delete the anti-channel's message"
                            buttons = no_restrict(user_id, chat_id)
                            sed = await rem_dlt_chnl(chat_id)

                        if sed:
                            await rem_anti_chnl(chat_id)
                            await query.message.edit(
                                f"{main}\n\nRestriction was: `{text}`",
                                reply_markup=InlineKeyboardMarkup(btn),
                            )
                    except:
                        return
                else:
                    try:
                        buttons = no_restrict(user_id, chat_id)
                        await query.message.edit(
                            "**Anti-Channel Guard already disabled in this chat!**",
                            reply_markup=InlineKeyboardMarkup(buttons),
                        )
                    except:
                        return
            except Exception as e:
                return await query.message.edit(f"An error occured!\n\n=> {e}")

        if data.startswith("_enable_ban"):
            try:
                if anti_ban_chnl:
                    try:
                        buttons = ban_btn(user_id, chat_id)
                        await query.message.edit(
                            "Restriction **Ban** already enabled in this chat!",
                            reply_markup=InlineKeyboardMarkup(buttons),
                        )
                        await query.answer(
                            "Restriction Ban already enabled in this chat!"
                        )
                    except:
                        return
                if guardian:
                    if anti_dlt_chnl:
                        try:
                            buttons = ban_btn(user_id, chat_id)
                            await add_ban_chnl(chat_id)
                            await rem_dlt_chnl(chat_id)
                            await query.message.edit(
                                "Anti-Channel Guard enabled with Restriction **Ban**! & Old Restriction **Only Delete** disabled\n\n__From now Shadow will ban the channel who send messages as channels & delete its message__",
                                reply_markup=InlineKeyboardMarkup(buttons),
                            )
                            await query.answer(
                                "Successfully added Anti-Channel with the restriction ban!"
                            )
                        except:
                            return
                    else:
                        try:
                            buttons = ban_btn(user_id, chat_id)
                            await add_ban_chnl(chat_id)
                            await query.message.edit(
                                "Anti-Channel Guard enabled with Restriction **Ban**!\n\n__From now Shadow will ban the channel who send messages as channels & delete its message__",
                                reply_markup=InlineKeyboardMarkup(buttons),
                            )
                            await query.answer(
                                "Successfully added Anti-Channel with the restriction ban!"
                            )
                        except:
                            return
                else:
                    try:
                        buttons = ban_btn(user_id, chat_id)
                        await add_anti_chnl(chat_id)
                        await add_ban_chnl(chat_id)
                        await query.message.edit(
                            "Anti-Channel Guard enabled with Restriction **Ban**!\n\n__From now Shadow will ban the channel who send messages as channels & delete its message__",
                            reply_markup=InlineKeyboardMarkup(buttons),
                        )
                        await query.answer(
                            "Successfully added Anti-Channel with the restriction delete!"
                        )
                    except:
                        return
            except Exception as e:
                return await query.message.edit(f"An error occured!\n\n=> {e}")

        if data.startswith("_enable_delete"):
            try:
                if anti_dlt_chnl:
                    try:
                        buttons = dlt_btn(user_id, chat_id)
                        await query.message.edit(
                            "Restriction **Delete** already enabled in this chat!",
                            reply_markup=InlineKeyboardMarkup(buttons),
                        )
                        await query.answer(
                            "Restriction Delete already enabled in this chat!"
                        )
                    except:
                        return
                if guardian:
                    if anti_ban_chnl:
                        try:
                            buttons = dlt_btn(user_id, chat_id)
                            await add_dlt_chnl(chat_id)
                            await rem_ban_chnl(chat_id)
                            await query.message.edit(
                                "Anti-Channel Guard enabled with Restriction **Delete**! & Old Restriction **Ban** disabled\n\n__From now Shadow will delete the messages of Anti-Channels__",
                                reply_markup=InlineKeyboardMarkup(buttons),
                            )
                            await query.answer(
                                "Successfully added Anti-Channel with the restriction delete!"
                            )
                        except:
                            return
                    else:
                        try:
                            buttons = dlt_btn(user_id, chat_id)
                            await add_dlt_chnl(chat_id)
                            await query.message.edit(
                                "Anti-Channel Guard enabled with Restriction **Delete**!\n\n__From now Shadow will delete the messages of Anti-Channels__",
                                reply_markup=InlineKeyboardMarkup(buttons),
                            )
                            await query.answer(
                                "Successfully added Anti-Channel with the restriction delete!"
                            )
                        except:
                            return
                else:
                    try:
                        buttons = dlt_btn(user_id, chat_id)
                        await add_anti_chnl(chat_id)
                        await add_dlt_chnl(chat_id)
                        await query.message.edit(
                            "Anti-Channel Guard enabled with Restriction **Delete**!\n\n__From now Shadow will delete the messages of Anti-Channels__",
                            reply_markup=InlineKeyboardMarkup(buttons),
                        )
                        await query.answer(
                            "Successfully added Anti-Channel with the restriction delete!"
                        )
                    except:
                        return
            except Exception as e:
                return await query.message.edit(f"An error occured!\n\n=> {e}")

        if data.startswith("_unban_"):
            try:
                anti_id = data.split("|")[-3]
            except:
                return
            try:
                await client.resolve_peer(anti_id)
                res = await query.message.chat.unban_member(anti_id)
                chat_data = await client.get_chat(anti_id)
                mention = (
                    f"@{chat_data.username}" if chat_data.username else chat_data.title
                )
                buttons = unban_btn(anti_id, user_id, chat_id)
                if res:
                    try:
                        await query.message.edit(
                            f"{mention} has been unbanned by {query.from_user.mention}!"
                        )
                        await query.message.edit_reply_markup(
                            reply_markup=InlineKeyboardButton(buttons)
                        )
                    except:
                        return
            except Exception as e:
                return await query.message.edit(f"An error occured!\n\n=> {e}")

        if data.startswith("_ban_"):
            try:
                anti_id = data.split("|")[-3]
            except:
                return
            try:
                await client.resolve_peer(anti_id)
                res = await client.kick_chat_member(chat_id, anti_id)
                chat_data = await client.get_chat(anti_id)
                mention = (
                    f"@{chat_data.username}" if chat_data.username else chat_data.title
                )
                buttons = chnl_ban_btn(anti_id, user_id, chat_id)
                if res:
                    try:
                        await query.message.edit(
                            f"{mention} has been banned by {query.from_user.mention}!"
                        )
                        await query.message.edit_reply_markup(
                            reply_markup=InlineKeyboardButton(buttons)
                        )
                    except:
                        return
            except Exception as e:
                return await query.message.edit(f"An error occured!\n\n=> {e}")
        else:
            return
    else:
        return


custom_message_filter = filters.create(
    lambda _, __, message: False
    if message.forward_from_chat or message.from_user
    else True
)
custom_chat_filter = filters.create(
    lambda _, __, message: True if message.sender_chat else False
)


@pbot.on_message(custom_message_filter & filters.group & custom_chat_filter)
async def anti_channel_guard(client, message):
    try:
        chat_id = message.chat.id
        message.chat.title
        chat = message.sender_chat
        anti_id = message.sender_chat.id
        a_usrnm = message.sender_chat.username
        a_title = message.chat_data.title
        mention = f"@{a_usrnm}" if a_usrnm else a_title
        guardian = await anti_chnl(chat_id)
        anti_ban_chnl = await ban_chnl(chat_id)
        anti_dlt_chnl = await dlt_chnl(chat_id)
    except:
        return
    try:
        if guardian:
            if chat.type == "channel":
                try:
                    lel = await client.get_chat(chat_id)
                    lol = lel.linked_chat.id
                except:
                    try:
                        if anti_ban_chnl:
                            ban = await client.kick_chat_member(chat_id, anti_id)
                            ban += await message.delete()
                        if anti_dlt_chnl:
                            dlt = await message.delete()
                    except:
                        return
                    if ban:
                        text = f"{mention} has been banned.\n\n💡 They can write only with his profile but not through other channels."
                        btn = [
                            [
                                InlineKeyboardButton(
                                    "Unban ✅",
                                    callback_data=f"_unban_|{anti_id}|{user_id}|{chat_id}",
                                )
                            ]
                        ]
                    if dlt:
                        text = f"{mention}'s message has been deleted.\n\n💡 They can write with his profile or other channels in future also."
                        btn = [
                            [
                                InlineKeyboardButton(
                                    "Enable Anti-Channel Ban ✅",
                                    callback_data=f"_enable_ban|{user_id}|{chat_id}",
                                )
                            ]
                        ]
                    hmm = await message.reply(
                        f"{text}", reply_markup=InlineKeyboardMarkup(btn)
                    )
                    await asyncio.sleep(10)
                    await hmm.delete()
                    return
                if lol == anti_id:
                    return
                else:
                    try:
                        if anti_ban_chnl:
                            ban = await client.kick_chat_member(chat_id, anti_id)
                            ban += await message.delete()
                        if anti_dlt_chnl:
                            dlt = await message.delete()
                    except:
                        return
                    if ban:
                        text = f"{mention} has been banned.\n\n💡 They can write only with his profile but not through other channels."
                        btn = [
                            [
                                InlineKeyboardButton(
                                    "Unban ✅",
                                    callback_data=f"_unban_|{anti_id}|{user_id}|{chat_id}",
                                )
                            ]
                        ]
                    if dlt:
                        text = f"{mention}'s message has been deleted.\n\n💡 They can write with his profile or other channels in future also."
                        btn = [
                            [
                                InlineKeyboardButton(
                                    "Enable Anti-Channel Ban ✅",
                                    callback_data=f"_enable_ban|{user_id}|{chat_id}",
                                )
                            ]
                        ]
                    hmm = await message.reply(
                        text, reply_markup=InlineKeyboardMarkup(btn)
                    )
                    await asyncio.sleep(10)
                    await hmm.delete()
    except:
        return
        




__MODULE__ = "Aɴᴛɪ Cʜᴀɴᴇᴇʟ"
__HELP__ = """
`your groups to stop anonymous channels sending messages into your chats.`

**Type of messages**
        ✗ document
        ✗ photo
        ✗ sticker
        ✗ animation
        ✗ video
        ✗ text
        
**Admin Commands:**
 ✗ /antichannel [on / off] - `Anti- channel  function`

**Note** - 'If linked_channel  send any containing characters in this type when on  function no del`  

**✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: Tᴇᴀᴍ DᴇCᴏᴅᴇ!**  
 """
__basic_cmds__ = __HELP__
