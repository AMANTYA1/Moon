from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name
from Yuriko.events import register


async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        if sed.is_admin:
            is_mod = True
        else:
            is_mod = False
    except:
        is_mod = False
    return is_mod
 

@register(pattern="^/tag(on|off|ki|bots|rec|admins|owner)?(.*)")
async def _(e):
    if not await is_admin(e, e.sender_id):
        await e.respond("You need to be an admin to do this.")
        return
    
    else:
    
        okk = e.text
        lll = e.pattern_match.group(1)
        users = 0
        o = 0
        nn = 0
        rece = 0
        if lll:
            xx = f"{lll}"
        else:
            xx = ""
        async for bb in e.client.iter_participants(e.chat_id, 150):
            users = users + 1
            x = bb.status
            y = bb.participant
            if isinstance(x, onn):
                o = o + 1
                if "on" in okk:
                    xx += f"\n⚜️ [{get_display_name(bb)}](tg://user?id={bb.id})"
            if isinstance(x, off):
                nn = nn + 1
                if "off" in okk:
                    if not (bb.bot or bb.deleted):
                        xx += f"\n⚜️ [{get_display_name(bb)}](tg://user?id={bb.id})"
            if isinstance(x, rec):
                rece = rece + 1
                if "rec" in okk:
                    if not (bb.bot or bb.deleted):
                        xx += f"\n⚜️ [{get_display_name(bb)}](tg://user?id={bb.id})"
            if isinstance(y, owner):
                if "admin" or "owner" in okk:
                    xx += f"\n👑 [{get_display_name(bb)}](tg://user?id={bb.id}) 👑"
            if isinstance(y, admin):
                if "admin" in okk:
                    if not bb.deleted:
                        xx += f"\n 👷‍♂️ [{get_display_name(bb)}](tg://user?id={bb.id})"
            if "ki" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n⚜️ [{get_display_name(bb)}](tg://user?id={bb.id})"
            if "bot" in okk:
                if bb.bot:
                    xx += f"\n🤖 [{get_display_name(bb)}](tg://user?id={bb.id})"
        await e.client.send_message(e.chat_id, xx)
        await e.delete()

