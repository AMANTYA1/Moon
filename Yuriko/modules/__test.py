from Yuriko.button.logo import *



__help__ = """𖣘 Kɪɢᴏ Hᴀᴠᴇ Aʀᴇ Mᴀᴋɪɴɢ ᴛʜʀᴇᴇ Tʏᴘᴇs Lᴏɢᴏ 
Hᴇʀᴇ ʏᴏᴜ sᴇᴇ.
"""  # no help string

__button__ = [ InlineKeyboardButton(text="Lᴏɢᴏ", callback_data="aliciafun_"),
            InlineKeyboardButton(text="Sʟᴏɢᴋ", callback_data="aliciafunemoji_"),
            InlineKeyboardButton(text="Gʟᴏɢᴏ", callback_data="aliciafungames_"),

] 
__buttons__ = [InlineKeyboardButton(text="Wʀɪᴛᴇ", callback_data="aliciafuncouple_"), 
]



__mod_name__ = "Lᴏɢᴏ"

dispatcher.add_handler(fun_callback_handler)
dispatcher.add_handler(fun_emoji_callback_handler)
dispatcher.add_handler(fun_games_callback_handler)
dispatcher.add_handler(fun_couple_callback_handler)
