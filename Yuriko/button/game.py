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


# Buttons Function for admin module

 
def kigo_sticker_callback(update, context):
    query = update.callback_query
    if query.data == "aliciasticker_":
        query.message.edit_text(
            text="""Here is the help for the *Game* module:

We not promise to update KIGO PERDAY

✗ /game - `to play gane in chrome and other idk k`

**✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ!**
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

 
def kigo_sticker_memify_callback(update, context):
    query = update.callback_query
    if query.data == "aliciastickermemify_":
        query.message.edit_text(
            text=""" Here is the help for the *A-game* module:

**✗ A-Game Module For play Animation game in group**
 
✗ /dice - `dice game`
✗ /dart - `dart gane`
✗ /ball - `to play ball game`

**✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ!**""",
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

sticker_callback_handler = CallbackQueryHandler(kigo_sticker_callback, pattern=r"kigosticker_", run_async=True)
sticker_memify_callback_handler = CallbackQueryHandler(kigo_sticker_memify_callback, pattern=r"kigostickermemify_", run_async=True)






