import os 
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from Yuriko.kigo import Yuriko
from Yuriko import telethn as bot

@Yuriko(pattern="^/glogo ?(.*)")
async def makelogo(event):
        quew = event.pattern_match.group(1).strip()
            
        if not quew:
           await event.reply("**Invalid Command Syntax**\n\n`/glogo [name]`")
           return
        else:
           pass
        msg = await event.reply('Creating your logo...wait!')
        try:
            text = quew
            if ";" in text:
                upper_text, lower_text = text.split(";")
                upper_text = upper_text.strip() 
                lower_text = lower_text.strip()
            else:
               upper_text = text
               lower_text = ""
            
            bg = [ 

               "https://telegra.ph/file/889af581df669d3f183b9.jpg",

               "https://telegra.ph/file/9d65663d6208159dd8be4.jpg",

               "https://telegra.ph/file/731767cc4bbcfdc699ee9.jpg",

               "https://telegra.ph/file/5b93306d798041209da95.jpg",

               "https://telegra.ph/file/3300df182f4c3ac5d128e.jpg",

               "https://telegra.ph/file/c2747c9581938f6961ad9.jpg",

               "https://telegra.ph/file/9d65663d6208159dd8be4.jpg",

               "https://telegra.ph/file/3d469bacf9dae31fb3d14.jpg",

               "https://telegra.ph/file/3300df182f4c3ac5d128e.jpg",

               "https://telegra.ph/file/c2747c9581938f6961ad9.jpg",

               "https://telegra.ph/file/bc4c284d2ab0b8b7bc934.jpg",

               "https://telegra.ph/file/e41726801097b95ce7f07.jpg",

               "https://telegra.ph/file/da5e5d0206be545eeac27.jpg",

               "https://telegra.ph/file/dd48902679e7612c551e7.jpg",

               "https://telegra.ph/file/ed6806a4ba310008a96a5.jpg",

               "https://telegra.ph/file/99eb170e579e7b7f2fbc8.jpg",

               "https://telegra.ph/file/12218896d755952806e4b.jpg",

               "https://telegra.ph/file/2bfe013c59efa1d40aaf1.jpg",

               "https://telegra.ph/file/84d3872334efcba960de6.jpg",

               "https://telegra.ph/file/f24182fab85e732f7b8a2.jpg",

               "https://telegra.ph/file/da1f931a438986834d464.jpg",

               "https://telegra.ph/file/d3bdda4ea1cbeb03d338e.jpg",

               "https://telegra.ph/file/1028be52628cabf7d9c14.jpg",

               "https://telegra.ph/file/aee7df75a5edd1b02abde.jpg",

               "https://telegra.ph/file/98594f777a3ff7ca56590.jpg",

               "https://telegra.ph/file/59452682abf194ba52f35.jpg",

               "https://telegra.ph/file/be93f3a8f47ddc06595da.jpg",

               "https://telegra.ph/file/4b4332ad51927956ec162.jpg",

               "https://telegra.ph/file/65ed566139a6f59330635.jpg",

               "https://telegra.ph/file/6fdaf704c340fd90b7447.jpg",

               "https://telegra.ph/file/bcf8802314be0877f52c1.jpg",

               "https://telegra.ph/file/1117b9082db928a8ac715.jpg",

               "https://telegra.ph/file/73066d5a889acb8584c9a.jpg",

               "https://telegra.ph/file/a4b2724f0093a02eb5b21.jpg",

               "https://telegra.ph/file/b441ce7cbcd42a504c26c.jpg",

               "https://telegra.ph/file/015ee9a1f298172057927.jpg",

               "https://telegra.ph/file/13a931844555d6c81607e.jpg",

               "https://telegra.ph/file/0b064018f9f215bfe80e7.jpg",

            ]
            
            randBg = random.choice(bg)
            

            allFonts = [
            "NEON____.TTF",
            ]
            randFont = random.choice(allFonts)
            response = requests.get(randBg)
            img = Image.open(BytesIO(response.content))
            blueimg = img.filter(ImageFilter.BoxBlur(1))
            draw = ImageDraw.Draw(blueimg)
            imgSize = blueimg.size


            if upper_text:
        
                  
                  fontSize = int(imgSize[1] / 5)
                  image_widthz, image_heightz = img.size    
                  font = ImageFont.truetype(f"./Yuriko/resources/fonts/{randFont}", fontSize)
                  textSize = font.getsize(upper_text)
                  while textSize[0] > imgSize[0] - 100:
                     fontSize -= 1
                     font = ImageFont.truetype(f"./Yuriko/resources/fonts/{randFont}", fontSize)
                     textSize = font.getsize(upper_text)
                  w, h = draw.textsize(upper_text, font=font)
                  h += int(h*0.5)
                  image_width, image_height = blueimg.size
                  x = (image_widthz-w)/2
                  y= ((image_heightz-h)/1.9+6)
                  draw.text((x, y), upper_text, font=font, fill="white", stroke_width=1, stroke_fill="black")
        
                  
              
            if lower_text:
        
                  fontSize = int(imgSize[1] / 14)
                  image_widthz, image_heightz = img.size
                  font = ImageFont.truetype(f"./Yuriko/resources/fonts/{randFont}", fontSize)
                  textSize = font.getsize(lower_text)
                  while textSize[0] > imgSize[0] - 100:
                     fontSize -= 1
                     font = ImageFont.truetype(f"./Yuriko/resources/fonts/{randFont}", fontSize)
                     textSize = font.getsize(lower_text)
                  w, h = draw.textsize(lower_text, font=font)
                  h += int(h*0.5)
                  image_width, image_height = blueimg.size
                  x = (image_widthz-w)/2
                  y= ((image_heightz-h)/1.6+6)
                  
                  draw.text((x, y), lower_text, font=font, fill="white", stroke_width=2, stroke_fill="black")
                  
            fname2 = "logobycoder.png"
            blueimg.save(fname2, "png")
            await bot.send_file(event.chat_id, fname2, caption="Made By @Kigo_omfobot")
            if os.path.exists(fname2):
               os.remove(fname2)
    

        except Exception as e:
            await msg.edit(f"Please Try Again! \nif you're getting Error again and again then Report @godzilla_chatting")
