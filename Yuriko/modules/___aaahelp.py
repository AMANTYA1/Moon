#      __________________________________________________________________________________
#     |                                                                                  |
#     |     HH    HH EEEEEE LL     PPPPPP      MMM    MMM EEEEEE NN     NN UU    UU      |
#     |     HH    HH EE     LL     PP  PP      MM M  M MM EE     NNNN   NN UU    UU      |
#     |     HHHHHHHH EEEEE  LL     PPPPPP      MM  MM  MM EEEEE  NN  NN NN UU    UU      | 
#     |     HH    HH EE     LL     PP          MM      MM EE     NN    NNN UU    UU      |
#     |     HH    HH EEEEEE LLLLLL PP          MM      MM EEEEEE NN     NN  UUUUUU       |
#     |__________________________________________________________________________________|     



# ----------------------------- IMPORTS ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- IMPORTS ----------------------------------------------------------
# ----------------------------- IMPORTS ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- IMPORTS ----------------------------------------------------------

import re, os, random, asyncio

from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from Yuriko import pbot

from Yuriko.modules.null.messages import Messages as MSG
from Yuriko.modules.null.buttons import Buttons as BTN

# ----------------------------- TEXT ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- TEXT ----------------------------------------------------------
# ----------------------------- TEXT ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- TEXT ----------------------------------------------------------

# Text are here -> .DaisyX/modules/resources/messages.py

# ----------------------------- BUTTONS ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- BUTTONS ----------------------------------------------------------
# ----------------------------- BUTTONS ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- BUTTONS ----------------------------------------------------------

# Start

suru = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="suru")]]

lover = [[InlineKeyboardButton("❔ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ❔", callback_data="ALL")]]
lover += [[InlineKeyboardButton("📃 IɴꜰᴏʀMᴀᴛɪᴏɴ 📃", callback_data="IAA")]]
lover += [[InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇꜱ", url =  "t.me/Deecodebots"),InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ 👥", url =  "t.me/Decodesupport")]]
lover += [[InlineKeyboardButton("💕 Sᴜᴍᴍᴏɴ Mᴇ 💕", url = "t.me/CRAZYVC_X_BOT?startgroup=true")]]

# Main help

help = [[InlineKeyboardButton("➕ Aʟʟ Cᴏᴍᴍᴀɴᴅꜱ ➕", callback_data="BCK")]]
help += [[InlineKeyboardButton("👥 Bᴀꜱɪᴄ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="BBC"),InlineKeyboardButton("Aᴅᴠᴀɴᴄᴇᴅ Cᴏᴍᴍᴀɴᴅꜱ 🛠", callback_data="ADC")]]
help += [[InlineKeyboardButton("📖 Exᴛʀᴀꜱ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="FTE"),InlineKeyboardButton("Iɴʟɪɴᴇ Cᴏᴍᴍᴀɴᴅꜱ 🔎", callback_data="ICMD")]]
help += [[InlineKeyboardButton("╰✰ Bᴀᴄᴋ ✰╮", callback_data="suru")]]

ghelp = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ALL")]]

# Extras

fte = [[InlineKeyboardButton("Basic",callback_data="basic"),InlineKeyboardButton("Book",callback_data="book"),InlineKeyboardButton("Carbon", callback_data="arbon")]]
fte += [[InlineKeyboardButton("CC Checker", callback_data="checker"), InlineKeyboardButton("Country", callback_data="country"),InlineKeyboardButton("Couple",callback_data="couple")]]
fte += [[InlineKeyboardButton("Covid", callback_data="covid"), InlineKeyboardButton("Currency", callback_data="paisa"),InlineKeyboardButton("Cricket Score", callback_data="cricket")]]
fte += [[InlineKeyboardButton("Date Time", callback_data="tugk"),InlineKeyboardButton("Fake Info",callback_data="fake"),InlineKeyboardButton("Image Editor", callback_data="image")]]
fte += [[InlineKeyboardButton("Karma", callback_data="karma"),InlineKeyboardButton("Maths",callback_data="monkey"),InlineKeyboardButton("Memes",callback_data="memes")]]
fte += [[InlineKeyboardButton("Music",callback_data="gaana"),InlineKeyboardButton("Music Player",callback_data="vcm"),InlineKeyboardButton("Name History",callback_data="history")]]
fte += [[InlineKeyboardButton("Night Mode", callback_data="soja"),InlineKeyboardButton("Open/ttf", callback_data="ttf"),InlineKeyboardButton("Paste", callback_data="paste")]]
fte += [[InlineKeyboardButton("Phone Info", callback_data="phone"),InlineKeyboardButton("Qr Code",callback_data="qr"), InlineKeyboardButton("Send", callback_data="send")]]
fte += [[InlineKeyboardButton("Telegraph",callback_data="graph"),InlineKeyboardButton("Scheduler", callback_data="shdlr"), InlineKeyboardButton("Torrent", callback_data="torrent")]]
fte += [[InlineKeyboardButton("Text to Speech",callback_data="t2s"),InlineKeyboardButton("Zip",callback_data="zepper")]]
fte += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ALL")]]

skem = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="FTE")]]

becktohlp = [[InlineKeyboardButton("« Go Inline »", switch_inline_query_current_chat="")],
             [InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ALL")]]

ufuk = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ADC")]]

# Advanced help

adc = [[InlineKeyboardButton("Android", callback_data="android"),InlineKeyboardButton("Anime",callback_data="anime"),InlineKeyboardButton("Backups",callback_data="backup")]]
adc += [[InlineKeyboardButton("Channel Tools", callback_data="chtool"), InlineKeyboardButton("ChatBot", callback_data="chatbot"), InlineKeyboardButton("Force Subscribe", callback_data="fsub")]]
adc += [[InlineKeyboardButton("Group Guardian", callback_data="gard"), InlineKeyboardButton("Lang-Tools", callback_data="langtools"), InlineKeyboardButton("Languages", callback_data="skem")]]
adc += [[InlineKeyboardButton("Polls", callback_data="poll"), InlineKeyboardButton("RSS Feed", callback_data="rss"),InlineKeyboardButton("Search", callback_data="search")]]
adc += [[InlineKeyboardButton("Stickers", callback_data="sticker"), InlineKeyboardButton("Tag Alerts", callback_data="tgalrt")]]
adc += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ALL")]]

# Basic Help

back = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BBC")]]

bbc = [[InlineKeyboardButton("Admins", callback_data="admin"),InlineKeyboardButton("AntiFlood",callback_data="flood"),InlineKeyboardButton("Blacklist",callback_data="blist")]]
bbc += [[InlineKeyboardButton("Connections",callback_data="connect"),InlineKeyboardButton("Disabling", callback_data="disable"), InlineKeyboardButton("Federations", callback_data="feds")]]
bbc += [[InlineKeyboardButton("Filters", callback_data="filters"),InlineKeyboardButton("Greetings", callback_data="welcome"), InlineKeyboardButton("Locks", callback_data="locks")]]
bbc += [[InlineKeyboardButton("Notes", callback_data="notes"),InlineKeyboardButton("Reports", callback_data="report"), InlineKeyboardButton("Rules", callback_data="rules")]]
bbc += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ALL")]]

# Tutorial 

tutorial_btn = [[InlineKeyboardButton("Quick Setup Guide",callback_data="pm_tutorial")]]
tutorial_btn += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="IAA")]]

# Start

info = [[InlineKeyboardButton("🤷 Hᴏᴡ Tᴏ Uꜱᴇ Mᴇ", callback_data="configuration"), InlineKeyboardButton("Aʙᴏᴜᴛ Mᴇ 👩‍💻", callback_data="abtme")]]
info += [[InlineKeyboardButton("📡 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url = "t.me/Deecodebots"), InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 👥", url =  "t.me/Decodesupport")]]
info += [[InlineKeyboardButton("💥 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url =  "https://github.com/TeamDeeCode/Yuriko"), InlineKeyboardButton("Tᴇʀᴍꜱ Aɴᴅ Cᴏɴᴅɪᴛɪᴏɴꜱ 📄", url =  "https://telegra.ph/Terms-And-Conditions-12-13")]]
info += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="suru")]]
abtbtn = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="IAA")]]
gbck = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="IAA")]]

ohkuki = [[InlineKeyboardButton("🛠️ Make Your Own Chatbot with Kuki",url="https://t.me/KukiUpdates/23")]]
ohkuki += [[InlineKeyboardButton("« Bᴀᴄᴋ",callback_data="BCK")]]
ohk = [[InlineKeyboardButton("« Bᴀᴄᴋ",callback_data="BCK")]]

# Help

kk = [[InlineKeyboardButton("Admins ", callback_data="admin"),InlineKeyboardButton("AI Assistant",callback_data="chatbot"),InlineKeyboardButton("AntiFlood",callback_data="flood")]]
kk += [[InlineKeyboardButton("Android ", callback_data="android"),InlineKeyboardButton("Anime ",callback_data="anime"),InlineKeyboardButton("Backups ",callback_data="backup")]]
kk += [[InlineKeyboardButton("Blacklist ", callback_data="blist"),InlineKeyboardButton("Channel Tools",callback_data="chtool"),InlineKeyboardButton("Connections ",callback_data="connect")]]
kk += [[InlineKeyboardButton("Disabling",callback_data="disable"),InlineKeyboardButton("Federations ", callback_data="feds"),InlineKeyboardButton("Filters ",callback_data="filters")]] 
kk += [[InlineKeyboardButton("Force Subscribe",callback_data="fsub"),InlineKeyboardButton("Greetings",callback_data="welcome"),InlineKeyboardButton("Group Guardian", callback_data="gard")]] 
kk += [[InlineKeyboardButton("Inline",callback_data="inline"),InlineKeyboardButton("Image Editor ", callback_data="image"),InlineKeyboardButton("Languages",callback_data="skem")]] 
kk += [[InlineKeyboardButton("Lang-Tools ", callback_data="langtools"),InlineKeyboardButton("Locks",callback_data="locks"),InlineKeyboardButton("Memes ",callback_data="memes")]] 
kk += [[InlineKeyboardButton("Music",callback_data="gaana"),InlineKeyboardButton("Music Player",callback_data="vcm"),InlineKeyboardButton("Notes",callback_data="notes")]]
kk += [[InlineKeyboardButton("Reports", callback_data="report"),InlineKeyboardButton("RSS Feed",callback_data="rss"),InlineKeyboardButton("Rules",callback_data="rules")]]
kk += [[InlineKeyboardButton("Search", callback_data="search"),InlineKeyboardButton("Stickers", callback_data="sticker"),InlineKeyboardButton("Tag Alert",callback_data="tgalrt")]]
kk += [[InlineKeyboardButton("📚Extras", callback_data="vehla"),InlineKeyboardButton("🗂Misc", callback_data="isc")]]
kk += [[InlineKeyboardButton("🔽 Expand Grouped", callback_data="EXPND")]]
kk += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ALL")]]

# Admin Tools

cheator = [[InlineKeyboardButton("Promotes/Demotes", callback_data="promote"), InlineKeyboardButton("Bans", callback_data="ban_kk"), InlineKeyboardButton("Mute", callback_data="muta")]]
cheator += [[InlineKeyboardButton("Warn", callback_data="dlk_kk"), InlineKeyboardButton("Cleans/Purges", callback_data="clean_kk"),InlineKeyboardButton("Users", callback_data="user_kk")]]
cheator += [[InlineKeyboardButton("Other", callback_data="other_kk"),InlineKeyboardButton("Pins", callback_data="pin_kk"),InlineKeyboardButton("Approoval", callback_data="aproval")]]
cheator += [[InlineKeyboardButton('« Bᴀᴄᴋ',callback_data='BBC')]]

sedlyf = [[InlineKeyboardButton('« Bᴀᴄᴋ',callback_data='gheiadmin')]]

# VC

vc = [[InlineKeyboardButton("Channel Music", callback_data="channel"), InlineKeyboardButton("More Tools", callback_data="mtool")]]
vc += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="FTE")]]

mc = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="vcm")]]

# Channel 

tool = [[InlineKeyboardButton("Auto Forward", callback_data="tfwd"), InlineKeyboardButton("Auto Post", callback_data="tpst")]]
tool += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ADC")]]

nikal = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="chtool")]]

#GGuard

gguardlel = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="gard")]]
gguartool = [[InlineKeyboardButton("Global Mode", callback_data="globlgard"), InlineKeyboardButton("NSFW Guard", callback_data="nsgard"), InlineKeyboardButton("Profanity Mode", callback_data="profgard")]]
gguartool += [[InlineKeyboardButton("No Bots", callback_data="nobgard"), InlineKeyboardButton("AntiArabic", callback_data="antgard"), InlineKeyboardButton("Anti Promo", callback_data="promogard")]]
gguartool += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ADC")]]

# Admins

warn = [[InlineKeyboardButton("Admin Commands", callback_data="wac"), InlineKeyboardButton("User Commands", callback_data="ucmds")]]
warn += [[InlineKeyboardButton("Warn Actions", callback_data="actwar"),InlineKeyboardButton("Warn Limits", callback_data="litwar")]]
warn += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BCK")]]

devil = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="dlk_kk")]]

kid = [[InlineKeyboardButton("Commands", callback_data="fscmd"), InlineKeyboardButton("Setup", callback_data="setupfs")]]
kid += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="ADC")]]

daisy = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="fsub")]]

# Antiflood

auto = [[InlineKeyboardButton("Configuring Time", callback_data="ftime"), InlineKeyboardButton("Supported Actions", callback_data="action")]]
auto += [[InlineKeyboardButton("Example", callback_data="expf")]]
auto += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BBC")]]

soja = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="flood")]]

disable = [[InlineKeyboardButton("Examples", callback_data="dexp")]]
disable += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BBC")]]

sed = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="disable")]]

# Feds 

fedd = [[InlineKeyboardButton('Fed admin commands',callback_data='fadmin'), InlineKeyboardButton('Fed owner commands',callback_data='fowner')]]
fedd += [[InlineKeyboardButton('Fed user commands',callback_data='users')]]
fedd += [[InlineKeyboardButton('« Bᴀᴄᴋ',callback_data='BCK')]]
    
    
fedhai = [[InlineKeyboardButton('« Bᴀᴄᴋ',callback_data='feds')]]

fedd = [[InlineKeyboardButton('Fed admin commands',callback_data='fadmin'), InlineKeyboardButton('Fed owner commands',callback_data='fowner')]]
fedd += [[InlineKeyboardButton('Fed user commands',callback_data='users')]]
fedd += [[InlineKeyboardButton('« Bᴀᴄᴋ',callback_data='BBC')]]
    
    
fedhai = [[InlineKeyboardButton('« Bᴀᴄᴋ',callback_data='feds')]]

# Filters

# |----------------------------------------------------------------------------------------------------------------------------------|

filter = [[InlineKeyboardButton("Basic Filters", callback_data="textfil")]]
filter += [[InlineKeyboardButton("Advanced Filters", callback_data="adfil")]]
filter += [[InlineKeyboardButton("Auto Filters", callback_data="genfil")]]
filter += [[InlineKeyboardButton("Random Filters", callback_data="ranfil")]]
filter += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BBC")]]

marja = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="filters")]]

# |-------------------------------------------------------------------------------------------------------------------------------|

pro = [[InlineKeyboardButton("Classic Filters", callback_data="clfil")]]
pro += [[InlineKeyboardButton("Button Help", callback_data="chutiya")]]
pro += [[InlineKeyboardButton("Variables Help", callback_data="vro")]]
pro += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="filters")]]

chutiya = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="adfil")]]

# Welcomes

randi = [[InlineKeyboardButton("Welcome Security", callback_data="security"),InlineKeyboardButton("Welcome Mutes", callback_data="chup"),InlineKeyboardButton("Button Help",callback_data="gpl")]]
randi += [[InlineKeyboardButton("Clean Services/Purges", callback_data="fuk"),InlineKeyboardButton("Variables Help",callback_data="vkl"),InlineKeyboardButton("Examples", callback_data="tkl")]]
randi += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BBC")]]

ghost = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="welcome")]]

# Locks

lock = [[InlineKeyboardButton('Lock Types', callback_data='typelocbsc'), InlineKeyboardButton('Permission Locks', callback_data='typelocprm')]]
lock += [[InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='BBC')]]

urllock = [[InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='locks')]]

# Notes

inuka = [[InlineKeyboardButton("Note Aliases", callback_data="alias"),InlineKeyboardButton("Formatting", callback_data="mat"),InlineKeyboardButton("Button Help",callback_data="ded")]]
inuka += [[InlineKeyboardButton("Variables Help",callback_data="ofp"),InlineKeyboardButton("Examples", callback_data="inuka")]]
inuka += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BBC")]]

you = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="notes")]]

# Polls
                              # W H O  T H E  F U C K  A D D E D  T H I S  M U C H  O F  F E A T U R E S 
               
               # I  H A T E  D A I S Y

dhoka = [[InlineKeyboardButton('Syntax', callback_data='tax'), InlineKeyboardButton('Stop Poll', callback_data='stpl')]]
dhoka += [[InlineKeyboardButton('Example', callback_data='llexp')]]
dhoka += [[InlineKeyboardButton('Back', callback_data='ADC')]]

danger = [[InlineKeyboardButton('« Bᴀᴄᴋ', callback_data='poll')]]

# Miscs

misc = [[InlineKeyboardButton("Basic", callback_data="basic"), InlineKeyboardButton("Book", callback_data="book"), InlineKeyboardButton("Fake Info", callback_data="fake")]]
misc += [[InlineKeyboardButton("Weather", callback_data="mosam"), InlineKeyboardButton("Phone Info", callback_data="phone"), InlineKeyboardButton("Currency", callback_data="paisa")]]
misc += [[InlineKeyboardButton("Name History", callback_data="history"),InlineKeyboardButton("Send", callback_data="send"),InlineKeyboardButton("Math", callback_data="meth")]]
misc += [[InlineKeyboardButton("Night Mode", callback_data="soja"), InlineKeyboardButton("Open/ttf", callback_data="ttf"),InlineKeyboardButton("Url Tools", callback_data="urtol")]]
misc += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BCK")]]

buk = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="isc")]]


# Xtras
xlm = [[InlineKeyboardButton("Carbon", callback_data="arbon"), InlineKeyboardButton("CC Checker", callback_data="checker"), InlineKeyboardButton("Cricket Score", callback_data="cricket")]]
xlm += [[InlineKeyboardButton("Country", callback_data="country"), InlineKeyboardButton("Covid", callback_data="covid"), InlineKeyboardButton("Date Time", callback_data="tugk")]]
xlm += [[InlineKeyboardButton("Paste", callback_data="paste"), InlineKeyboardButton("Polls", callback_data="poll"), InlineKeyboardButton("Karma", callback_data="karma")]]
xlm += [[InlineKeyboardButton("Telegraph", callback_data="graph"), InlineKeyboardButton("Torrent", callback_data="torrent"), InlineKeyboardButton("Text to Speech", callback_data="t2s")]]
xlm += [[InlineKeyboardButton("Virus Scan", callback_data="virus"), InlineKeyboardButton("Qr Code", callback_data="qr"), InlineKeyboardButton("Url Lock", callback_data="rlock")]]
xlm += [[InlineKeyboardButton("Scheduler", callback_data="shdlr"), InlineKeyboardButton("Zip",callback_data="zepper")]]
xlm += [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="BCK")]]

war = [[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="vehla")]]



# ----------------------------- CALLBACK ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- CALLBACK ----------------------------------------------------------
# ----------------------------- CALLBACK ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- CALLBACK ----------------------------------------------------------

@pbot.on_callback_query()
async def _(b,cb):
    try:
        try:
            user_id = cb.from_user.id
        except:
            return
        if cb.data == "suru":
            try:
                await cb.message.edit(MSG.START, reply_markup=InlineKeyboardMarkup(lover))
                message.stop_propagation()            
            except:
                return
            

        elif cb.data == "ALL":
            try:
                await cb.message.edit(MSG.HELP, reply_markup=InlineKeyboardMarkup(help))
                message.stop_propagation()            
            except:
                return
            
            
        elif cb.data == "EXPND":
            try:
                await cb.message.edit(MSG.NEW_PROJECT_TEXT, reply_markup=BTN.NEW_PROJECT_BUTTONS)
                message.stop_propagation()            
            except:
                return   
            
            
        elif cb.data == "ICMD":
            try:
                await cb.message.edit(MSG.INLINELIST, reply_markup=InlineKeyboardMarkup(becktohlp))
                message.stop_propagation()            
            except:
                return
            

        elif cb.data==("FTE"):

            try:
                await cb.message.edit(MSG.FUN_N_EXTRAS, reply_markup=InlineKeyboardMarkup(fte))
                message.stop_propagation()            
            except:
                return

            
        elif cb.data==("ADC"):

            try:
                await cb.message.edit(MSG.ADV_CMDS, reply_markup=InlineKeyboardMarkup(adc))
                message.stop_propagation()            
            except:
                return
            

        elif cb.data==("BBC"):

            try:
                await cb.message.edit(MSG.BASIC_CMDS, reply_markup=InlineKeyboardMarkup(bbc))
                
                message.stop_propagation()            
            except:
                return

            
        elif cb.data==("IAA"):

            try:
                await cb.message.edit(MSG.INFO, reply_markup=InlineKeyboardMarkup(info), parse_mode="html")
                message.stop_propagation()            
            except:
                return

            
        elif cb.data==("configuration"):

            try:
                await cb.message.edit(MSG.TUTORIAL_TEXT, reply_markup=InlineKeyboardMarkup(tutorial_btn))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("abtme"):

            try:
                await cb.message.edit(MSG.ABTT, reply_markup=InlineKeyboardMarkup(abtbtn), disable_web_page_preview=True,)
                message.stop_propagation()            
            except:
                return


        elif cb.data==("BCK"):

            try:
                await cb.message.edit(MSG.HLP, reply_markup=InlineKeyboardMarkup(kk))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("chtool"):

            try:
                await cb.message.edit(MSG.C_TOOLS_TEXT, reply_markup=InlineKeyboardMarkup(tool))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("tfwd"):

            try:
                await cb.message.edit(MSG.AUTO_FOR_TEXT, reply_markup=InlineKeyboardMarkup(tool))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("tpst"):            

            try:
                await cb.message.edit('''Help for **AutoPost** Module:

**Autopost**

Autopost forward messages coming in channel to given channel automatically
Can be set to multiple channel too

**Syntax**
-/autopost [FROM_CHANNEL_ID] [TO_CHANNEL_ID]: Enable auto posting from channel to channel
-/rmautopost [FROM_CHANNEL_ID] [TO_CHANNEL_ID]: Enable auto posting from channel to channel

**Rules**
- You should add me to both chat with admin rights. 
- You should be admin of both chats    
- No media allowed

**Autoforward can only be used to forward messages from Channel to Channel**''', reply_markup= InlineKeyboardMarkup(tool) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("gard"):

            try:
                await cb.message.edit('''Help for **Group Guardian** module:

**Group Guardian:**

Group's Security is also an very essential fact to consider in group management
Group Guardian is the inbuilt toolkit in daisy for avoid spammers, and to improve security of your group
        ''', reply_markup= InlineKeyboardMarkup( gguartool) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("globlgard"):           

            try:
                await cb.message.edit('''Help for **Global Mode**: 
Force members to use English in your group
Daisy will delete all non English messages

**Commmands**
- /globalmode [on/off]: Enable/Disable English only mode''', reply_markup= InlineKeyboardMarkup(gguardlel)) 
                message.stop_propagation()            
            except:
                return


        elif cb.data==("nsgard"):

            try:
                await cb.message.edit('''Help for **NSFW Guard Mode**: 
Is users send porn on your group. Don't worry Daisy can delete it all
When enabled Daisy will delete photos, stickers, gifs, videos contain porn

**Commmands**
- /nsfwguardian [on/off]: Enable/disable porn cleaning''', reply_markup= InlineKeyboardMarkup(gguardlel) )
                message.stop_propagation()            
            except:
                return



        elif cb.data==("profgard"):
            try:
                await cb.message.edit('''Help for **profanity Mode**: 
Force members not to use slag words in your group
Yuriko will delete all non polite messages

**Commmands**
- /profanity [on/off]: Enable/Disable slag word cleaning''', reply_markup= InlineKeyboardMarkup(gguardlel) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("nobgard"):            
            try:
                await cb.message.edit('''Help for **No Bots Mode**: 
No bots can be used to stop sending messages by non admin bots
When enabled Daisy will delete photos, stickers, gifs, videos sent by non admin bots

**Commmands**
- /nobots [on/off]: Enable/disable non admin bot message deleting''', reply_markup= InlineKeyboardMarkup(gguardlel) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("antgard"):
            try:
                await cb.message.edit('''Help for **AntiArabic Mode**: 
AntiArabic mode is used to delete right to left arabic spam messages
When enabled Daisy will delete text contain arabics and messages sent by arabic usernames
*This module only designed to avoid spammers. 

**Commmands**
- /antiarabic [on/off]: Enable/disable antiarabic mode''', reply_markup= InlineKeyboardMarkup(gguardlel) )
                message.stop_propagation()            
            except:
                return

        elif cb.data==("promogard"):
            try:
                await cb.message.edit('''Help for **No Promo Mode**: 
Anti Promo mode is used to delete promotive spam messages sent in a group
When enabled Daisy will delete links for other groups, usernames of other groups, and some more spam messages using AI algorithm

**Commmands**
- /antipromo [on/off]: Enable/disable antipromo mode''', reply_markup= InlineKeyboardMarkup(gguardlel) )
                message.stop_propagation()            
            except:
                return

        elif cb.data==("vcm"):
            try:
                await cb.message.edit('''Help For **Music Player** Module:

**Music Player Module is no longer supported in Daisy**

Use @ViSioN_MusiC_BoT bot for playing Music in your groups and channel.
__All commands are same as before__''', reply_markup= InlineKeyboardMarkup(ohk) )
                message.stop_propagation()            
            except:
                return

        elif cb.data==("channel"):

            try:
                await cb.message.edit('''Help for **Channel Music Player** Module:

**=>> Channel Music Play 🛠**

**For linked group admins only:**
- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /ccurrent - Show now playing
- /cplayer - Open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

**Note:** channel can also be used instead of c in commands.

**If you don't like to play in linked group:**

1. Get your channel ID. I would be something like (-100xxxxxxxxxx or -501xxxxxx)
2. Make a new group or rename it to --> Channel Music:your_channel_id
3. Add @YurikoRobot as Channel admin with full permissions add helper to channel
4. Simply send commands in your group.''', reply_markup= InlineKeyboardMarkup(mc) )
                message.stop_propagation()            
            except:
                return

        elif cb.data==("mtool"):
            try:
                await cb.message.edit('''Help for **Music Player>>More Tools** Module

**=>> More tools 🧑‍🔧**
/admincache: Updates admin info of your group. Try if bot don't recognize an admin
/userbotjoin : Invite @DaisyXHelper userbot to your chat
/userbotleave : Userbot leaves your chat

Player cmd and all other cmds except /play, /dplay, /splay are only for admins who manages group.''', reply_markup= InlineKeyboardMarkup(mc) )

                message.stop_propagation()            
            except:
                return




        elif cb.data==("muta"):
            try:
                await cb.message.edit('''** Mutes **
- /mute: mute a user
- /unmute: unmutes a user
- /tmute [entity] : temporarily mutes a user for the time interval.''',reply_markup= InlineKeyboardMarkup(sedlyf))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("aproval"):
            try:
                await cb.message.edit('''** Approoval **

Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood, Groupguardian not applying to them.

That's what approvals are for - approve of trustworthy users to allow them to send 

Admin commands:
- /checkstatus: Check a user's approval status in this chat.

Admin commands:
- /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
- /disapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
- /listapproved: List all approved users.
- /disapproveall: disapprove ALL users in a chat. This cannot be undone.''',reply_markup= InlineKeyboardMarkup(cheator))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("gheiadmin"):
            try:
                await cb.message.edit('''Make it easy to admins for manage users and groups with the admin module!
**Available commands:**
** Admin List **
- /adminlist: Shows all admins of the chat.
- /admincache: Update the admin cache, to take into account new admins/admin permissions.''',reply_markup= InlineKeyboardMarkup(cheator))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("promote"):
            try:
                await cb.message.edit('''** Promotes & Demotes**
- /promote (user) (?admin's title): Promotes the user to admin.
- /demote (user): Demotes the user from admin.
- /lowpromote: Promote a member with low rights
- /midpromote: Promote a member with mid rights
- /highpromote: Promote a member with max rights
- /lowdemote: Demote an admin to low permissions
- /middemote: Demote an admin to mid permissions''',reply_markup= InlineKeyboardMarkup(sedlyf) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("ban_kk"):
            try:
                await cb.message.edit('''** Bans & Kicks **
- /ban: bans a user
- /tban [entity] : temporarily bans a user for the time interval.
- /unban: unbans a user
- /unbanall: Unban all banned members
- /banme: Bans you
- /kick: kicks a user
- /kickme: Kicks you''',reply_markup= InlineKeyboardMarkup(sedlyf))
                message.stop_propagation()            
            except:
                return

        elif cb.data==("wac"):
            try:
                await cb.message.edit('''**Commands For Admins**

**General (Admins):**
- /warn (?user) (?reason): Use this command to warn the user! you can mention or reply to the offended user and add reason if needed
- /delwarns or /resetwarns: This command is used to delete all the warns user got so far in the chat
- /dwarn [reply]: Delete the replied message and warn him''', reply_markup= InlineKeyboardMarkup(devil) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("litwar"):
            try:
                await cb.message.edit('''**Limits For Warn**

**Warnlimt (Admins):**
- /warnlimit (new limit): Sets a warnlimit
Not all chats want to give same maximum warns to the user, right? This command will help you to modify default maximum warns. Default is 3

The warnlimit should be greater than <code>1</code> and less than <code>10,000</code>''', reply_markup= InlineKeyboardMarkup(devil) )
                message.stop_propagation()            
            except:
                return

        elif cb.data==("ucmds"):
            try:
                await cb.message.edit('''**Warn Related Commands For Users**

**User Commands:**
/warns (?user)
Use this command to know number of warns and information about warns you got so far in the chat. To use yourself you doesn't require user argument.''',reply_markup= InlineKeyboardMarkup(devil) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("actwar"):
            try:
                await cb.message.edit('''** Actions For Warns**

**Warnaction (Admins):**
/warnaction (mode) (?time)
Well again, not all chats want to ban (default) users when exceed maximum warns so this command will able to modify that.
Current supported actions are <code>ban</code> (default one), <code>mute</code>, <code>tmute</code>. The tmute mode require <code>time</code> argument as you guessed.''', reply_markup= InlineKeyboardMarkup(devil) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("dlk_kk"):
            try:
                await cb.message.edit ('''** Warns **
You can keep your members from getting out of control using this feature!

**Available commands:**

All Commands are given below as per there uses in buttons. 
Click on button to which related commands you want to know. 

**Note:** This Command is specially for controlling spams in groups also to limit the users to break the rules of groups''', reply_markup= InlineKeyboardMarkup(sedlyf) )
                message.stop_propagation()            
            except:
                return

        elif cb.data==("dlk_kk"):
            try:
                await cb.message.edit ('''** Warns **
You can keep your members from getting out of control using this feature!

**Available commands:**

All Commands are given below as per there uses in buttons. 
Click on button to which related commands you want to know. 

**Note:** This Command is specially for controlling spams in groups also to limit the users to break the rules of groups''', reply_markup= InlineKeyboardMarkup(warn) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("clean_kk"):
            try:
                await cb.message.edit(''' ** Cleaner/Purges **
- /purge: deletes all messages from the message you replied to
- /del: deletes the message replied to
- /zombies: counts the number of deleted account in your group
- /kickthefools: Kick inactive members from group (one week) ''',reply_markup= InlineKeyboardMarkup(sedlyf))
                message.stop_propagation()            
            except:
                return



        elif cb.data==("user_kk"):
            try:
                await cb.message.edit('''**User Info**
    - /info: Get user's info
    - /users: Get users list of group
    - /spwinfo : Check user's spam info from intellivoid's Spamprotection service
    - /whois : Gives user's info like pyrogram''',reply_markup= InlineKeyboardMarkup(sedlyf))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("other_kk"):
            try:
                await cb.message.edit('''**Other**
- /invitelink: Get chat's invitr link
- /settitle [entity] [title]: sets a custom title for an admin. If no [title] provided defaults to "Admin"
- /setgrouptitle [text] set group title
- /setgrouppic: reply to an image to set as group photo
- /setdescription: Set group description
- /setsticker: Set group sticker''',reply_markup= InlineKeyboardMarkup(sedlyf))
                message.stop_propagation()            
            except:
                return




        elif cb.data==("admin"):
            try:
                await cb.message.edit('''Make it easy to admins for manage users and groups with the admin module!
    **Available commands:**
    ** Admin List **
    - /adminlist: Shows all admins of the chat.
    - /admincache: Update the admin cache, to take into account new admins/admin permissions.''',reply_markup= InlineKeyboardMarkup(cheator))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("chatbot"):
            try:
                await cb.message.edit('''Help for **AI Assistant** module:

**Chatbot** 
AI based chatbot allows Daisy to talk and provides a more interactive group chat experience.
- /chatbot [ON/OFF]: Enables and disables AI Chat mode
- /chatbot [acobot/kuki] : Switch between chatbots

**Available chatbots**
Kuki - Advanced, inteligent and cute chatbot which will keep you happy all time.. Join @KukiUpdates for updates
Acobot -Simple but powerful chatbot which can keep AI chat more clean and professional

**Language Support**
Yuriko's Acobot based chatbot support almost all languages in world and Kuki support all major languages

**Assistant Service**
- /ask [question]: Ask question from daisy
- /ask [reply to voice note]: Get a voice reply
- /yuriko [Message]: Get voice reply 
''', reply_markup= InlineKeyboardMarkup(ohkuki) )
                message.stop_propagation()            
            except:
                return



        elif cb.data==("setupfs"):
            try:
                await cb.message.edit('''**Setup of Force Subscriber**

**Setup**
1) First of all add me in the group as admin with ban users permission and in the channel as admin.
Note: Only creator of the group can setup me and i will not allow force subscribe again if not done so.''', reply_markup= InlineKeyboardMarkup(daisy) )
                message.stop_propagation()            
            except:
                return



        elif cb.data==("fscmd"):
            try:
                await cb.message.edit('''**Commands for Force Subscriber**
**Commmands**
- /forcesubscribe - To get the current settings.
- /forcesubscribe no/off/disable - To turn of ForceSubscribe.
- /forcesubscribe {channel username} - To turn on and setup the channel.
- /forcesubscribe clear - To unmute all members who muted by me.
**Note:** /forcesub is an alias of /forcesubscribe''', reply_markup= InlineKeyboardMarkup(daisy) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("fsub"):
            try:
                await cb.message.edit('''Help for **Force Subscribe**  module:

**ForceSubscribe:**
- Yuriko can mute members who are not subscribed your channel until they subscribe
- When enabled I will mute unsubscribed members and show them a unmute button. When they pressed the button I will unmute them.

**For Any Help** **Contact** @Shubhanshutya''', reply_markup= InlineKeyboardMarkup(kid) )
                message.stop_propagation()            
            except:
                return



        elif cb.data==("android"): 
                try: 
                    await cb.message.edit('''Help for **Android** module:
**Module specially made for Android users.**

**GSI**
- /phh: Get the latest PHH AOSP GSIs.
- /phhmagisk: Get the latest PHH Magisk.

**Device firmware:**
- /samcheck (model) (csc): Samsung only - shows the latest firmware info for the given device, taken from samsung servers.
- /samget (model) (csc): Similar to the /samcheck command but having download buttons.

**Misc**
- /magisk: Get latest Magisk releases.
- /twrp (codename): Gets latest TWRP for the android device using the codename.
- /ofox (codename): Gets latest OFRP for the android device using the codename.
- /ofox devices: Sends the list of devices with stable releases supported by OFRP.
- /models (codename): Search for Android device models using codename.
- /whatis (codename): Find out which smartphone is using the codename.''',reply_markup= InlineKeyboardMarkup(ufuk))
                except:
                    return

        elif cb.data==("anime"):
            try:
                await cb.message.edit('''Help for **Anime** module:

Get information about anime, manga or anime characters.

**Available commands:**
- /anime (anime): returns information about the anime.
- /character (character): returns information about the character.
- /manga (manga): returns information about the manga.
- /airing (anime): returns anime airing info.
- /kaizoku (anime): search an anime on animekaizoku.com
- /kayo (anime): search an anime on animekayo.com
- /ganime (anime): search an anime on gogoanime.so
- /upcoming: returns a list of new anime in the upcoming seasons.
- /aq : get anime random quote''', reply_markup= InlineKeyboardMarkup(ufuk) )
                message.stop_propagation()            
            except:
                return

        elif cb.data==("tgalrt"):
            try:
                await cb.message.edit('''Help for **Tag Alert** module:

Too many mentions.. Cant you manage them all alone..

**Here is the solution**

If you are tagged/mentioned in a group where Daisy is present
Daisy will notify it to you via private message after enabling tag alerts

**Commands (only work on bot inbox)**
- /tagalert on : Turn tag alerts on
- /tagalert off : Turn tag alert off

Example:
If you are mentioned in a group Daisy will tell you who mentioned you, message that you are tagged in and which group is that
''', reply_markup= InlineKeyboardMarkup(ufuk) )
                message.stop_propagation()            
            except:
                return



        elif cb.data==("ftime"):
            try:
                await cb.message.edit('''**Way to Configure Timing**

Replace (limit) with any integer, should be less than 200. When setting up, Daisy would ask you to send expiration time, if you dont understand what this expiration time for? User who sends specified limit of messages consecutively within this TIME, would be kicked, banned whatever the action is. if you dont want this TIME, wants to take action against those who exceeds specified limit without mattering TIME INTERVAL between the messages. you can reply to question with 0

**Configuring the time:**
2m = 2 minutes
2h = 2 hours
2d = 2 days''', reply_markup= InlineKeyboardMarkup(soja) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("expf"):
            try:
                await cb.message.edit('''**Examples of setting floods**
**Example:**
Me: /setflood 10
Daisy: Please send expiration time [...]
Me: 5m (5 minutes)
DONE!

- /setfloodaction (action): Sets the action to taken when user exceeds flood limit''', reply_markup= InlineKeyboardMarkup(soja) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("action"):
            try:
                await cb.message.edit ('''**Currently supported actions:**
**Actions:**
ban
mute
kick
More soon™''', reply_markup= InlineKeyboardMarkup(soja) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("flood"):
            try:
                await cb.message.edit('''Help for **AntiFlood** module:

You know how sometimes, people join, send 100 messages, and ruin your chat? With antiflood, that happens no more!

Antiflood allows you to take action on users that send more than x messages in a row.

**Admins only:**
- /antiflood: Gives you current configuration of antiflood in the chat
- /antiflood off: Disables Antiflood
- /setflood (limit): Sets flood limit
- /setfloodaction [ban/kick/mute/tban/tmute]: Action to perform when user have exceeded flood limit. ban/kick/mute/tmute/tban Allowed

**Note:**
 - Value must be filled for tban and tmute!!
 It can be:
 5m = 5 minutes
 6h = 6 hours
 3d = 3 days
 1w = 1 week''', reply_markup= InlineKeyboardMarkup(auto) )
                message.stop_propagation()            
            except:
                return



        elif cb.data==("blist"):
            try:
                await cb.message.edit('''Help for **Blacklist** module:

**Yuriko's filters are the blacklist too **
- /addfilter [trigger] Select action: blacklists the trigger
- /delfilter [trigger] : stop blacklisting a certain blacklist trigger
- /filters: list all active blacklist filters

**Url Blacklist** 
- /geturl: View the current blacklisted urls
- /addurl [urls]: Add a domain to the blacklist. The bot will automatically parse the url.
- /delurl [urls]: Remove urls from the blacklist.

**Example:**
- /addblacklist the admins suck: This will remove "the admins suck" everytime some non-admin types it
- /addurl bit.ly: This would delete any message containing url "bit.ly"''',reply_markup= InlineKeyboardMarkup(back))
                message.stop_propagation()            
            except:
                return


        elif cb.data==("connect"):
            try:
                await cb.message.edit('''Help for **Connections** module:

Sometimes you need change something in your chat, like notes, but you don't want to spam in it, try connections, this allow you change chat settings and manage chat's content in personal message with Daisy.

**Available commands are:**
**Avaible only in PM:**
- /connect: Show last connected chats button for fast connection
- /connect (chat ID or chat nickname): Connect to chat by argument which you provided
- /reconnect: Connect to last connected chat before
- /disconnect: Disconnect from

**Avaible only in groups:**
- /connect: Direct connect to this group

**Other commands:**
- /allowusersconnect (on/off enable/disable): Enable or disable connection feature for regular users, for admins connections will be works always''', reply_markup= InlineKeyboardMarkup(back) )
                message.stop_propagation()            
            except:
                return





        elif cb.data==("dexp"):
            try:
                await cb.message.edit('''**Examples of Disabling Commands**

**Examples:**
/disable adminlist
It would disable usauge of /adminlist command in the chat!

/enable adminlist
This enables previously disable command /adminlist.''', reply_markup= InlineKeyboardMarkup(sed) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("disable"):
            try:
                await cb.message.edit('''Help for **Disabling** module:

Disabling module is allow you to disable certain commands from be executed by users.

**Available commands:**
- /disableable: Shows commands which can be disabled
- /disabled: Shows the all disabled commands of the chat
- /disable (command name): Disables the command. Command should be disable-able
- /enable (command name): Enables the disabled command back.
- /enableall: Enables all disabled commands''', reply_markup= InlineKeyboardMarkup(disable) )
                message.stop_propagation()            
            except:
                return





        elif cb.data==("feds"):
            try:
                await cb.message.edit('''**FEDERATIONS**

Own many groups? Cant ban spammers in all chats manually?
Well federations are built just for you,

Basically there is 2 reasons to use Federations:

1. You have many chats and want to ban users in all of them with 1 command
2. You want to subscribe to any of the antispam Federations to have your chat(s) protected.

In both cases Daisy can help you to do that.

Arguments types help:
(): required argument
(user): required but you can reply on any user's message instead
(file): required file, if file isn't provided you will be entered in file state, this means AllMight will wait file message from you. Type /cancel to leave from it.
(? ): additional argument

**Note: Yuriko's federations got updated. You can use old federations by using old infront of federation commands. Send /oldfedshelp for more help.**
  
''',reply_markup= InlineKeyboardMarkup(fedd) )
                message.stop_propagation()            
            except:
                return



        elif cb.data==("fadmin"):
            try:
                await cb.message.edit('''**Fed Admin Commands**

The following is the list of all fed admin commands. To run these, you have to be a federation admin in the current federation.

**Avaible for Federation admins and owners:**
- /fchatlist (?Fed ID) or /fchats (?Fed ID): Shows a list of chats in the your Federation list
- /fban (user) (?Fed ID) (?reason): Bans user in the Fed and Feds which subscribed on this Fed
- /sfban (user) (?Fed ID) (?reason): As above, but silently - means the messages about fbanning and replied message (if was provided) will be removed
- /unfban (user) (?Fed ID) (?reason): Unbans a user from a Federation

**Note: Yuriko' s federations got updated. You can use old federations by using old infront of federation commands. Send /oldfedshelp for more help.**''',reply_markup= InlineKeyboardMarkup(fedhai) )
                message.stop_propagation()            
            except:
                return


        elif cb.data==("fowner"):
            try:
                await cb.message.edit('''**Federation Owner Commands**

These are the list of available fed owner commands. To run these, you have to own the current federation.

**Only for Federation owner:**
- /fnew (name) or /newfed (name): Creates a new Federation
- /frename (?Fed ID) (new name): Renames your federation
- /fdel (?Fed ID) or /delfed (?Fed ID): Removes your Federation
- /fpromote (user) (?Fed ID): Promotes a user to the your Federation
- /fdemote (user) (?Fed ID): Demotes a user from the your Federation
- /fsub (Fed ID): Subscibes your Federation over provided
- /funsub (Fed ID): unsubscibes your Federation from provided
- /fsetlog (? Fed ID) (? chat/channel id) or /setfedlog (? Fed ID) (? chat/channel id): Set's a log chat/channel for your Federation
- /funsetlog (?Fed ID) or /unsetfedlog (?Fed ID): Unsets a Federation log chat\channel
- /fexport (?Fed ID): Exports Federation bans
- /fimport (?Fed ID) (file): Imports Federation bans

**Note: Yuriko s federations got updated. You can use old federations by using old infront of federation commands. Send /oldfedshelp for more help.**''',reply_markup= InlineKeyboardMarkup(fedhai) )
                message.stop_propagation()            
            except:
                return




        elif cb.data==("users"):
            try:
                await cb.message.edit('''**User Commands**

These commands do not require you to be admin of a federation. These commands are for general commands, such as looking up information on a fed, or checking a user's fbans.

**Only Chat owner:**
- /fjoin (Fed ID) or /joinfed (Fed ID): Joins current chat to provided Federation
- /fleave or /leavefed: Leaves current chat from the fed

**Avaible for all users:**
- /fcheck (?user): Check user s federation ban info
- /finfo (?Fed ID): Info about Federation

**Note: Yuriko s federations got updated. You can use old federations by using old infront of federation commands. Send /oldfedshelp for more help.**''',reply_markup= InlineKeyboardMarkup(fedhai) )
                message.stop_propagation()            
            except:
                return




        elif cb.data == "filters": 
            try:
                await cb.message.edit(MSG.FILTERS,reply_markup= InlineKeyboardMarkup(filter))
                message.stop_propagation()            
            except:
                return


        elif cb.data == "chutiya": 
            try:
                await cb.message.edit('''
**Buttons:**
Here you will know how to setup buttons in your note, welcome note, etc...

There are different types of buttons!

Due to current Implementation adding invalid button syntax to your note will raise error! This will be fixed in next major version.

**Did you know?**
You could save buttons in same row using this syntax
`[Button](btn{mode}:{args if any}:same)`
(adding :same like that does the job.)

**Button Note:**
Don't confuse this title with notes with buttons 😜

This types of button will allow you to show specific notes to users when they click on buttons!

You can save note with button note without any hassle by adding below line to your note ( Don't forget to replace notename according to you 😀)

`[Button Name](btnnote:notename)`

**URL Button:**
Ah as you guessed! This method is used to add URL button to your note. With this you can redirect users to your website or even redirecting them to any channel, chat or messages!

You can add URL button by adding following syntax to your note

`[Button Name](btnurl:https://your.link.here)`

**Button rules:**
Well in v2 we introduced some changes, rules are now saved seperately unlike saved as note before v2 so it require seperate button method!

You can use this button method for including Rules button in your welcome messages, filters etc.. literally anywhere*

You use this button with adding following syntax to your message which support formatting!
`[Button Name](btnrules)`''', reply_markup= InlineKeyboardMarkup(chutiya) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "vro": 
            try:
                await cb.message.edit('''
**Variables:**
Variables are special words which will be replaced by actual info

**Avaible variables:**
`{first}`: User's first name
`{last}`: User's last name
`{fullname}`: User's full name
`{id}`: User's ID
`{mention}`: Mention the user using first name
`{username}`: Get the username, if user don't have username will be returned mention
`{chatid}`: Chat's ID
`{chatname}`: Chat name
`{chatnick}`: Chat username''', reply_markup= InlineKeyboardMarkup(pro) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "genfil": 
            try:
                await cb.message.edit('''Help for **Auto Filters** Module:

**AUTO FILTERS**
Daisy Can filter content of a given channel automatically
**Currently support:**
    - Videos
    - Media
    - Documents
    - Music

**Setting up**
1) Add @YurikoRobot to your channel
2) Make bot admin with full permissions
2) Go back to your group

**Commands**
- /autofilter [Channel Username] : Add given channel to autofiltering
- /autofilterdel [Channel Username] : Remove given channel from auto filtering
- /autofilterdelall : Remove all channels from automatic filtering
- /autofiltersettings : Show settings panel about auto filtering channels

Original work is done by @Shubhanshutya''', reply_markup= InlineKeyboardMarkup(marja) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "clfil": 
            try:
                await cb.message.edit('''Help for **Classic Filters** Module:

Classic filters are just like marie's filter system. If you still like that kind of filter system
**Admin Only**
- /cfilter  : Every time someone says "word", the bot will reply with "message"
You can also include buttons in filters, example send /savefilter google in reply to Click Here To Open Google | [Button.url('Google', 'google.com')]
- /stopcfilter : Stop that filter.
- /stopallcfilters: Delete all filters in the current chat.
**Admin+Non-Admin**
- /cfilters: List all active filters in the chat

Please note classic filters can be unstable. We recommend you to use /addfilter''', reply_markup= InlineKeyboardMarkup(pro) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "ranfil": 
            try:
                await cb.message.edit('''Help for **Random Filters** Module:

**Random Filters**
Random filters can be used to give a random reply from a given set of commands

**Commands**:
- /randomfilter [filter name] [reply to message]: Set random filters
Note: Replies must be seperated with | or %%%

- /filters: See list of filters
- /stop [filter name]: Stop a filter

**Syntax**:
The correct syntax of a set of replies
"word/sentence one |word/sentence two"
Example: "Hi%%%Hello%%%how are you"

        ''', reply_markup= InlineKeyboardMarkup(marja) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "adfil": 
            try:
                await cb.message.edit('''Help for **Advanced Filters** Module:

**Advanced Filters (Admins):**
- /addfilter (word/sentence): This is used to add filters.
- /delfilter (word/sentence): Use this command to remove a specific filter.
- /delallfilters: As in command this is used to remove all filters of group.

**As of now, there is 6 actions that you can do:** 
- `Send a note`
- `Warn the user`
- `Ban the user`
- `Mute the user`
- `tBan the user`
- `tMute the user`

**A filter can support multiple actions !** 

Ah if you don't understand what this actions are for? Actions says bot what to do when the given word/sentence is triggered.
You can also use regex and buttons for filters. Check /buttonshelp to know more.

**Available for all users:**
- /filters or /listfilters

**Use of regex**
You can use regex with advanced filters
use "re:" at first of an filter to use regex
Example: /addfilter re:hi$ (This will only reply to word hi, not for words starting with hi)

You want to know all filter of your chat/ chat you joined? Use this command. It will list all filters along with specified actions !''', reply_markup= InlineKeyboardMarkup(pro) )

                message.stop_propagation()            
            except:
                return



        elif cb.data == "textfil": 
            try:
                await cb.message.edit('''Help for **Text Filters**:

**TEXT FILTERS** 
Text filters are for short and text replies
**Commands available** 
- /filter [KEYWORD] [REPLY TO MESSAGE] : Filters the replied message with given keyword.
- /stop [KEYWORD] : Stops the given filter.

**Difference between text filter and filter**
If you filtered word "hi" with /addfilter it filters all words including hi. 
**Future explained:**
    - When a filter added to hi as "hello" when user sent a message like "It was a hit" bot replies as "Hello" as word contain hi
    ** You can use regex to remove this if you like
Text filters won't reply like that. It only replies if word = "hi" (According to example taken) 
**Text filters can filter**
- `A single word`
- `A sentence`
- `A sticker`''', reply_markup= InlineKeyboardMarkup(marja) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "filters": 
            try:
                await cb.message.edit('''Help for **Filters** module:

**Filters Module**:
Filter module is great for everything! filter in here is used to filter words or sentences in your chat - send notes, warn, ban those!

**Yuriko filters comes under 4 types.**

1) **Advanced Filters** -  Built for send notes, warn, ban those who send a word/sentence. Support regex, Buttons, Formatting and variables

2) **Text Filters** - Text filters are for short and text replies

3) **Autofilters** -  Filter content of a given channel automatically

4) **Classic Filters** - Old marie type filters for classic lovers''',reply_markup= InlineKeyboardMarkup(filter) )
                message.stop_propagation()            
            except:
                return





        elif cb.data == "gpl": 
            try:
                await cb.message.edit('''
**Buttons:**
Here you will know how to setup buttons in your note, welcome note, etc...

There are different types of buttons!

Due to current Implementation adding invalid button syntax to your note will raise error! This will be fixed in next major version.

**Did you know?**
You could save buttons in same row using this syntax
`[Button](btn{mode}:{args if any}:same)`
(adding :same like that does the job.)

**Button Note:**
Don't confuse this title with notes with buttons 😜

This types of button will allow you to show specific notes to users when they click on buttons!

You can save note with button note without any hassle by adding below line to your note ( Don't forget to replace notename according to you 😀)

`[Button Name](btnnote:notename)`

**URL Button:**
Ah as you guessed! This method is used to add URL button to your note. With this you can redirect users to your website or even redirecting them to any channel, chat or messages!

You can add URL button by adding following syntax to your note

`[Button Name](btnurl:https://your.link.here)`

**Button rules:**
Well in v2 we introduced some changes, rules are now saved seperately unlike saved as note before v2 so it require seperate button method!

You can use this button method for including Rules button in your welcome messages, filters etc.. literally anywhere*

You use this button with adding following syntax to your message which support formatting!
    `[Button Name](btnrules)`''', reply_markup= InlineKeyboardMarkup(randi) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "vkl": 
            try:
                await cb.message.edit('''
**Variables:**
Variables are special words which will be replaced by actual info

**Avaible variables:**
`{first}`: User's first name
`{last}`: User's last name
`{fullname}`: User's full name
`{id}`: User's ID
`{mention}`: Mention the user using first name
`{username}`: Get the username, if user don't have username will be returned mention
`{chatid}`: Chat's ID
`{chatname}`: Chat name
`{chatnick}`: Chat username''', reply_markup= InlineKeyboardMarkup(randi) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "security": 
            try:
                await cb.message.edit('''
**Welcome security:**
- /welcomesecurity (level)
Turns on welcome security with specified level, either button or captcha.
Setting up welcome security will give you a choice to customize join expiration time aka minimum time given to user to verify themselves not a bot, users who do not verify within this time would be kicked!

- /welcomesecurity (off/no/0): Disable welcome security
- /setsecuritynote: Customise the "Please press button below to verify themself as human!" text
- /delsecuritynote: Reset security text to defaults

**Available levels:**
- button: Ask user to press "I'm not a bot" button
- math: Asking to solve simple math query, few buttons with answers will be provided, only one will have right answer
- captcha: Ask user to enter captcha

If welcome security is enabled, user will be welcomed with security text, if user successfully verify self as user, he/she will be welcomed also with welcome text in his PM (to prevent spamming in chat).

If user didn't verified self for 24 hours he/she will be kicked from chat.''', reply_markup= InlineKeyboardMarkup(randi)) 
                message.stop_propagation()            
            except:
                return


        elif cb.data == "chup": 
            try:
                await cb.message.edit('''
**Welcome mutes:**
- /welcomemute (time): Set welcome mute (no media) for X time
- /welcomemute (off/no): Disable welcome mute''', reply_markup= InlineKeyboardMarkup(randi) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "fuk": 
            try:
                await cb.message.edit('''
**Purges:**
- /cleanwelcome (on/off): Deletes old welcome messages and last one after 45 mintes
- /cleanservice (on/off): Cleans service messages (user X joined)''', reply_markup= InlineKeyboardMarkup(randi) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "tkl": 
            try:
                await cb.message.edit('''
**Addings buttons and variables to welcomes or security text:**
Buttons and variables syntax is same as notes buttons and variables.
Click on **Button Help** and **Variable Help** to get started with using it.

Settings images, gifs, videos or stickers as welcome:
Saving attachments on welcome is same as saving notes with it, read the notes help about it. But keep in mind what you have to replace /save to /setwelcome

**Examples:**
- `Get the welcome message without any formatting`
    -> `/welcome raw`''', reply_markup= InlineKeyboardMarkup(randi) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "welcome": 
            try:
                await cb.message.edit('''Help for **Greetings** module:

**Available commands:**
**General:**
- /setwelcome or /savewelcome: Set welcome
- /setwelcome (on/off): Disable/enabled welcomes in your chat
- /welcome: Shows current welcomes settings and welcome text
- /resetwelcome: Reset welcomes settings''', reply_markup= InlineKeyboardMarkup(randi) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "image": 
            try:
                await cb.message.edit('''Help for **Image Editor** module:

**IMAGE EDITOR** 
Yuriko have some advanced image editing tools inbuilt
Bright, Circle, RemBG, Blur, Border, Flip, Glitch, Sticker maker and more

- /edit [reply to image]: Open the image editor

**Logo Maker** 
Create Beautiful logos for your profile pictures from Daisy. 

- /logo [TEXT]: Create a logo 
- /logohq [TEXT]: Create a HQ logo 
- /brandcrowd [TEXT : TYPE]: Create logos from brandcrowd.com (Only work on groups)

Ex:
  `/logo Shubhanshu'
  `/brandcrowd Yuriko:Robot`
  
Logo Maker is Powered by @SingleDevelopers
Special Thanks to @TroJanzHEX for Image Editor''',reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "backup": 
            try:
                await cb.message.edit('''Help for **Backups** module:

Sometimes you want to see all of your data in your chats or you want to copy your data to another chats or you even want to swift bots, in all these cases imports/exports for you!

**Available commands:**
- /export: Export chat's data to JSON file
- /import: Import JSON file to chat

**Notes:** Exporting / importing avaible every 2 hours to prevent flooding.''', reply_markup= InlineKeyboardMarkup(ufuk)) 
                message.stop_propagation()            
            except:
                return



        elif cb.data == "inline": 
            try:
                await cb.message.edit('''Help for **Inline** module:

**INLINE BOT SERVICE OF @DAISYXBOT**  

I'm more efficient when added as group admin. By the way these commands can be used by anyone in a group via inline.

**Syntax**
@YurikoRobot [command] [query]

**Commands Available**
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
- pokedex [TEXT]: Pokemon Search''',reply_markup= InlineKeyboardMarkup(ohk) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "langtools": 
            try: 
                await cb.message.edit('''Help for **Lang-Tools** module:

- /tr language code or /tr language code , text: Type in reply to a message or (/tr language code , text) to get it's translation in the destination language
- /define text: Type the word or expression you want to search
For example /define lesbian
- /spell: while replying to a message, will reply with a grammar corrected version
- /forbesify: Correct your punctuations better use the advanged spell module
- /synonyms word: Find the synonyms of a word
- /antonyms word: Find the antonyms of a word''',reply_markup= InlineKeyboardMarkup(ufuk) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "skem": 
            try:
                await cb.message.edit('''Help for **Languages** module:

This module is dedicated towards utlising Yuriko localization feature!

**Available commands:**
- /lang: Shows a list of avaible languages
- /lang (language codename): Sets a language

**Example:** /lang
Daisy will send you bunch of inline buttons where you can select your prefered language interatively without any hassles!''',reply_markup= InlineKeyboardMarkup(ufuk) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "typeloc": 
            try:
                await cb.message.edit('''Help For **Locks** Module

Is users sending anoying things in group.. No longer ned to worry. Locks can handle it
You can Use this feature to block users from sending specific message types to your group!

**Locks are two types**
1) Normal Locks: Delete user's message when locked content is sent
2) Permission Locks: Lock permissions of group to block users from sending specific message types.
`See Locktypes for more info`

Available commands are:
- /locks or /chatlocks: Use this command to know current state of your locks in your group!
- /locktypes: Use this command to get available locktypes for chat
- /lock (locktype): Locks a type of messages
- /unlock (locktype): Unlocks a type of message''', reply_markup= InlineKeyboardMarkup(lock) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "typelocbsc": 
            try:
                await cb.message.edit('''**Locktypes**
**Basic Locktypes available for a chat: **

video
audio
document
forward
photo
sticker
gif
games
album
voice
video_note
contact
location
address
reply
message
comment
edit
mention
inline
polls
dice
buttons
media
email
url
bots
all

Yuriko will delete user's message if locked content is sent
        ''', reply_markup= InlineKeyboardMarkup(lock) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "typelocprm": 
            try:
                await cb.message.edit('''**Locktypes**

**Permissions Locks Available for a chat:**

send_messages
send_stickers
send_gifs
send_media
send_games
send_inline
url_prev
send_polls
change_info
invite_user
pin_messages
all_permissions
        ''', reply_markup= InlineKeyboardMarkup(lock) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "url": 
            try:
                await cb.message.edit('''Help for **Locks** Module

**Url Lock** 
Block links sent by users in your group

**Commands:**
- /urllock [on/off]: Enable/Disable URL Lock''', reply_markup= InlineKeyboardMarkup(lock) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "locks": 
            try:
                await cb.message.edit('''Help for **Locks** module:

Use this feature to block users from sending specific message types to your group!

**Basic Locks**

**Comands:**
- /locks or /locktypes: Use this command to know current state of your locks in your group!
- /lock (locktype): Locks a type of messages
- /unlock (locktype): Unlocks a type of message''', reply_markup= InlineKeyboardMarkup(lock) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "monkey": 
            try:
                await cb.message.edit('''Help for **Maths** module:

Solves complex math problems using https://newton.now.sh and python math module
- /simplify- Math /math 2^2+2(2)
- /factor - Factor /factor x^2 + 2x
- /derive - Derive /derive x^2+2x
- /integrate - Integrate /integrate x^2+2x
- /zeroes - Find 0's /zeroes x^2+2x
- /tangent - Find Tangent /tangent 2lx^
- /area - Area Under Curve /area 2:4lx^3`
- /cos - Cosine /cos pi
- /sin - Sine /sin 0
- /tan - Tangent /tan 0
- /arccos - Inverse Cosine /arccos 1
- /arcsin - Inverse Sine /arcsin 0
- /arctan - Inverse Tangent /arctan 0
- /abs - Absolute Value /abs -1
- /log* - Logarithm /log 2l8

Keep in mind, To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).''',reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return

        elif cb.data == "shdlr": 
            try:
                await cb.message.edit('''Help for **Message Scheduler** module:

You can Shedule messages or set reminders with this module
**Commands**
 - /remind <(date) (time)|zone|reason>: sets a alarm/reminder 
**Syntax:** `/remind 01/01/2022 10:00:00 AM | America/New_York | breakfast`
**NOTE:** Please turn on notifications for @YurikoRobot otherwise you will not get notification for the reminder

**Commands**
 - /schedule <(date) (time)|zone|reason>: sets a scheduled message
**Syntax:** `/schedule 01/01/2022 10:00:00 AM | America/New_York | Hi guys`
!''',reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "memes": 
            try: 
                await cb.message.edit('''Help for **Memes** module:

**Some memes command, find it all out yourself !**

- /owo: OWO de text
- /stretch: STRETCH de text
- /clapmoji: Type in reply to a message and see magic
- /bmoji: Type in reply to a message and see magic
- /copypasta: Type in reply to a message and see magic
- /vapor: owo vapor dis
- /shout text: Write anything that u want it to should
- /zalgofy: reply to a message to glitch it out!
- /table: get flip/unflip :v.
- /decide: Randomly answers yes/no/maybe
- /bluetext: Must type for fun
- /toss: Tosses A coin
- /abuse: Abuses the cunt
- /insult: Insult the cunt
- /slap: Slaps the cunt
- /roll: Roll a dice.
- /rlg: Join ears,nose,mouth and create an emo ;-;
- /react: Check on your own
- /rhappy: Check on your own
- /rangry: Check on your own
- /angrymoji: Check on your own
- /crymoji: Check on your own
- /cowsay, /tuxsay , /milksay , /kisssay , /wwwsay , /defaultsay , /bunnysay , /moosesay , /sheepsay , /rensay , /cheesesay , /ghostbusterssay , /skeletonsay text: Returns a stylish art text from the given text
- /deepfry: Type this in reply to an image/sticker to roast the image/sticker
- /figlet: Another Style art
- /dice: Roll A dice
- /dart: Throw a dart and try your luck
- /basketball: Try your luck if you can enter the ball in the ring
- /type text: Make the bot type something for you in a professional way
- /carbon text: Beautifies your text and enwraps inside a terminal image [ENGLISH ONLY]
- /sticklet text: Turn a text into a sticker
- /fortune: gets a random fortune quote
- /quotly: Type /quotly in reply to a message to make a sticker of that
- /animate: Enwrap your text in a beautiful anime''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "gaana": 
            try:
                await cb.message.edit('''Help for **Music** module:

/video query: download video from youtube.  
/saavn query: download song from saavn. 
/music query: download song from yt servers. (API BASED) 
/shazam [reply to audio]: Do a reverse search from a part of audio
/lyrics song name : This plugin searches for song lyrics with song name.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "soja":  
            try: 
                await cb.message.edit('''Help for **Night Mode** module:

**The Night mode**
Tired managing group all time
Close your group at at a given time and open back at a given time

**Turning on**
- /nightmode [ON/OFF]: Enable/Disable Night Mode [default settings*].
- /setnightmode [TIME ZONE] | Start time [see example] | End time [see example]
Example:
    /setnightmode Asia/kolkata | 01:30:00 AM | 02:35:00 AM
    
Note: remember chat permissions messages,gifs,games,inline,invite will be allowed when opening chat

*Default settings: Close your group at 12.00 a.m. and open back at 6.00 a.m.(IST)''',reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return

        elif cb.data == "meth":
            try:
                await cb.message.edit("""
Solves complex math problems using https://newton.now.sh and python math module

 - /math- Math /math 2^2+2(2)
 - /factor - Factor /factor x^2 + 2x
 - /derive - Derive /derive x^2+2x
 - /integrate - Integrate /integrate x^2+2x
 - /zeroes - Find 0's /zeroes x^2+2x
 - /tangent - Find Tangent /tangent 2lx^
 - /area - Area Under Curve /area 2:4lx^3`
 - /cos - Cosine /cos pi
 - /sin - Sine /sin 0
 - /tan - Tangent /tan 0
 - /arccos - Inverse Cosine /arccos 1
 - /arcsin - Inverse Sine /arcsin 0
 - /arctan - Inverse Tangent /arctan 0
 - /abs - Absolute Value /abs -1
 - /log* - Logarithm /log 2l8
 
Keep in mind, To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).
""", reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return
            
        elif cb.data == "zepper":
            try:
                await cb.message.edit("""
**ZIPPER**

- /zip: reply to a telegram file to compress it in .zip format
- /unzip: reply to a telegram file to decompress it from the .zip format""", reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "ded": 
            try:
                await cb.message.edit('''
**Buttons:**
Here you will know how to setup buttons in your note, welcome note, etc...

There are different types of buttons!

Due to current Implementation adding invalid button syntax to your note will raise error! This will be fixed in next major version.

**Did you know?**
You could save buttons in same row using this syntax
`[Button](btn{mode}:{args if any}:same)`
(adding :same like that does the job.)

**Button Note:**
Don't confuse this title with notes with buttons 😜

This types of button will allow you to show specific notes to users when they click on buttons!

You can save note with button note without any hassle by adding below line to your note ( Don't forget to replace notename according to you 😀)

`[Button Name](btnnote:notename)`

**URL Button:**
Ah as you guessed! This method is used to add URL button to your note. With this you can redirect users to your website or even redirecting them to any channel, chat or messages!

You can add URL button by adding following syntax to your note

`[Button Name](btnurl:https://your.link.here)`

**Button rules:**
Well in v2 we introduced some changes, rules are now saved seperately unlike saved as note before v2 so it require seperate button method!

You can use this button method for including Rules button in your welcome messages, filters etc.. literally anywhere*

You use this button with adding following syntax to your message which support formatting!
`[Button Name](btnrules)`''', reply_markup= InlineKeyboardMarkup(inuka) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "ofp": 
            try:
                await cb.message.edit('''
**Variables:**
Variables are special words which will be replaced by actual info

**Avaible variables:**
`{first}`: User's first name
`{last}`: User's last name
`{fullname}`: User's full name
`{id}`: User's ID
`{mention}`: Mention the user using first name
`{username}`: Get the username, if user don't have username will be returned mention
`{chatid}`: Chat's ID
`{chatname}`: Chat name
`{chatnick}`: Chat username''', reply_markup= InlineKeyboardMarkup(inuka) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "alias": 
            try:
                await cb.message.edit('''
**Notes aliases:**
You can save note with many names, example:
`/save name1|name2|name3`
That will save a note with 3 different names, by any you can /get note, that can be useful if users in your chat trying to get notes which exits by other names.


**Removing many notes per one request:**
To remove many notes you can use the /clear command, just place all note names which you want to remove as argument of the command, use | as seprator, for example:
`/clear note1|note2|note3`


**Notes buttons and variables:**
Notes support inline buttons, Click on **Button Help** below to get started with using it. 
Variables are special words which will be replaced by actual info like if you add {id} in your note it will be replaced by user ID which asked note.''', reply_markup= InlineKeyboardMarkup(inuka) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "mat": 
            try:
                await cb.message.edit('''
**Notes formatting and settings:**
Every note can contain special settings, for example you can change formatting method to HTML by %PARSEMODE_HTML and fully disable it by %PARSEMODE_NONE ( By default formatting is Markdown or the same formatting Telegram supports )

%PARSEMODE_(HTML, NONE): Change the note formatting
%PREVIEW: Enables the links preview in saved note''', reply_markup= InlineKeyboardMarkup(inuka) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "inuka": 
            try:
                await cb.message.edit('''
**Examples:**
**An example of how to save a note would be via:**
`/save data` This is example note!
Now, anyone using `/get data`, or `#data` will be replied to with This is example note!.

**Saving pictures and other non-text data:**
If you want to save an image, gif, or sticker, or any other data, do the following:
`/save` word while replying to a sticker or whatever data you'd like. Now, the note at #word contains a sticker which will be sent as a reply.

**Removing many notes per one request:**
To remove many notes you can use the /clear command, just place all note names which you want to remove as argument of the command, use | as seprator, for example:
    `/clear note1|note2|note3`''', reply_markup= InlineKeyboardMarkup(inuka) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "notes": 
            try:
                await cb.message.edit('''Help for **Notes** module:

Sometimes you need to save some data, like text or pictures. With notes, you can save any types of Telegram's data in your chats.
Also notes perfectly working in PM with Daisy.

**Available commands:**
- /save (name) (data): Saves the note.
- #(name) or /get (name): Get the note registered to that word.
- /clear (name): deletes the note.
- /notes or /saved: Lists all notes.
- /noteinfo (name): Shows detailed info about the note.
- /search (search pattern): Search text in notes
- /clearall: Clears all notes

**Only in groups:**
- /privatenotes (on/off): Redirect user in PM to see notes
- /cleannotes (on/off): Will clean old notes messages''', reply_markup= InlineKeyboardMarkup(inuka) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "pin_kk": 
            try:
                await cb.message.edit('''Help for **Pinning** module:

**Basic Pins** 
- /pin: silently pins the message replied to - add 'loud' or 'notify' to give notifs to users.
- /unpin: unpins the currently pinned message'
- /unpinall unpin all messages.

**Other** 
- /permapin [reply]: Pin a custom message through the bot. This message can contain markdown, buttons, and all the other cool features.
- /antichannelpin [yes/no/on/off]: Don't let telegram auto-pin linked channels. If no arguments are given, shows current setting.
- /cleanlinked [yes/no/on/off]: Delete messages sent by the linked channel.

**Note:** When using antichannel pins, make sure to use the /unpin command, instead of doing it manually. Otherwise, the old message will get re-pinned when the channel sends any messages.''', reply_markup= InlineKeyboardMarkup(cheator) )
                message.stop_propagation()            
            except:
                return




        elif cb.data == "tax": 
            try:
                await cb.message.edit('''**Syntax For Polling Module**
**Syntax**  -
- /poll [poll-id] question | True@optionnumber/False [True/False] [True/False] [option1] [option2] ... upto [option10]''', reply_markup= InlineKeyboardMarkup(dhoka) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "stpl": 
            try:
                await cb.message.edit('''Help for **Poll** Module
**To stop a poll** 
Reply to the poll with `/stoppoll [poll-id]` to stop the poll
**Fogot poll id** 
- /forgotpollid - to reset poll''', reply_markup= InlineKeyboardMarkup(dhoka) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "llexp": 
            try:
                await cb.message.edit('''Help for **Poll** module
**Examples**  -
- /poll 12345 | am i cool? | False False False yes no`
- /poll 12345 | am i cool? | True@1 False False yes no`''', reply_markup= InlineKeyboardMarkup(dhoka) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "poll": 
            try:
                await cb.message.edit('''Help for **Polls** module:

You can now send polls anonymously with Daisy
Here is how you can do it:
**Parameters**  -
- poll-id - a poll id consists of an 5 digit random integer, this id is automatically removed from the system when you stop your previous poll
- question - the question you wanna ask
- [True@optionnumber/False](1) - quiz mode, you must state the correct answer with @ eg: True@ or True@2
- [True/False](2) - public votes
- [True/False](3) - multiple choice''', reply_markup= InlineKeyboardMarkup(dhoka) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "report": 
            try:
                await cb.message.edit('''Help for **Reports** module:

We're all busy people who don't have time to monitor our groups 24/7. But how do you react if someone in your group is spamming?

Presenting reports; if someone in your group thinks someone needs reporting, they now have an easy way to call all admins.

**Available commands:**
- /report (?text): Reports
- @admins: Same as above, but not a clickable

**TIP:** You always can disable reporting by disabling module''', reply_markup= InlineKeyboardMarkup(back) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "rss": 
            try:
                await cb.message.edit('''Help for **RSS Feed** module:

- /addrss : Add Rss to the chat
- /testrss : Test RSS Of The Chat
- /listrss : List all RSS Of The Chat
- /delrss : Delete RSS From The Chat
- /delallrss : Deletes All RSS From The Chat''', reply_markup= InlineKeyboardMarkup(ufuk) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "rules": 
            try:
                await cb.message.edit('''Help for **Rules** module:

**Available Commands:**
- /setrules (rules): saves the rules (also works with reply)
- /rules: Shows the rules of chat if any!
- /resetrules: Resets group's rules''', reply_markup= InlineKeyboardMarkup(back) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "search": 
            try:
                await cb.message.edit('''Help for **Search** module:

- /google text: Perform a google search
- /so - Search For Something On Stack OverFlow
- /gh - Search For Something On GitHub
- /yts - Search For Something On YouTub
- /app appname: Searches for an app in Play Store and returns its details.
- /reverse [reply to img] - Do a reverse search of the replied image
- /search_img - Search Images''', reply_markup= InlineKeyboardMarkup(ufuk) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "sticker": 
            try:
                await cb.message.edit('''Help for **Stickers** module:

Stickers are the best way to show emotion.

**Available commands:**
- /searchsticker: Search stickers for given query.
- /packinfo: Reply to a sticker to get it's pack info
- /getsticker: Uploads the .png of the sticker you've replied to
- /sticker_id : Reply to Sticker for getting sticker Id. 
- /kang [Emoji for sticker] [reply to Image/Sticker]: Kang replied sticker/image.
- /rmkang [REPLY]: Remove replied sticker from your kang pack.''', reply_markup= InlineKeyboardMarkup(ufuk) )
                message.stop_propagation()            
            except:
                return


        # |------------------------------------------------------------------------------------------------|


        elif cb.data == "isc": 
            try:
                await cb.message.edit('''Help For **Misc** Module:''', reply_markup= InlineKeyboardMarkup(misc) )
                message.stop_propagation()            
            except:
                return





        elif cb.data == "ttf": 
            try:
                await cb.message.edit('''Help for **Open/ttf** Module:
**Available Commands**:
- /open : it's used to open any file via reply to file. 
- /ttf : it's used to make any text to file.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "checker": 
            try:
                await cb.message.edit('''Help for **CC Checker** Module:

**Available Commands**:
- /au [cc]: Stripe Auth given CC
- /pp [cc]: Paypal 1$ Guest Charge
- /ss [cc]: Speedy Stripe Auth
- /ch [cc]: Check If CC is Live
- /bin [bin]: Gather's Info About the bin
- /gen [bin]: Generates CC with given bin
- /key [sk]: Checks if Stripe key is Live

**Note:** Format of cc is ccnum|mm|yy|cvv
    **Privacy warning:** Don't check any of your personal CC's.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "string": 
            try:
                await cb.message.edit('''Help for **Channel Tools** Module:
        **Coming Soon''', reply_markup= InlineKeyboardMarkup(buk) )
                message.stop_propagation()            
            except:
                return




        elif cb.data == "history": 
            try:

                await cb.message.edit('''Help for **Name History** Module:

**Available Commands**:
- /namehistory [REPLY]: Get the Username and Name history of user.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "send": 
            try:
                await cb.message.edit('''Help for **Send** Module:

**Commands**:
- /send [MESSAGE]: Send given text by bot.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "urtol": 
            try:
                await cb.message.edit('''Help for **Url Tools** Module:

**Available Commands**:
- /short (url): Shortify given url.
- /getip (url): Displays information about an IP / domain.
- /direct (url): Generates direct links from the sourceforge.net
- /up [reply to url]: Upload files from replied url 
- /plink [reply to file]: Get direct download link of replied file via transfer.sh
- /tmpninja [reply to file]: Get direct download url of replied file via tmp.ninja''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return

        elif cb.data == "mosam": 

            try:
                await cb.message.edit('''Help for **Weather** Module:

**Available Commands**:
- /weather (city name) : Gives weather forcast
- /weatherimg (city name) : Gives weather image''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "phone": 
            try:
                await cb.message.edit('''Help for **Phone Info** Module:

**Available Commands**:
- /phone [phone no]: Gathers no info (Use with country code)''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "paisa": 

            try:
                await cb.message.edit('''Help for **Currency** Module:

**Commands**:
- /cash : currency converter
Example syntax: `/cash 1 USD INR`''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return




        elif cb.data == "book": 

            try:
                await cb.message.edit('''Help for **Book** Module:

**Available commands:**
- /book book name : Usage :Gets Instant Download Link Of Given Book.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "fake": 
            try:
                await cb.message.edit('''Help for **Fake Info** Module:

**Commands**:
- /fakegen : Generates Fake Information
- /picgen : generate a fake pic''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "basic": 

            try:
                await cb.message.edit('''Help for **Basic** Module:

**Available commands:**
- /github (username): Returns info about a GitHub user or organization.
- /wiki (keywords): Get wikipedia articles just using this bot.
- /imdb: Search for a movie
- /cancel: Disables current state. Can help in cases if DaisyX ♕ not responing on your cb.message.
- /id: get the current group id. If used by replying to a message, gets that user's id.
- /info: get information about a user.
- /paste: Pase the text/file in nekobin
- /gps: Find a location''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        # |-------------------------------------------------------------------------------------------------|

        elif cb.data == "vehla": 
            try:
                await cb.message.edit('''Help for **Extras** Module''', reply_markup= InlineKeyboardMarkup(xlm)) 
                message.stop_propagation()            
            except:
                return



        elif cb.data == "qr": 

            try:
                await cb.message.edit('''Help for **Qr Code** Module:

**Commands**
- /getqr - Get text in qr.
- /makeqr - Make a qr code.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "karma": 

            try:
                await cb.message.edit('''Help for **Karma** Module:

**KARMA**
[UPVOTE] - Use upvote keywords like "+", "+1", "thanks" etc to upvote a cb.message.
[DOWNVOTE] - Use downvote keywords like "-", "-1", etc to downvote a cb.message.

- /karma [ON/OFF]: Enable/Disable karma in group. 
- /karma [Reply to a message]: Check user's karma
- /karma: Chek karma list of top 10 users''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return




        elif cb.data == "country": 

            try:
                await cb.message.edit('''Help for **Country** Module:

**Commands**
- /country [country name]*:* Gathering info about given country''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "covid": 
            try:
                await cb.message.edit('''Help for **Covid** Module:

**Commands**     
- /covid - To Get Global Stats of Covid.
- /covid [COUNTRY] - To Get Stats of A Single Country.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "cricket": 
            try:
                await cb.message.edit('''Help for **Cricket Score** Module:

**MATCH INFO**     
- /cs - Gathers match information (globally)''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "torrent": 
            try:
                await cb.message.edit('''Help for **Torrent** Module:

**Available Commands**
- @YurikoRobot torrent [QUERY]: Search for torrent links''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "t2s": 
            try:
                await cb.message.edit('''Help for **Text To Speech** Module:

**Commands**
- /tts: Reply to any message to get text to speech output
- /stt: Type in reply to a voice message(english only) to extract text from it.''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "virus": 
            try:
                await cb.message.edit('''Help for **Virus Scan** Module:

**Commands**
- /scanit: Scan a file for virus (MAX SIZE = 3MB)''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "paste": 
            try:
                await cb.message.edit('''Help for **Paste** Module:

**Commands**
- /paste [reply]
Usage: Create a paste or a shortened url using nekobin (https://nekobin.com)''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "graph": 
            try:
                await cb.message.edit('''Help for **Telegraph** Module:

**Available Commands for Telegraph**
- /telegraph media : To Make Link of Any Image Or MP4 video. 
- /telegraph text : To make Link of Any Text Written. ''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "arbon": 
            try:
                await cb.message.edit('''Help for **Carbon** Module:

**Commands**
- /carbon : make carbon of any text''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "tugk": 
            try:
                await cb.message.edit('''Help for **Date Time** Module:

**Commands**
- /datetime [timezone]: Get the present date and time information
You can check out this [link](https://timezonedb.com/time-zones) for the available timezones''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "afk": 
            try:
                await cb.message.edit('''Help for **Afk** Module;

**Available Commands in AFK**
- /afk reason : mark yourself as AFK(Away From Keyboard)''', reply_markup= InlineKeyboardMarkup(skem)) 
                message.stop_propagation()            
            except:
                return



        elif cb.data == "rlock": 
            try:
                await cb.message.edit('''Help for **Url Lock** Module:

**Available Commads in Url Lock**
Block links sent by users in your group 
- /urllock [on/off]: Enable/Disable URL Lock''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return


        elif cb.data == "couple": 
            try:
                await cb.message.edit('''Help for **Couples** Module:

It's just a fun module for having little fun. 

**Couples**
- /couple: Choose a random couple of the day''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return



        elif cb.data == "encrypt": 
            try:
                await cb.message.edit('''Help for **Encrypt Text** Module:

**Encrypt text**
- /encrypt [reply to text]: Encrypt replied text
- /decrypt [reply to encrypted]: Decrypt text''', reply_markup= InlineKeyboardMarkup(skem) )
                message.stop_propagation()            
            except:
                return

        else:
            return cb.message.continue_propagation()
    except:
        print("send help error")
        return cb.message.continue_propagation()
    
    
    
    
    

# ----------------------------- COMMANDS ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- COMMANDS ----------------------------------------------------------
# ----------------------------- COMMANDS ----------------------------------------------------------------------------------------
# ----------------------------------------------------------- COMMANDS ----------------------------------------------------------



@pbot.on_message(filters.command(["start", "start@YurikoRobot","yurikostart"]) & filters.private)
async def sjs(client,message):
      if len(message.command) < 2:
        await message.reply(MSG.START, reply_markup= InlineKeyboardMarkup(lover))
      else:
        return message.continue_propagation()

@pbot.on_message(filters.command(["start", "start@YurikoRobot","yurikostart"]) & ~filters.private & ~filters.channel)
async def sjs(client,message):
    try:
        await message.reply("**Heya, Yuriko here :) PM me if you have any questions how to use me!**")       
    except:
        return

@pbot.on_message(filters.command(["help", "help@YurikoRobot","yurikohelp"]) & filters.private)
async def _w(client,message):
    try:
        await message.reply(MSG.HLP, reply_markup= InlineKeyboardMarkup(kk), disable_web_page_preview =True)
    except:
        return
    
@pbot.on_message(filters.command(["help", "help@DaisyXBot", "daisyhelp"]) & ~filters.private & ~filters.channel)
async def _ws(client,message):
    try:
        await message.reply("**Click me for help!**", reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("Click me for help",url = "t.me/DaisyXBot?start=help")]]))
    except:
        return

@pbot.on_message(filters.private & filters.text)
async def _(client,message):
    if message.text == "/start help" :
        try:
            await message.reply(MSG.HLP, reply_markup= InlineKeyboardMarkup(kk), disable_web_page_preview =True)
        except:
            return
    elif message.text == "/start tutorial" :
        try:
            await message.reply(MSG.TUTORIAL_TEXT, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Quick Setup Guide",callback_data="pm_tutorial")]]))
        except:
            return
    else:
        return message.continue_propagation()

    
    
# THIS IS WHAT WE CALL GET FUCKEDDD......................................................................... FUCKING HELP MENU OVER .......................................  
