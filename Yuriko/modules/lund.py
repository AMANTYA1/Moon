import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from Yuriko import dispatcher
from Yuriko.modules.disable import DisableAbleCommandHandler
from Yuriko.modules.helper_funcs.chat_status import is_user_admin, user_admin
from Yuriko.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'lund' 
EDIT_SLEEP = 1
#edit how many times in 'lund' 
EDIT_TIMES = 3

police_siren = [
            "𓂸𓂸𓂸\n𓂺𓂺𓂺𓂺\n💦💦💦💦",
            "👄👄👄\n👅👅👅\n𓃗𓃗"
]



@user_admin
@run_async
def lund(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Police is coming!') 
    for x in range(EDIT_TIMES):
        msg.edit_text(police_siren[x%2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('Gira diya bc 😪 sprem')



LUND_HANDLER = DisableAbleCommandHandler("lund", lund)


dispatcher.add_handler(LUND_HANDLER)
