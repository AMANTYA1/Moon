import os 
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from Yuriko.kigo import Yuriko
from Yuriko import telethn as bot

@Yuriko(pattern="^/blogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if not quew:
       await event.reply("**Invalid Command Syntax**\n\n`/blogo [name]`")
       return
 else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./Yuriko/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Yuriko/resources/Chopsic.otf", 330)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "LogoByNull.png"
    img.save(fname2, "png")
    await bot.send_file(event.chat_id, fname2, caption="Made By @Kigo_omfobot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @godzilla_chatting, {e}')

