#  Full credits to

#  II    N    N    U   U    K   K      A
#  II    N N  N    U   U    K K       A A
#  II    N  N N    U   U    K K      A A A
#  II    N    N     U U     K   K   A     A


from pymongo import MongoClient
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Yuriko.confing import get_str_key
from Yuriko import pbot

MONGO_DB_URI = get_str_key("MONGO_URI")
client = MongoClient(MONGO_DB_URI)
dbd = client["missjuliarobot"]
approved_users = dbd.approve
db = dbd
tagdb = db.tagdb1


@pbot.on_message(filters.command(["tagalert"]) & filters.private)
async def locks_dfunc(_, message):
    lol = await message.reply("Processing..")
    if len(message.command) != 2:
        return await lol.edit("Expected on or off 👀")
    parameter = message.text.strip().split(None, 1)[1].lower()

    if parameter == "on" or parameter == "ON":
        if not message.from_user:
            return
        if not message.from_user.username:
            return await lol.edit(
                "Only users with usernames are eligible for tag alert service. Sorry :("
            )
        uname = str(message.from_user.username)
        uname = uname.lower()
        isittrue = tagdb.find_one({f"teg": uname})
        if not isittrue:
            tagdb.insert_one({f"teg": uname})
            return await lol.edit(
                f"🔔 **--Tag alerts enabled--**\n\nWhen someone tags you as @{uname} you will be notified"
            )
        else:
            return await lol.edit("Tag alerts already enabled for you :)")
    if parameter == "off" or parameter == "OFF":
        if not message.from_user:
            return
        if not message.from_user.username:
            return await lol.edit(
                "Only users with usernames are eligible for tag alert service. Sorry :("
            )
        uname = message.from_user.username
        uname = uname.lower()
        isittrue = tagdb.find_one({f"teg": uname})
        if isittrue:
            tagdb.delete_one({f"teg": uname})
            return await lol.edit("Tag alerts removed")
        else:
            return await lol.edit("Tag alerts already disabled for you")
    else:
        await lol.edit("I only recognize on & off 👀")


@pbot.on_message(filters.incoming & ~filters.edited)
async def mentioned_alert(client, message):
    try:
        if not message:
            message.continue_propagation()
            return
        if not message.from_user:
            message.continue_propagation()
            return
        input_str = message.text
        input_str = input_str.lower()
        if "@" in input_str:

            input_str = input_str.replace("@", "  |")
            inuka = input_str.split("|")[1]
            text = inuka.split()[0]
        else:
            return message.continue_propagation()
        if tagdb.find_one({f"teg": text}):
            pass
        else:
            return message.continue_propagation()
        try:
            chat_name = message.chat.title
            message.chat.id
            tagged_msg_link = message.link
        except:
            return message.continue_propagation()
        user_ = message.from_user.mention or f"@{message.from_user.username}"

        final_tagged_msg = f"**--🔔 You Have Been Tagged--**\n\n**Group:** {chat_name}\n**By user:** {user_}\n**Message:** [Here]({tagged_msg_link})"
        button_s = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔔 View Message 🔔", url=tagged_msg_link)]]
        )
        try:
            await client.send_message(
                chat_id=f"{text}",
                text=final_tagged_msg,
                reply_markup=button_s,
                disable_web_page_preview=True,
            )

        except:
            return message.continue_propagation()
        message.continue_propagation()
    except:
        return message.continue_propagation()
