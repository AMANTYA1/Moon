from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telethon.tl.types import InputMediaDice

from Yuriko.events import register
from Yuriko.button.game import *

@register(pattern="^/dice(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice(""))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(""))
        except BaseException:
            pass


@register(pattern="^/dart(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("🎯"))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎯"))
        except BaseException:
            pass


@register(pattern="^/ball(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("🏀"))
    input_int = int(input_str)
    if input_int > 5:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🏀"))
        except BaseException:
            pass

__mod_name__ = "Gᴀᴍᴇs"

__help__ = """
𖣘 Hᴇʜᴇ Gᴜʏs Sᴏᴍᴇ Gᴀᴍᴅ ʙʏ Kɪɢᴏ 
Nᴏᴛ Lɪᴋᴇ BGᴍɪ

👇Gᴀᴍᴇ        👇A-Gᴀᴍᴇ
"""
__button__ = [ InlineKeyboardButton(text="Gᴀᴍᴇ", callback_data="nullgame_"),
            InlineKeyboardButton(text="A-Gᴀᴍᴇ", callback_data="gamexd_"),
            

] 
__buttons__ = []

__lovely_tools__ = __help__

dispatcher.add_handler(game_callback_handler)
dispatcher.add_handler(game_memify_callback_handler)
