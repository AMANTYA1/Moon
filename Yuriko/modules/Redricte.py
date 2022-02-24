
from Yuriko import pbot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp
import pyromod

text = """
Click the below button on go to the github repo, 
then fork it and give me **forked source link**.
@YurikoRobot
"""


@app.on_message(filters.command("deploy"))
async def givedeploylink(_, message):        
    sex = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Fork Source", url=f"https://github.com/FriDayXD/yuriko//fork"),
                InlineKeyboardButton("My Github", callback_data="github")
            ]
        ]
)

    await app.send_photo(message.chat.id, photo="https://telegra.ph/file/0dee6659879249e0fcbc2.jpg", 
                                             caption=text, reply_markup=sex, parse_mode='Markdown')
    
    while True :
        askit = await app.listen(message.chat.id, filters=filters.text, timeout=120)
        fork = askit.text
        if fork == "https://github.com/szsupunma/sz-rosebot" or fork == "https://github.com/szsupunma/sz-rosebot.git":
            return await app.ask(message.chat.id, "You can't use original repo... try again! by sending /deploy command with fork link")
        if fork != "https://github.com/FriDayXD/yuriko/" and fork != "https://github.com/FriDayXD/yuriko.git" : break
    m = await app.send_message(message.chat.id, "`⚙️ Creating Your link..`")
    hmm = "https://heroku.com/deploy?template=" + str(fork)
    await message.reply_photo(
                  photo = "https://telegra.ph/file/2a318a6b85663814a2ce6.jpg",
                  caption =f"""
**Deploy link generated**
**Requestor** : {message.from_user.mention}
**Link** : `{hmm}`
Click the below button to deploy it heroku.  
@szteambots          
                   """, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Deploy", url="https://heroku.com/deploy?template="+str(fork))]]))
    await m.delete()

@app.on_callback_query(filters.regex("github"))
async def github(_, query):
    API = f'https://api.github.com/users/szsupunma'
    async with aiohttp.ClientSession() as session:
        async with session.get(API) as request:
            result = await request.json()
            try:
                repositories = result['public_repos']
                followers = result['followers']
                await query.answer(f"""
» Followers: {followers}
» Username: AMANTYA1
» Repositories: {repositories}
@YurikoRobot
""", show_alert=True)
            except Exception as e:
                print(str(e))
                pass



__mod_name__ = "Redirect"
__help__ = """
**Hello Dear Developers**,
As you know, some of open source repositories  got flagged by heroku.
So many of you may not be able to deploy them! 

**Here is the way to bypass it :**

1. Login or Signup on github
2. Fork the Repo and Copy Its URL
3. start @YurikoRobot  pm.
4. send /deploy command
5. send Your Copied URL 
6. Click heroku deploy url button
7. Now Fillup Variables & Deploy .

Note: You can also deploy any repo using this that are flagged in heroku.

[Video tutorial](Soon) | [Use Site](Soon)
"""
