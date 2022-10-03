from Yuriko import pbot as arpi
import re
import os
import asyncio
from pyrogram.errors import FloodWait
from pyrogram import filters

 
SUDO = os.environ["SUDO_USER"]
SUDO = SUDO.split(" ")
ab = map(int, SUDO)
ab = list(ab)

CHATS = os.environ["CHAT"]
CHATS = CHATS.split(" ")
ch = map(int, CHATS)
ch = list(ch)


filter_ = (
           (filters.me | filters.user(ab) | filters.chat(ch))
            & filters.command(["scrape", "scr"], ",")
            & ~filters.via_bot
            & ~filters.forwarded
          )


@arpi.on_message(filter_)
async def skrep(client, message):
  lis = []
  id_ = message.from_user.id
  me = await arpi.get_me()
  d = await message.reply_text("`starting.....`")

  if len(message.command) == 2:
    lim = int(message.command[1]) 
    async for x in arpi.iter_history(message.chat.id, limit=lim):
      msg = x.text
      msg = str(msg) 
      msg = msg.replace("\n", " ")
      if "|" in msg:
        str_ = msg.split(" ")
        for item in str_:
          if item.startswith("3") or item.startswith("5") or item.startswith("4") or item.startswith("6"):
            try:
              try:
                p1 = re.compile(r'\d{16}\|\d{2}\|\d{2,4}\|\d{3}')
                m1 = p1.findall(item)
                m1 = "".join(m1)
                if m1 not in lis:
                  lis.append(m1)
              except:
                p2 = re.compile(r'\d{16}\|\d{2}/\d{2,4}\|\d{3}')
                m2 = p2.findall(item)
                m2 = "".join(m2)
                if m2 not in lis:
                  lis.append(m2)
            except:
              pass
          else:
            pass
    
      else:
        a = re.compile(r'\d{15,16}')
        b = a.findall(msg)
        l = len(b)
        if l == 0:
          pass
        else:
          p = re.compile(r'\d+')
          m = p.findall(msg)
          len_ = len(m)
          x = len_//4
          y = x*4
          a = 0
          while a < y:
            try:
              ccn = m[a]
              a = a+1
              cvv = m[a]
              a = a+1
              mm = m[a]
              a = a+1
              yy = m[a]
              cc = f"{ccn}|{mm}|{yy}|{cvv}"
              if cc not in lis:
                lis.append(cc)
              a = a+1
            except:
              pass

  
  elif len(message.command) == 3:
    grup = message.command[1]
    grup = grup.replace("@", "")
    if grup.isdigit():
      grup = int(grup)
    lim = int(message.command[2])
    async for x in arpi.iter_history(grup, limit=lim):
      msg = x.text
      msg = str(msg)
      msg = msg.replace("\n", " ")
      if "|" in msg:
        str_ = msg.split(" ")
        for item in str_:
          if item.startswith("3") or item.startswith("5") or item.startswith("4") or item.startswith("6"):
            try:
              try:
                p1 = re.compile(r'\d{16}\|\d{2}\|\d{2,4}\|\d{3}')
                m1 = p1.findall(item)
                m1 = "".join(m1)
                if m1 not in lis:
                  lis.append(m1)
              except:
                p2 = re.compile(r'\d{16}\|\d{2}/\d{2,4}\|\d{3}')
                m2 = p2.findall(item)
                m2 = "".join(m2)
                if m2 not in lis:
                  lis.append(m2)
            except:
              pass
          else:
            pass
    
      else:
        a = re.compile(r'\d{15,16}')
        b = a.findall(msg)
        l = len(b)
        if l == 0:
          pass
        else:
          p = re.compile(r'\d+')
          m = p.findall(msg)
          len_ = len(m)
          x = len_//4
          y = x*4
          a = 0
          if len(m[0]) == 15 or 16:
            while a < y:
              try:
                ccn = m[a]
                a = a+1
                cvv = m[a]
                a = a+1
                mm = m[a]
                a = a+1
                yy = m[a]
                cc = f"{ccn}|{mm}|{yy}|{cvv}"
                if cc not in lis:
                  lis.append(cc)
                a = a+1
              except:
                pass
          else:
            pass
            
  else:
    if id_ == me.id:
      await message.reply_text("`Invalid format`")
    else:
      await d.edit("`Invalid format`")

  """os.chdir("/app/Vinci/modules/")
  try:
    os.mkdir("scrapped")
    os.chdir("/app/Yuriko/modules/scrapped/")
  except:
    os.chdir("/app/Yuriko/modules/scrapped/")"""
    
  try:
    c = len(lis)
    flnm = f"x{c}_scrapped.txt"
    if c == 0:
      await d.edit("`No CC FOUND!`")
    else:
      f = open(flnm, "a")
      for item in lis:
        if len(item) > 22:
          f.write(re.sub(r'^$\n', '', f"{item}\n", flags=re.MULTILINE))
      f.close()
      #print("sending file...")
      if id_ == me.id:
        await arpi.send_document(message.chat.id, flnm, caption=f"\n**✅ Scrapped successfully!**\n**CC Found**: {c}\n\n**Bot by:** @MeCorw")
      else:
        await arpi.send_document(message.chat.id, flnm, caption=f"\n**✅ Scrapped successfully!**\n**CC Found**: {c}\n\n**Bot by:** @MeCorw", reply_to_message_id=message.message_id) 
      os.remove(flnm)
      if id_ == me.id:
        await message.delete()
      else:
        await d.delete()
    
  except:
    if id_ == me.id:
      await message.delete()
    else:
      await d.edit("`Unexpected error`")


