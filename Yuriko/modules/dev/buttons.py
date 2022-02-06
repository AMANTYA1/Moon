import os
from pyrogram.types import *

class Buttons():
  NEW_PROJECT_BUTTONS = InlineKeyboardMarkup(
             [[
                InlineKeyboardButton("Admins ", callback_data="admin"),
                InlineKeyboardButton("Approoval", callback_data="aproval"),
                InlineKeyboardButton("Android ", callback_data="android"),
              ],
              [
                InlineKeyboardButton("Anime ",callback_data="anime"),
                InlineKeyboardButton("AntiFlood",callback_data="flood"),
                InlineKeyboardButton("Anti-Promo", callback_data="promogard"),
              ],
              [
                InlineKeyboardButton("AntiArabic", callback_data="antgard"), 
                InlineKeyboardButton("Bans", callback_data="ban_kk"),
                InlineKeyboardButton("Blacklist ", callback_data="blist"),  
              ],  
              [
                InlineKeyboardButton("Books", callback_data="book"),              
                InlineKeyboardButton("Channel Tools",callback_data="chtool"),                
                InlineKeyboardButton("Connections ",callback_data="connect"),
              ],  
              [
                InlineKeyboardButton("Carbon", callback_data="arbon"),
                InlineKeyboardButton("Cricket Score", callback_data="cricket"),                
                InlineKeyboardButton("Country", callback_data="country"),
              ],  
              [
                InlineKeyboardButton("CC Checker", callback_data="checker"),
                InlineKeyboardButton("Covid", callback_data="covid"),
                InlineKeyboardButton("Chatbot",callback_data="chatbot"),        
              ],  
              [
                InlineKeyboardButton("Cleans/Purges", callback_data="clean_kk"),                
                InlineKeyboardButton("Currency", callback_data="paisa"),
                InlineKeyboardButton("Date Time", callback_data="tugk"),
              ],  
              [
                InlineKeyboardButton("Disabling",callback_data="disable"),                
                InlineKeyboardButton("Fake Info", callback_data="fake"),                    
                InlineKeyboardButton("Federations ", callback_data="feds"),
              ],  
              [
                InlineKeyboardButton("Filters ",callback_data="filters"),                
                InlineKeyboardButton("Force Subscribe",callback_data="fsub"),                    
                InlineKeyboardButton("Greetings",callback_data="welcome"),
              ],  
              [
                InlineKeyboardButton("Global Mode", callback_data="globlgard"),                
                InlineKeyboardButton("Inline",callback_data="inline"),                
                InlineKeyboardButton("Image Editor ", callback_data="image"),
              ],  
              [
                InlineKeyboardButton("Karma", callback_data="karma"),
                InlineKeyboardButton("Lang-Tools ", callback_data="langtools"),                
                InlineKeyboardButton("Languages",callback_data="skem"),
              ],  
              [
                InlineKeyboardButton("Memes ",callback_data="memes"),
                InlineKeyboardButton("Math",callback_data="meth"),
                InlineKeyboardButton("Mute", callback_data="muta"),
              ],  
              [
                InlineKeyboardButton("Name History", callback_data="history"),                
                InlineKeyboardButton("Notes",callback_data="notes"),
                InlineKeyboardButton("Night Mode", callback_data="soja"),
              ],  
              [
                InlineKeyboardButton("No Bots Mode", callback_data="nobgard"),
                InlineKeyboardButton("NSFW Guard", callback_data="nsgard"),
                InlineKeyboardButton("Paste", callback_data="paste"),
              ],  
              [
                InlineKeyboardButton("Phone Info", callback_data="phone"),
                InlineKeyboardButton("Pins", callback_data="pin_kk"),
                InlineKeyboardButton("Promotes/Demotes", callback_data="promote"),
              ],
                              # W H O  T H E  F U C K  A D D E D  T H I S  M U C H  O F  F E A T U R E S 
               
               # I  H A T E  D A I S Y
               
              [
                InlineKeyboardButton("Polls", callback_data="poll"),
                InlineKeyboardButton("Qr Code", callback_data="qr"),
                InlineKeyboardButton("Open/ttf", callback_data="ttf"),
        #       InlineKeyboardButton("Other", callback_data="other_kk"),
              ],
              [
                InlineKeyboardButton("Reports", callback_data="report"),
                InlineKeyboardButton("RSS Feed",callback_data="rss"),
                InlineKeyboardButton("Rules",callback_data="rules"),
              ],
                              # W H O  T H E  F U C K  A D D E D  T H I S  M U C H  O F  F E A T U R E S 
               
               # I  H A T E  D A I S Y               
              [
                InlineKeyboardButton("Search", callback_data="search"),
                InlineKeyboardButton("Stickers", callback_data="sticker"),
                InlineKeyboardButton("Send", callback_data="send"),
              ],
              [
                InlineKeyboardButton("Tag Alert",callback_data="tgalrt"),                
                InlineKeyboardButton("Telegraph", callback_data="graph"),
                InlineKeyboardButton("Scheduler", callback_data="shdlr"),

              ],
              [
                InlineKeyboardButton("Text to Speech", callback_data="t2s"),           
                InlineKeyboardButton("Tools", callback_data="basic"),                      
                InlineKeyboardButton("Url Tools", callback_data="urtol"),                
           

              ],
              [
                InlineKeyboardButton("Url Lock", callback_data="rlock"),     
                InlineKeyboardButton("Users", callback_data="user_kk"),
                InlineKeyboardButton("Virus Scan", callback_data="virus"),
              ],  
              [
                InlineKeyboardButton("Warn", callback_data="dlk_kk"),
                InlineKeyboardButton("Weather", callback_data="mosam"),
                InlineKeyboardButton("Zip", callback_data="zepper"),

              ],
              [
                InlineKeyboardButton(text="🔼 Collapse", callback_data="BCK")
             ]]
        )
  
  CHAT_WELCOME_BUTTON = InlineKeyboardMarkup(
             [[
                InlineKeyboardButton("Quick Setup Guide", url="t.me/DaisyXBot?start=tutorial")
             ]]
        )
