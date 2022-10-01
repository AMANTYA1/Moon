# @greyyvbss
# Dont Remove Credit

import os

from PIL import Image, ImageDraw, ImageFont
from Yuriko.events import register

def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = len(line) // 55
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]


@register(pattern="^/write ?(.*)")
async def writer(event):
    if event.reply_to:
        reply = await event.get_reply_message()
        text = reply.message
    elif event.pattern_match.group(1).strip():
        text = event.text.split(maxsplit=1)[1]
    else:
        return await event.reply("Give some Text")
    k = await event.reply("On My way 😂..")
    img = Image.open("Yuriko/resources/kertas.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Yuriko/resources/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "crow.jpg"
    img.save(file)
    await event.reply(file=file)
    os.remove(file)
    await k.delete()
   
    
