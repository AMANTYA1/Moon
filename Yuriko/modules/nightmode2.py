# ---------- NIGHTMODE v2.0 ----------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------- NIGHTMODE v2.0 ------------------------------------------------------------------
# ---------- NIGHTMODE v2.0 ----------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------- NIGHTMODE v2.0 ------------------------------------------------------------------

import asyncio
from datetime import timedelta

import dateparser
from pymongo import MongoClient
from pyrogram import filters
from pyrogram.types import ChatPermissions

from Yuriko.config import get_str_key
from Yuriko import pbot

MONGO_DB_URI = get_str_key("MONGO_DB_URI")

# Setting Up Mongo 🤣
client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["daisyxbot"]
nightmod = db.nightmode3


def get_info(id):
    return nightmod.find_one({"id": id})


@pbot.on_message(filters.command(["setnightmode"]))
async def customize_night(_, message):

    lol = await message.reply("Processing...")

    if message.chat.type == "private":
        return await lol.edit("**You can set nightmode only in groups :(**")

    if message.chat.type == "channel":
        return

    else:
        if len(message.command) != 2:
            return await lol.edit("Give other parameters too 👀")

        parameter = message.text.split(None, 1)[1]

        if "|" in parameter:
            zone, ctime, otime = parameter.split("|")

        else:
            return await lol.edit("Invalid Syntax..!")

        zone = zone.strip()
        ctime = ctime.strip()
        otime = otime.strip()

        if len(ctime) != 11:
            return await lol.edit("Please enter valid date and time...!")

        if len(otime) != 11:
            return await lol.edit("Please enter valid date and time...!")

        if not zone and ctime and otime:
            return await lol.edit("Missing some parameters.!")

        ttime = dateparser.parse(
            "now", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "YMD"}
        )

        if ttime is None or otime is None or ctime is None:
            return await lol.edit("Please enter valid `date`, `time` & `zone`")

        cctime = dateparser.parse(
            f"{ctime}", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "DMY"}
        ) + timedelta(days=1)

        ootime = dateparser.parse(
            f"{otime}", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "DMY"}
        ) + timedelta(days=1)

        if cctime == ootime:
            return await lol.edit("Chat opening and closing time can not be same..!")

        if not ootime > cctime and not cctime < ootime:
            return await lol.edit("Chat opening time must be greater than closing time")

        if cctime > ootime:
            return await lol.edit(
                "Chat closing time can't be greater than opening time"
            )

        chats = nightmod.find({})
        for c in chats:
            if message.chat.id == c["id"] and c["valid"] is True:
                to_check = get_info(id=message.chat.id)
                nightmod.update_one(
                    {
                        "_id": to_check["_id"],
                        "id": to_check["id"],
                        "valid": to_check["valid"],
                        "zone": to_check["zone"],
                        "ctime": to_check["ctime"],
                        "otime": to_check["otime"],
                    },
                    {"$set": {"zone": zone, "ctime": cctime, "otime": ootime}},
                )
                await lol.edit(
                    "**Nightmode already set**\n\n__I am updating the zone, closing time and opening time with the new zone, closing time and opening time__"
                )
                await asyncio.sleep(5)
                return await lol.edit(
                    f"**Nightmode Updated Successfully in {message.chat.title} chat**"
                )
        nightmod.insert_one(
            {
                "id": message.chat.id,
                "valid": True,
                "zone": zone,
                "ctime": cctime,
                "otime": ootime,
            }
        )
        await lol.edit(f"**Nightmode set successfully in {message.chat.title} chat !**")


@pbot.on_message(filters.incoming & ~filters.edited)
async def night_mode(client, message):
    try:
        if not message:
            return message.continue_propagation()
        if not message.from_user:
            return message.continue_propagation()

        chats = nightmod.find({})

        for c in chats:
            id = c["id"]
            valid = c["valid"]
            zone = c["zone"]
            c["ctime"]
            otime = c["otime"]
            present = dateparser.parse(
                "now", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "YMD"}
            )
            try:
                if present > otime and valid:
                    newtime = otime + timedelta(days=1)
                    to_check = get_info(id=id)
                    if not to_check:
                        return message.continue_propagation()
                    if not newtime:
                        return message.continue_propagation()
                    nightmod.update_one(
                        {
                            "_id": to_check["_id"],
                            "id": to_check["id"],
                            "valid": to_check["valid"],
                            "zone": to_check["zone"],
                            "ctime": to_check["ctime"],
                            "otime": to_check["otime"],
                        },
                        {"$set": {"otime": newtime}},
                    )

                    sed = await client.send_message(
                        id,
                        "🌗 Night Mode Ending :)\n\n `Chat Opening...`",
                    )
                    await client.set_chat_permissions(
                        id,
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_stickers=True,
                            can_send_animations=True,
                        ),
                    )

                    await sed.edit(
                        "**🌗Night Mode Ended**\n\n`Chat opened`: __EveryOne Should Be Able To Send Messages__\n\n**Powered by @Mr_Shadow_Robot**"
                    )
                    message.continue_propagation()
                    break
                    return message.continue_propagation()
            except:
                print("Chat open error in nightbot")
                return message.continue_propagation()
            continue

        chats = nightmod.find({})

        for c in chats:
            id = c["id"]
            valid = c["valid"]
            zone = c["zone"]
            ctime = c["ctime"]
            c["otime"]
            c["otime"]
            present = dateparser.parse(
                "now", settings={"TIMEZONE": f"{zone}", "DATE_ORDER": "YMD"}
            )
            try:
                if present > ctime and valid:
                    newtime = ctime + timedelta(days=1)
                    to_check = get_info(id=id)

                    if not to_check:
                        return message.continue_propagation()
                    if not newtime:
                        return message.continue_propagation()

                    nightmod.update_one(
                        {
                            "_id": to_check["_id"],
                            "id": to_check["id"],
                            "valid": to_check["valid"],
                            "zone": to_check["zone"],
                            "ctime": to_check["ctime"],
                            "otime": to_check["otime"],
                        },
                        {"$set": {"ctime": newtime}},
                    )
                    sed = await client.send_message(
                        id,
                        "🌗 Night Mode Starting :)\n\n`Chat closing...`",
                    )
                    await client.set_chat_permissions(
                        id,
                        ChatPermissions(
                            can_send_messages=False,
                        ),
                    )
                    await sed.edit(
                        "**🌗Night Mode Started**\n\n `Chat close initiated`: __Only Admins Should Be Able To Send Messages__\n\n**Powered by @Mr_Shadow_Robot**"
                    )
                    message.continue_propagation()
                    break
                    return message.continue_propagation()
            except:
                print("Chat close error")
                return message.continue_propagation()
            continue
        return message.continue_propagation()
    except:
        return


# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------

 __mod_name__ = "Night Mode"

__help__ =
"""
<b>The Night Mode</b>

Tired managing group all time
Close your group at at a given time and open back at a given time

<b>Available Commands</b>
- /nightmode [ON/OFF]: Enable/Disable Night Mode (Default settings*)
- /setnightmode [TIME ZONE] | [Start time] | [End time]: Set nightmode (See example)

<u>Example:</u>
- /setnightmode Asia/kolkata | 01:30:00 AM | 02:35:00 AM
    
<i>Note: Remember chat permissions messages,gifs,games,inline,invites will be allowed when opening chat</i>

*Default settings: Close your group at 12.00 AM. and open back at 6.00 AM.(IST)
"""
