import html
import os
import json
import importlib
import time
import re
import sys
import traceback
import Yuriko.modules.sql.users_sql as sql
from sys import argv
from typing import Optional
from telegram import __version__ as peler
from platform import python_version as memek
from Yuriko import (
    ALLOW_EXCL,
    CERT_PATH,
    DONATION_LINK,
    LOGGER,
    OWNER_ID,
    PORT,
    SUPPORT_CHAT,
    TOKEN,
    URL,
    WEBHOOK,
    SUPPORT_CHAT,
    dispatcher,
    StartTime,
    telethn,
    pbot,
    updater,
)

# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from Yuriko.modules import ALL_MODULES
from Yuriko.modules.helper_funcs.chat_status import is_user_admin
from Yuriko.modules.helper_funcs.misc import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


LOVELY_MENU =  """
*👋 Hello {} !* there My name is *KIGO*.
I can help manage your groups with
useful features, feel free to add me to 
your groups!
"""

Lovelybuttons = [
     [
        InlineKeyboardButton(text="❔ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ❔", callback_data="lovelyx_"),
     ],
     [
        InlineKeyboardButton(text="ɪɴғᴏ&Aʙᴏᴜᴛ", callback_data="lovelyx_vko"),
     ],
     [  
        InlineKeyboardButton(text="🙋Uᴘᴅᴀᴛᴇ", url="https://t.me/kigo_omfo"),
        InlineKeyboardButton(text="👥Sᴜᴘᴘᴏʀᴛ", url="https://t.me/godzilla_chatting")
     ], 
     [
       InlineKeyboardButton(text="✨Aᴅᴅ ᴍᴇ✨", url="https://t.me/Kigo_omfobot?startgroup=true"),
     ],
]


LOVELYX_VIDAA = """https://telegra.ph/file/42cccf592372353af7c10.mp4"""


LOVELY_HELP = """
*✗ MAIN COMMANDS ✗*
✗ /start - `Starts me! Your probably already used this.`
✗ /help - `Click this I ll let you know about myself!`
✗ /settings - `in PM: will send you your settings for all supported modules.`
✗ *In A Group: Will Redirect You To Pm With All That Chats Settings.*)"""

LOVELY_BASICC = """This are some *Basic commands* which will help you to manage group easily by INNEXIA"""

LOVELY_ADVANCEE = """*Advanced commands*
Advanced commands will help you to secure your group easily and also you will know here some awesome features"""

LOVELY_EXTRA = """Fun tools and Extras
Extra tools which are available in bot and tools made for fun are here
You can choose an option below, by clicking a button.
For any query join @OmFoXD"""

DONATE_STRING = """Heya, glad to hear you want to donate!
 You can support the project by contacting @TUSHAR204 \
 Supporting isnt always financial! \
 Those who cannot provide monetary support are welcome to help us develop the bot at ."""

LOVELY_HELPX = """Hey there! My name is *INNEXIA 🔥*
*✗ MAIN COMMANDS ✗*
✗ /start - `Starts me! Your probably already used this.`
✗ /help - `Click this I ll let you know about myself!`
✗ /settings - `in PM: will send you your settings for all supported modules.`
✗ *In A Group: Will Redirect You To Pm With All That Chats Settings.*)"""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
LOVELY_BASIC = {}
LOVELY_ADVANCE = {}
LOVELY_TOOLS = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

LOVELY_CMDS =  [
       [
           InlineKeyboardButton(text="Basic", callback_data="lovelybasic_back"),           
           InlineKeyboardButton(text="Advanced", callback_data="lovelyadvance_back"),
       ],      
       [
           InlineKeyboardButton(text="Extra", callback_data="lovelytools_back"),
           InlineKeyboardButton(text="Inline", switch_inline_query_current_chat=""),
       ],
       [ 
           InlineKeyboardButton(text="All Commands", callback_data="help_back"),
           InlineKeyboardButton(text="Main menu", callback_data="lovelyx_back"),
       ],
]

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("Yuriko.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__lovely_basic__") and imported_module.__lovely_basic__:
        LOVELY_BASIC[imported_module.__mod_name__.lower()] = imported_module
 
    if hasattr(imported_module, "__lovely_advance__") and imported_module.__lovely_advance__:
        LOVELY_ADVANCE[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__lovely_tools__") and imported_module.__lovely_tools__:
        LOVELY_TOOLS[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module



# do not async
def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    dispatcher.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=keyboard,
    )


def test(update: Update, context: CallbackContext):
    # pprint(eval(str(update)))
    # update.effective_message.reply_text("Hola tester! _I_ *have* `markdown`", parse_mode=ParseMode.MARKDOWN)
    update.effective_message.reply_text("This person edited a message")
    print(update.effective_message)


def start(update: Update, context: CallbackContext):
    args = context.args
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, LOVELY_HELP)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="Go Back", callback_data="help_back")]]
                    ),
                )

            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            update.effective_message.reply_text(
                LOVELY_MENU.format(
                    escape_markdown(first_name),
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),                        
                reply_markup=InlineKeyboardMarkup(Lovelybuttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
            )
    else:
        update.effective_message.reply_text(
            "KIGO is alive use below buttons to explore my features in group or pm!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Open in private chat",
                            url="t.me/{}?start".format(context.bot.username),
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="Explore here", callback_data="lovelyx_back"
                        ),
                    ],
                ]
            ),
        )

def error_handler(update, context):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    LOGGER.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    message = (
        "An exception was raised while handling an update\n"
        "<pre>update = {}</pre>\n\n"
        "<pre>{}</pre>"
    ).format(
        html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False)),
        html.escape(tb),
    )

    if len(message) >= 4096:
        message = message[:4096]
    # Finally, send the message
    context.bot.send_message(chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML)


# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors


def help_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "Here is the help for the *{}* module:\n".format(
                    HELPABLE[module].__mod_name__
                )
                + HELPABLE[module].__help__
            )
            query.message.edit_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text="Updates", url="https://t.me/kigo_omfo"), InlineKeyboardButton(text="Support", url="https://t.me/godzilla_chatting")],
                    [InlineKeyboardButton(text="Go back", callback_data="help_back"), InlineKeyboardButton(text="Add KIGO", url="https://t.me/Kigo_omfobot?startgroup=true")]
                  ]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.edit_text(
                text=LOVELY_HELP,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, HELPABLE, "help")
                ),
            )

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.edit_text(
                text=LOVELY_HELP,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, HELPABLE, "help")
                ),
            )

        elif back_match:
            query.message.edit_text(
                text=LOVELY_HELP,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")
                ),
            )

        # ensure no spinny white circle
        context.bot.answer_callback_query(query.id)
        # query.message.delete()

    except BadRequest:
        pass

def lovelybasic_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"lovelybasic_module\((.+?)\)", query.data)
    prev_match = re.match(r"lovelybasic_prev\((.+?)\)", query.data)
    next_match = re.match(r"lovelybasic_next\((.+?)\)", query.data)
    back_match = re.match(r"lovelybasic_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "Here is the help for the *{}* module:\n".format(
                    LOVELY_BASIC[module].__mod_name__
                )
                + LOVELY_BASIC[module].__lovely_basic__
            )
            query.message.edit_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text="Updates", url="https://t.me/kigo_omfo"), InlineKeyboardButton(text="Support", url="https://t.me/godzilla_chatting")],
                    [InlineKeyboardButton(text="Go back", callback_data="lovelybasic_back"), InlineKeyboardButton(text="Add KIGO", url="https://t.me/Kigo_omfobot?startgroup=true")]
                  ]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.edit_text(
                text=LOVELY_BASICC,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, LOVELY_BASIC, "lovelybasic")
                ),
            )

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.edit_text(
                text=LOVELY_BASICC,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, LOVELY_BASIC, "lovelybasic")
                ),
            )

        elif back_match:
            query.message.edit_text(
                text=LOVELY_BASICC,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, LOVELY_BASIC, "lovelybasic")
                ),
            )

    except BadRequest:
        pass

def lovelyadvance_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"lovelyadvance_module\((.+?)\)", query.data)
    prev_match = re.match(r"lovelyadvance_prev\((.+?)\)", query.data)
    next_match = re.match(r"lovelyadvance_next\((.+?)\)", query.data)
    back_match = re.match(r"lovelyadvance_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "Here is the help for the *{}* module:\n".format(
                    LOVELY_ADVANCE[module].__mod_name__
                )
                + LOVELY_ADVANCE[module].__lovely_advance__
            )
            query.message.edit_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text="Updates", url="https://t.me/kigo_omfo"), InlineKeyboardButton(text="Support", url="https://t.me/godzilla_chatting")],
                    [InlineKeyboardButton(text="Go back", callback_data="lovelyadvance_back"), InlineKeyboardButton(text="Add KIGO", url="https://t.me/Kigo_omfobot?startgroup=true")]
                  ]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.edit_text(
                text=LOVELY_ADVANCEE,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, LOVELY_ADVANCE, "lovelyadvance")
                ),
            )

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.edit_text(
                text=LOVELY_ADVANCEE,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, LOVELY_ADVANCE, "lovelyadvance")
                ),
            )

        elif back_match:
            query.message.edit_text(
                text=LOVELY_ADVANCEE,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, LOVELY_ADVANCE, "lovelyadvance")
                ),
            )

    except BadRequest:
        pass
def lovelytools_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"lovelytools_module\((.+?)\)", query.data)
    prev_match = re.match(r"lovelytools_prev\((.+?)\)", query.data)
    next_match = re.match(r"lovelytools_next\((.+?)\)", query.data)
    back_match = re.match(r"lovelytools_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "Here is the help for the *{}* module:\n".format(
                    LOVELY_TOOLS[module].__mod_name__
                )
                + LOVELY_TOOLS[module].__lovely_tools__
            )
            query.message.edit_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text="Updates", url="https://t.me/kigo_omfo"), InlineKeyboardButton(text="Support", url="https://t.me/godzilla_chatting")],
                    [InlineKeyboardButton(text="Go back", callback_data="lovelytools_back"), InlineKeyboardButton(text="Add KIGO", url="https://t.me/Kigo_omfobot?startgroup=true")]
                  ]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.edit_text(
                text=LOVELY_EXTRA,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, LOVELY_TOOLS, "lovelytools")
                ),
            )

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.edit_text(
                text=LOVELY_EXTRA,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, LOVELY_TOOLS, "lovelytools")
                ),
            )

        elif back_match:
            query.message.edit_text(
                text=LOVELY_EXTRA,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, LOVELY_TOOLS, "lovelytools")
                ),
            )

    except BadRequest:
        pass

def lovelyx_about_callback(update, context):
    query = update.callback_query
    if query.data == "lovelyx_":
        query.message.edit_text(
            text=LOVELY_HELPX,
        parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                LOVELY_CMDS
            ),
        )
    elif query.data == "lovelyx_back":
        first_name = update.effective_user.first_name
        uptime = get_readable_time((time.time() - StartTime))
        query.message.edit_text(
                LOVELY_MENU.format(
                    escape_markdown(first_name),
                    escape_markdown(uptime),
                    sql.num_users(),
                    sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(Lovelybuttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )

    elif query.data == "lovelyx_tutorials":
        query.message.reply_text(
            text="Hi I'm KIGO, one of the fastest and most features for your groups"
                 "\n\nYou can also Play Music groups by using me!",
        parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="🔥Add me to Group🔥", url="https://t.me/Kigo_omfobot?startgroup=true"),
                 ],
                 [
                    InlineKeyboardButton(text="Video Tutorial", callback_data="lovelyx_vid"),
                 ],
                 [
                    InlineKeyboardButton(text="☜︎︎︎ Back", callback_data="lovelyx_vko"),
                    InlineKeyboardButton(text="Next ☞︎︎︎", callback_data="lovelyx_pro"),
                 ]
                ]
            ),
        )
        query.message.delete()
        
    elif query.data == "lovelyx_pro":
        query.message.edit_text(
            text="""<b>Hey, Welcome to Lovely configuration Tutorial
Before we go, I need admin permissions in this chat to work properly
1) Click Manage Group
2) Go to Administrators and add</b> @innexiaBot <b>as Admin
3) Giving full permissions make Lovely fully useful</b>""",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
              [[InlineKeyboardButton(text="previous", callback_data="lovelyx_tutorials"),
                InlineKeyboardButton(text="next", callback_data="lovelyx_help")],               
              ]
            ),
        )

    elif query.data == "lovelyx_help":
        query.message.edit_text(
            text="""*Let's make your group bit effective now
Congragulations, Lovely now ready to manage your group
Here are some essentialt to try on
✗ Admin tools
Basic Admin tools help you to protect and powerup your group
You can ban members, Kick members, Promote someone as admin through commands of bot
✗ Welcomes
Lets set a welcome message to welcome new users coming to your group
send* /setwelcome *[message] to set a welcome message
Also you can Stop entering robots or spammers to your chat by setting welcome captcha 
Refer Help menu to see everything in detail*""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
              [
                [InlineKeyboardButton(text="previous", callback_data="lovelyx_pro"),
                 InlineKeyboardButton(text="next", callback_data="lovelyx_helpc")]
                ]
            ),
        )

    elif query.data == "lovelyx_helpc":
        query.message.edit_text(
            text="""✗ *Filters*
Filters can be used as automated replies/ban/delete when someone use a word or sentence
For Example if I filter word 'hello' and set reply as 'hi'
Bot will reply as 'hi' when someone say 'hello'
You can add filters by sending /filter [filter name]
✗ *AI Chatbot*
Want someone to chat in group?
INNEXIA has an intelligent chatbot with multilang support
Let's try it,
Send /chatbot on and reply to any of my messages to see the magic""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
              [
                [InlineKeyboardButton(text="previous", callback_data="lovelyx_helpb"),
                 InlineKeyboardButton(text="next", callback_data="lovelyx_helpd")]
                ]
            ),
        )
    elif query.data == "lovelyx_helpd":
        query.message.edit_text(
            text="""✗ *Setting up Notes*
You can save message/media/audio or anything as notes
to get a note simply use # at the beginning of a word
See the image..
You can also set buttons for notes and filters (refer help menu)
✗ *Setting up NightMode*
You can set up NightMode Using /nightmode on/off command.
Note- Night Mode chats get Automatically closed at 12pm(IST)
and Automatically openned at 6am(IST) To Prevent Night Spams.""",
         parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
              [
                [InlineKeyboardButton(text="previous", callback_data="lovelyx_helpc"),
                 InlineKeyboardButton(text="next", callback_data="lovelyx_helpe")]
                ]
            ),
        )
    elif query.data == "lovelyx_term":
        query.message.edit_text(
            text="""✗ *Terms and Conditions:*
- Only your first name, last name (if any) and username (if any) is stored for a convenient communication!
- No group ID or it's messages are stored, we respect everyone's privacy.
- Messages between Bot and you is only infront of your eyes and there is no backuse of it.
- Watch your group, if someone is spamming your group, you can use the report feature of your Telegram Client.
- Do not spam commands, buttons, or anything in bot PM.
*NOTE:* Terms and Conditions might change anytime
*Updates Channel:* @kigo_omfo
*Support Chat:* @godzilla_chatting""",
          parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[
                InlineKeyboardButton(text="Back", callback_data="about_")]]
            ),
        )
    elif query.data == "lovelyx_helpe":
        query.message.edit_text(
            text="""So now you are at the end of basic tour. But this is not all I can do.
Send /help in bot pm to access help menu
There are many handy tools to try out. 
And also if you have any suggessions about me, Don't forget to tell them to devs
Again thanks for using me
✗ By using @Kigo_omfobot you are agreed to our terms & conditions""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Help", callback_data="lovelyx_")],
                [InlineKeyboardButton(text="back", callback_data="lovelyx_helpd"),
                InlineKeyboardButton(text="Main menu", callback_data="lovelyx_tutorials")]]
            ),
    
        )
    
    elif query.data == "lovelyx_vida":
        query.message.reply_video(
            LOVELYX_VIDAA, caption=""" Hey, Welcome to KIGO configuration Tutorial
Before we go, I need admin permissions in this chat to work properly
1) Click Manage Group
2) Goto Administrators and add @Kigo_omfobot as Admin
3) Giving full permissions make KIGO fully useful""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Back", callback_data="lovelyx_tutorials")]]
            ),             
        ) 
        query.message.delete() 
    
    elif query.data == "lovelyx_vko":
        query.message.reply_text(
            text=""" info & About

In here you can find what is KIGO and how to set her up

Click buttons for help""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Hᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ", callback_data="lovelyx_tutorials")],
                [InlineKeyboardButton(text="ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="lovelyx_umm"),
                InlineKeyboardButton(text="☜︎︎︎ Bᴀᴄᴋ", callback_data="lovelyx_back")]]
            ),
        )

    elif query.data == "lovelyx_umm":
        query.message.edit_text(
            text="""Soon""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Back", callback_data="lovelyx_vko")]]
            ),
        )
    
    elif query.data == "lovelyx_vid":
        query.message.reply_video(
            LOVELYX_VIDAA, caption=""" Hey, Welcome to KIGO configuration Tutorial
Before we go, I need admin permissions in this chat to work properly
1) Click Manage Group
2) Goto Administrators and add @Kigo_omfobot as Admin
3) Giving full permissions make KIGO fully useful""",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Back", callback_data="lovelyx_tutorials")]]
            ),             
        ) 
        query.message.delete()    
                  
#🤣🤣🤣🤣

def get_basic(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in LOVELY_BASIC):
            module = args[1].lower()
            update.effective_message.reply_text(
                f"Contact me in PM to get help of {module.capitalize()}",
                reply_markup=None,
      )
            return
        update.effective_message.reply_text(
            "Use below buttons to explore features or to close menu",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Basic commands", callback_data="lovelybasic_back"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="Close menu", callback_data="stngs_back"
                        ),
                    ],               
                ]
            ),
        )


def get_advance(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in LOVELY_ADVANCE):
            module = args[1].lower()
            update.effective_message.reply_text(
                f"Contact me in PM to get help of {module.capitalize()}",
                reply_markup=None,
      )
            return
        update.effective_message.reply_text(
            "Use below buttons to explore features or to close menu",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Advance commands", callback_data="lovelyadvance_back"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="Close menu", callback_data="stngs_back"
                        ),
                    ],               
                ]
            ),
        )

def get_tools(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in LOVELY_TOOLS):
            module = args[1].lower()
            update.effective_message.reply_text(
                f"Contact me in PM to get help of {module.capitalize()}",
                reply_markup=None,
      )
            return
        update.effective_message.reply_text(
            "Use below buttons to explore features or to close menu",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Extra commands", callback_data="lovelytools_back"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="Close menu", callback_data="stngs_back"
                        ),
                    ],               
                ]
            ),
        )            

def get_help(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
            module = args[1].lower()
            update.effective_message.reply_text(
                f"Contact me in PM to get help of {module.capitalize()}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Help",
                                url="t.me/{}?start=ghelp_{}".format(
                                    context.bot.username, module
                                ),
                            )
                        ]
                    ]
                ),
            )

            return
        update.effective_message.reply_text(
            "Use below buttons to explore my awesome features in pm or group.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Open in private chat",
                            url="t.me/{}?start=help".format(context.bot.username),
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="Open here", callback_data="help_back"
                        ),
                    ],
                ]
            ),
        )
        return

    elif len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        text = (
            "Here is the available help for the *{}* module:\n".format(
                HELPABLE[module].__mod_name__
            )
            + HELPABLE[module].__help__
        )
        send_help(
            chat.id,
            text,
            InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Go Back", callback_data="help_back")]]
            ),
        )

    else:
        send_help(chat.id, LOVELY_HELP)


def send_settings(chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join(
                "*{}*:\n{}".format(mod.__mod_name__, mod.__user_settings__(user_id))
                for mod in USER_SETTINGS.values()
            )
            dispatcher.bot.send_message(
                user_id,
                "These are your current settings:" + "\n\n" + settings,
                parse_mode=ParseMode.MARKDOWN,
            )

        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any user specific settings available :'(",
                parse_mode=ParseMode.MARKDOWN,
            )

    else:
        if CHAT_SETTINGS:
            chat_name = dispatcher.bot.getChat(chat_id).title
            dispatcher.bot.send_message(
                user_id,
                text="Which module would you like to check {}'s settings for?".format(
                    chat_name
                ),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )
        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any chat settings available :'(\nSend this "
                "in a group chat you're admin in to find its current settings!",
                parse_mode=ParseMode.MARKDOWN,
            )


def settings_button(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user
    bot = context.bot
    mod_match = re.match(r"stngs_module\((.+?),(.+?)\)", query.data)
    prev_match = re.match(r"stngs_prev\((.+?),(.+?)\)", query.data)
    next_match = re.match(r"stngs_next\((.+?),(.+?)\)", query.data)
    back_match = re.match(r"stngs_back\((.+?)\)", query.data)
    try:
        if mod_match:
            chat_id = mod_match.group(1)
            module = mod_match.group(2)
            chat = bot.get_chat(chat_id)
            text = "*{}* has the following settings for the *{}* module:\n\n".format(
                escape_markdown(chat.title), CHAT_SETTINGS[module].__mod_name__
            ) + CHAT_SETTINGS[module].__chat_settings__(chat_id, user.id)
            query.message.reply_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Go Back",
                                callback_data="stngs_back({})".format(chat_id),
                            )
                        ]
                    ]
                ),
            )

        elif prev_match:
            chat_id = prev_match.group(1)
            curr_page = int(prev_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                "Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        curr_page - 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif next_match:
            chat_id = next_match.group(1)
            next_page = int(next_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                "Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        next_page + 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif back_match:
            chat_id = back_match.group(1)
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                text="Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(escape_markdown(chat.title)),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )

        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
        query.message.delete()
    except BadRequest as excp:
        if excp.message not in [
            "Message is not modified",
            "Query_id_invalid",
            "Message can't be deleted",
        ]:
            LOGGER.exception("Exception in settings buttons. %s", str(query.data))


def get_settings(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]

    # ONLY send settings in PM
    if chat.type != chat.PRIVATE:
        if is_user_admin(chat, user.id):
            text = "Click here to get this chat's settings, as well as yours."
            msg.reply_text(
                text,
                reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Open in private chat",
                                url="t.me/{}?start=stngs_{}".format(
                                    context.bot.username, chat.id)
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                           text="Close", callback_data="stngs_back"
                        ),
                    ]
                ]
            ),
        )
        else:
            text = "Click here to check your settings."

    else:
        send_settings(chat.id, user.id, True)

def donate(update: Update, context: CallbackContext):
    user = update.effective_message.from_user
    chat = update.effective_chat  # type: Optional[Chat]
    bot = context.bot
    if chat.type == "private":
        update.effective_message.reply_text(
            DONATE_STRING, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )

        if OWNER_ID != 1920507972:
            update.effective_message.reply_text(
                "I'm free for everyone ❤️ If you wanna make me smile, just join"
                "[My Channel]({})".format(DONATION_LINK),
                parse_mode=ParseMode.MARKDOWN,
            )
    else:
        try:
            bot.send_message(
                user.id,
                DONATE_STRING,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
            )

            update.effective_message.reply_text(
                "I've PM'ed you about donating to my creator!"
            )
        except Unauthorized:
            update.effective_message.reply_text(
                "Contact me in PM first to get donation information."
            )


def migrate_chats(update: Update, context: CallbackContext):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGGER.info("Successfully migrated!")
    raise DispatcherHandlerStop


def main():

    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.sendMessage(
                f"@{SUPPORT_CHAT}", 
                f"""**lee baji 🔥🙂**

**Python:** `{memek()}`
**Telegram Library:** `v{peler}`""",
                parse_mode=ParseMode.MARKDOWN
            )
        except Unauthorized:
            LOGGER.warning(
                "Bot isnt able to send message to support_chat, go and check!"
            )
        except BadRequest as e:
            LOGGER.warning(e.message)

    test_handler = CommandHandler("test", test, run_async=True)
    start_handler = CommandHandler("start", start, run_async=True)

    help_handler = CommandHandler("help", get_help, run_async=True)
    help_callback_handler = CallbackQueryHandler(
        help_button, pattern=r"help_.*", run_async=True
    )

    lovelybasic_handler = CommandHandler("lovelybasic", get_basic, run_async=True)
    lovelybasic_callback_handler = CallbackQueryHandler(
        lovelybasic_button, pattern=r"lovelybasic_.*", run_async=True
    )

    lovelyadvance_handler = CommandHandler("lovelyadvance", get_advance, run_async=True)
    lovelyadvance_callback_handler = CallbackQueryHandler(
        lovelyadvance_button, pattern=r"lovelyadvance_.*", run_async=True
    )

    lovelytools_handler = CommandHandler("lovelytools", get_tools, run_async=True)
    lovelytools_callback_handler = CallbackQueryHandler(
        lovelytools_button, pattern=r"lovelytools_.*", run_async=True
    )

    settings_handler = CommandHandler("settings", get_settings, run_async=True)
    settings_callback_handler = CallbackQueryHandler(
        settings_button, pattern=r"stngs_", run_async=True
    )


    lovelyx_callback_handler = CallbackQueryHandler(
        lovelyx_about_callback, pattern=r"lovelyx_", run_async=True
    )

    donate_handler = CommandHandler("donate", donate, run_async=True)
    migrate_handler = MessageHandler(
        Filters.status_update.migrate, migrate_chats, run_async=True
    )

    dispatcher.add_handler(test_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(lovelybasic_handler)
    dispatcher.add_handler(lovelyadvance_handler)
    dispatcher.add_handler(lovelytools_handler)
    dispatcher.add_handler(lovelyx_callback_handler)
    dispatcher.add_handler(settings_handler)
    dispatcher.add_handler(help_callback_handler)
    dispatcher.add_handler(lovelybasic_callback_handler)
    dispatcher.add_handler(lovelyadvance_callback_handler)
    dispatcher.add_handler(lovelytools_callback_handler)
    dispatcher.add_handler(settings_callback_handler)
    dispatcher.add_handler(migrate_handler)
    dispatcher.add_handler(donate_handler)

    dispatcher.add_error_handler(error_callback)

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN, certificate=open(CERT_PATH, "rb"))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)

    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    pbot.start()
    main()
