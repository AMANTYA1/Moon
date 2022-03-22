from telethon import events, Button, custom
from Yuriko.events import register

@register(pattern=("^/(game|games)"))
async def games(event):

    await event.reply(
                    "hello, we have attched some games for you, press the button and play games.",
                    buttons=[
                        [
                            Button.url(
                                "BUBBLE TOWER 3D",
                                "https://play.famobi.com/bubble-tower-3d",
                            ),
                            Button.url(
                                "ROM NOM RUN",
                                "https://play.famobi.com/om-nom-run",
                            ),
                        ],

                        [
                            Button.url(
                                "CANNON BALLS 3D",
                                "https://play.famobi.com/cannon-balls-3d",
                            ),
                            Button.url(
                                "ARCHERY WORLD TOUR",
                                "https://play.famobi.com/archery-world-tour",
                            ),
                        ]
                    ],
                    parse_mode="html",
                )
