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

 
def alicia_sticker_callback(update, context):
    query = update.callback_query
    if query.data == "aliciasticker_":
        query.message.edit_text(
            text="""Here is the help for the *Quote* module:

We not promise to update KIGO PERDAY

✗ /q <reply to text> - `create quote`

✗ /qr <reply to text> - `Create quote with reply message sur` 

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

 
def alicia_sticker_memify_callback(update, context):
    query = update.callback_query
    if query.data == "aliciastickermemify_":
        query.message.edit_text(
            text=""" Here is the help for the *old-quote* module:

KIGO Is Always Try Something this is old-quote
 
✗ /sq <reply to text> - `Create simple boy like  q`

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

sticker_callback_handler = CallbackQueryHandler(alicia_sticker_callback, pattern=r"aliciasticker_", run_async=True)
sticker_memify_callback_handler = CallbackQueryHandler(alicia_sticker_memify_callback, pattern=r"aliciastickermemify_", run_async=True)






