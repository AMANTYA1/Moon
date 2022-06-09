from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from Yuriko.__main__ import *


# Buttons Function for fun module
LogoXd = """https://telegra.ph/file/c69a68148cf09661549f5.jpg"""

def alicia_fun_callback(update, context):
    query = update.callback_query
    if query.data == "aliciafun_":
        query.message.reply_photo(
            Logoxd, caption=""" Here is the help for the *Logo* module:

✗ /logo - `<text/name> Create a logo with your name`

✗ /logo Null ; Robot :  use ; for write in next line

**✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ**  
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        )
        query.message.delete()


def alicia_fun_emoji_callback(update, context):
    query = update.callback_query
    if query.data == "aliciafunemoji_":
        query.message.edit_text(
            text=""" Here is the help for the *Simple-logo* module:

✗ /slogo - `<text/name> Create a simple logo with random view.`

✗ /wlogo - `<text/name> Create a logo with wide view only.`

**✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ**
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        )


def alicia_fun_games_callback(update, context):
    query = update.callback_query
    if query.data == "aliciafungames_":
        query.message.edit_text(
            text=""" Here is the help for the *Glogo* module:

✗ /glogo - ` <text/name>  Create a logo with photo girls.

**✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ**
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        )



def alicia_fun_couple_callback(update, context):
    query = update.callback_query
    if query.data == "aliciafuncouple_":
        query.message.edit_text(
            text=""" Here is the help for the *Couples* module:

✗ /write - `Any text to make write logo.`

**✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ**
               """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_back")
                 ]
                ]
            ),
        )






# Handlers start from here 

fun_callback_handler = CallbackQueryHandler(alicia_fun_callback, pattern=r"aliciafun_", run_async=True)
fun_emoji_callback_handler = CallbackQueryHandler(alicia_fun_emoji_callback, pattern=r"aliciafunemoji_", run_async=True)
fun_games_callback_handler = CallbackQueryHandler(alicia_fun_games_callback, pattern=r"aliciafungames_", run_async=True)
fun_couple_callback_handler = CallbackQueryHandler(alicia_fun_couple_callback, pattern=r"aliciafuncouple_", run_async=True)





