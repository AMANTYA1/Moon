import re
from pyrogram.types import (
  ChatPermissions, 
  InlineKeyboardButton,
  InlineKeyboardMarkup, 
  Message, 
  User, 
  InputMediaAnimation
)
from pyrogram import filters
from Yuriko import telethn as client
from Yuriko.function.pluginhelpers import member_permissions
from Yuriko import BOT_ID

from Yuriko.modules.resources.messages import Messages as MSG
from Yuriko.modules.resources.buttons import Buttons as BTN


welcome_captcha_group = 6
@Client.on_message(filters.new_chat_members, group=welcome_captcha_group)
async def welcomeee(_, message: Message): 
  try:
    for member in message.new_chat_members:
        pos =1 
        if not member.is_bot:
          return
        else:
          if member.id == BOT_ID:
            try:
                await message.reply_text(MSG.CHAT_WELCOME_MSG, reply_markup=BTN.CHAT_WELCOME_BUTTON)                
                
            except:
                return
  except:
    return
  
@Client.on_message(filters.private & filters.incoming & filters.command(['tutorial']))
async def _helhp(client, message):
    await client.send_animation(
        chat_id = message.chat.id,
        animation=MSG.TUTORIAL_GIFS[1],
        caption = MSG.LOL_TUTORIAL_TEXT[1],
        parse_mode="markdown",
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )
    

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(filters.regex(pattern=r"^pm_tutorial$"))
async def _heldp(b, cb):
    chat_id = cb.message.chat.id
    try:
      await b.send_animation(
          chat_id = chat_id,
          animation=MSG.TUTORIAL_GIFS[1],
          caption = MSG.LOL_TUTORIAL_TEXT[1],
          parse_mode="markdown",
          reply_markup = InlineKeyboardMarkup(map(1)),     
      )
    except:
      return
    try:
      await cb.message.delete()
    except:
      return

@Client.on_callback_query(filters.regex(pattern=r"^back_to_main$"))
async def back_to_main(b, cb):
    chat_id = cb.message.chat.id
    try:
      LEL = [[
                InlineKeyboardButton(text = 'Go Tour Again', callback_data = "pm_tutorial")
             ],
             [
                InlineKeyboardButton(text = "🔝Main Menu", callback_data = "IAA")
             ]]      
      await b.send_message(
          chat_id = chat_id,
          text = "You have came back from the basic tour",
          reply_markup = InlineKeyboardMarkup(LEL)
      )
    except:
      return
    try:
      await cb.message.delete()
    except:
      return

@Client.on_callback_query(help_callback_filter)
async def help_answer(b, cb):
    chat_id = cb.message.chat.id
    message_id = cb.message.message_id
    msg = int(cb.data.split('+')[1])
    try:
      await b.edit_message_media(
            chat_id=chat_id,    
            message_id=message_id,
            media=InputMediaAnimation(media=MSG.TUTORIAL_GIFS[msg],
            caption=MSG.LOL_TUTORIAL_TEXT[msg]),    
            reply_markup=InlineKeyboardMarkup(map(msg)),
      )
    except:
      return
@Client.on_callback_query(filters.regex(pattern=r"^tcls$"))
async def m_cb(b, cb):
      try:
        await cb.answer("Closed menu")
        await cb.message.delete()
      except:
        return
def map(pos):
    if(pos==1):
        button = [[
                    InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
                  ],
                  [
                    InlineKeyboardButton(text = "🔝Main Menu", callback_data = "back_to_main")
                 ]]
    elif(pos==len(MSG.LOL_TUTORIAL_TEXT)-1):
        url = f"https://t.me/DeCodeSupport"
        button = [[
                    InlineKeyboardButton(text = 'Terms & Conditions', url="https://telegra.ph/Terms-and-Conditions-06-21"),
                  ],
                  [
                    InlineKeyboardButton(text = '📲 Updates', url=f"https://t.me/DeeCodeBots"),
                    InlineKeyboardButton(text = '💬 Support', url=f"https://t.me/DeCodeSupport"),
                  ],
                  [
                    InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                    InlineKeyboardButton(text = '❌', callback_data = "tcls"),
                  ],
                  [
                    InlineKeyboardButton(text = "🔝Main Menu", callback_data = "back_to_main")
                 ]]
    else:
        button = [[
                    InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                    InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
                  ],
                  [
                    InlineKeyboardButton(text = "🔝Main Menu", callback_data = "back_to_main")
                 ]]
    return button
