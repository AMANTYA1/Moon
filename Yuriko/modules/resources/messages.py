import os

class Messages():
  NEW_PROJECT_TEXT = """
**All Commands**

Everything grouped in Yuriko help menu is expanded and listed below

Click buttons to get help  
"""
  
  CHAT_WELCOME_MSG = """
Thanks for adding me to your group! Don't forget follow my news channel @DaisyXUpdates.

**New to Yuriko, Touch the below button and start me in PM**
"""
  
  START = """
Hey there! My name is **YURIKO**.
I can help manage your groups with useful features, feel free to add me to your groups!
"""

  HELP = """
**Welcome to help menu**

Select **All commands** for full help or select catagory for more help documentation on selected fields
"""

  INLINELIST = """
**Inline Commands**
 
Inline commands can be used by anyone via inline.

**Syntax:**
   @YurikoRobot [command] [query]

**Commands Available:**
- alive - Check Bot's Stats.
- yt [query] - Youtube Search.
- tr [LANGUAGE_CODE] [QUERY]** - Translate Text.
- modapk [name] - Give you direct link of mod apk.
- ud [QUERY] - Urban Dictionary Query
- google [QUERY] - Google Search.
- webss [URL] - Take Screenshot Of A Website.
- bitly [URL] - Shorten A Link.
- wall [Query] - Find Wallpapers.
- pic [Query] - Find pictures.
- saavn [SONG_NAME] - Get Songs From Saavn.
- deezer [SONG_NAME] - Get Songs From Deezer.
- torrent [QUERY] - Torrent Search.
- reddit [QUERY] - Get memes from reddit.
- imdb [QUERY] - Search movies on imdb.
- spaminfo [ID] - Get spam info of the user.
- lyrics [QUERY] - Get lyrics of the song.
- paste [TEXT] - Paste text on pastebin.
- define [WORD] - Get definition from Dictionary.
- synonyms [WORD] - Get synonyms from Dictionary.
- antonyms [WORD] - Get antonyms from Dictionary.
- country [QUERY] - Get Information about given country.
- cs - Gathers Cricket info (Globally).
- covid [COUNTRY] - Get covid updates of given country.
- fakegen - Gathers fake information.
- weather [QUERY] - Get weather information.
- datetime [QUERY] - Get Date & time information of given country/region.
- app [QUERY] - Search for apps in playstore.
- gh [QUERY] - Search github.
- so [QUERY] - Search stack overflow.
- wiki [QUERY] - Search wikipedia.
- ping - Check ping rate.
- pokedex [TEXT]: Pokemon Search

❖ You can try this by clicking below button ❖
"""

  ABTT = """
<b><u>About Me</u></b>

@YurikoRobot is one of the most powerful group management bot exist in telegram trusted by millions of users & tens thousands of groups all over the world

Yuriko project is developed by @Shubhanshutya with the help of many open source projects

Daisy was online since 2019 and helped many admins to keep their groups effectively 

<b>Why Daisy:</b>
   - <b>Simple:</b> Daisy brings you the best tools with a simple easy to use manner
   - <b>Featured:</b> Daisy is the most featured group management bot ever made
   - <b>Fast:</b> Daisy can do things faster in groups
   - <b>Independent:</b> Daisy is Maintained by volunteers, No gbans, No sudo powers. All power belongs to you.

[♚ Special Credits](https://telegra.ph/Special-Credits-06-21)

[💾 Source Code ](https://github.com/AMANTYA1/Yuriko)

[♕ Team Null](https://github.com/AMANTYA1) 

[📄 Terms And Conditions](https://telegra.ph/Terms-and-Conditions-06-21)

<b>Licensed under the GNU Affero General Public Lisence v3.0</b>

© 2020 - 2021 @YurikoRobot. All Rights Reserved
"""

  TUTORIAL_TEXT = """
**New to Yuriko!** Here is the quick start guide which will help you to understand what is Daisy and how to use it.

Click below button to enter a basic tour to know about how to use me
"""
  
  TUTORIAL_GIFS = [
"http://telegra.ph//file/60fd8f0252283943348ba.jpg",            
"http://telegra.ph//file/60fd8f0252283943348ba.jpg", 
"http://telegra.ph//file/60fd8f0252283943348ba.jpg",             
"http://telegra.ph//file/60fd8f0252283943348ba.jpg", 
"http://telegra.ph//file/60fd8f0252283943348ba.jpg", 
"http://telegra.ph//file/60fd8f0252283943348ba.jpg", 
"http://telegra.ph//file/60fd8f0252283943348ba.jpg", 
"http://telegra.ph//file/60fd8f0252283943348ba.jpg"    
      ]
  
  LOL_TUTORIAL_TEXT = [
            ".",
f"""
**Hey, Welcome to Yuriko configuration Tutorial**

**Before we go, I need admin permissions in this chat to work properly**
1) Click Manage Group
2) Goto Administrators and add @YurikoRobot as Admin
3) Giving full permissions make Yuriko fully useful
""",

f"""
**Let's make your group bit effective now**

Congragulations, Yuriko now ready to manage your group

Here are some essentialt to try on

**Admin tools**
Basic Admin tools help you to protect and powerup your group
You can ban members, Kick members, Promote someone as admin through commands of bot

**Welcomes**
Lets set a welcome message to welcome new users coming to your group
send /setwelcome [message] to set a welcome message
Also you can Stop entering robots or spammers to your chat by setting welcome captcha 

**Refer Help menu to see everything in detail**
""",
f"""
**Filters**
Filters can be used as automated replies/ban/delete when someone use a word or sentence
For Example if I filter word 'hello' and set reply as 'hi'
Bot will reply as 'hi' when someone say 'hello'
You can add filters by sending /addfilter [filter name]

**AI Chatbot**
Want someone to chat in group?
Yuriko has an intelligent chatbot with multilang support
Let's try it,
Send `/chatbot on` and reply to any of my messages to see the magic
""",

f"""
**Setting up notes**
You can save message/media/audio or anything as notes
to get a note simply use # at the beginning of a word
See the image..
You can also set buttons for notes and filters (refer help menu)
""",

f"""
**Setting up antilood**
Let's stop spammer activities in your group
Set /antoflood [number]
then send a time to set the timer or set only stop continues messeges by sending 0
And now let's set the punishment for spammers by sending /setfloodaction (read help menu)
""",

f"""
**Using Inline tools**
Is Yuriko only for groups?.
No she can help you in personal chats too
you can use few commands of Yuriko via inline
type @YurikoRobot and enjoy inline
""",

f"""
**So now you are at the end of basic tour. But this is not all I can do.

Send /help in bot pm to access help menu**

There are many handy tools to try out. 
And also if you have any suggessions about me, Don't forget to tell them to devs

**Again thanks for using me**

✪ By using @YurikoRobot you are agreed to our terms & conditions
"""        
      ]

  FUN_N_EXTRAS = """
**Fun tools and Extras**

Extra tools which are available in bot and tools made for fun are here

Click the buttons for help
"""

  INFO = """
<b><u>Info & About</u></b>

In here you can find what is Daisy and how to set her up

Click buttons for help
"""

  FILTERS = """
Help for **Filters** module:

**Filters Module**:
Filter module is great for everything! filter in here is used to filter words or sentences in your chat - send notes, warn, ban those!

**Yuriko filters comes under 4 types.**

1) **Advanced Filters** -  Built for send notes, warn, ban those who send a word/sentence. Support regex, Buttons, Formatting and variables

2) **Text Filters** - Text filters are for short and text replies

3) **Autofilters** -  Filter content of a given channel automatically

4) **Random Filters** - Random reply will be given from a set of given replies
"""

  HLP = """
**All Commands**

Every possibility of Daisy is documentated here

Click buttons to get help
"""

  ADV_CMDS = """
**Advanced Commands**

Advanced commands will help you to secure your groups from attackers and do many stuff in group from a single bot

Click buttons for help
"""

  BASIC_CMDS = """
**Basic Commands**

Basic commands are the basic tools of Daisy which help you to manage your group easily and effectively

Click buttons to get help
"""

  C_TOOLS_TEXT = """
Help for **Channel Tools** Module:

**Channel tools**

Have too many channels and groups, and need to send one post to all,
Channel tools are built for you

Channel tools are coming in two types
1) Autoforward
2) Autopost
"""

  AUTO_FOR_TEXT = """
Help for **AutoForward** Module:

**Autoforward**

Autoforward forward messages coming in channel to given group automatically
Can be set to multiple groups too

**Syntax**
/autoforward [FROM_CHANNEL_ID] [TO_CHAT_ID] : Enable auto forwarding from channel to group
/rmautoforward [FROM_CHANNEL_ID] [TO_CHAT_ID] : Disable auto forwarding from channel to group

**「 Rules 」**
- You should add me to both chat with admin rights. 
- You should be admin of both chats
- No media allowed

**Autoforward can be used to forward messages from Channel to Groups**
"""
