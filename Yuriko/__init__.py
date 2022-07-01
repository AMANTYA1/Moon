import logging
import os
import sys
import json
import asyncio
import time
import spamwatch
import telegram.ext as tg
from inspect import getfullargspec
from aiohttp import ClientSession
from Python_ARQ import ARQ
from redis import StrictRedis
from motor.motor_asyncio import AsyncIOMotorClient
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.sessions import MemorySession
from pyrogram.types import Message
from pyrogram import Client, errors
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from pyrogram.types import Chat, User
import pymongo

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DRAGONS = {int(x) for x in os.environ.get("DRAGONS", "").split()}
        DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = {int(x) for x in os.environ.get("DEMONS", "").split()}
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = {int(x) for x in os.environ.get("WOLVES", "").split()}
    except ValueError: 
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = {int(x) for x in os.environ.get("TIGERS", "").split()}
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", True))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "YurikoRobot")
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    SESSION_STRING = os.environ.get("SESSION_STRING", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "postgresql://ivsnctpi:uZ2ywNAb1KWa7zhocG09xoRbHfcDFfGw@fanny.db.elephantsql.com/ivsnctpi")
    REDIS_URL = os.environ.get('REDIS_URL', "redis://Akshay:Akshay_123@redis-11962.c301.ap-south-1-1.ec2.cloud.redislabs.com:11962/Akshay")
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://Aman:Aman@cluster0.7bsvz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    ARQ_API = os.environ.get("ARQ_API", "BCYKVF-KYQWFM-JCMORU-RZWOFQ-ARQ")
    DONATION_LINK = os.environ.get("DONATION_LINK")
    LOAD = os.environ.get("LOAD", "").split()
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "godzilla_chatting")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    LASTFM_API_KEY = os.environ.get("LASTFM_API_KEY", None)
    CF_API_KEY = os.environ.get("CF_API_KEY", None)
    WELCOME_DELAY_KICK_SEC = os.environ.get("WELCOME_DELAY_KICL_SEC", None)
    BOT_ID = int(os.environ.get("BOT_ID", None))
    ARQ_API_URL = "https://grambuilders.tech"
    ARQ_API_KEY = "SMINJX-OXJKOS-KFXZMD-CSLZRO-ARQ"

    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)

    try:
        BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

else:
    from Yuriko.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = Config.JOIN_LOGGER
    OWNER_USERNAME = Config.OWNER_USERNAME
    ALLOW_CHATS = Config.ALLOW_CHATS
    try:
        DRAGONS = {int(x) for x in Config.DRAGONS or []}
        DEV_USERS = {int(x) for x in Config.DEV_USERS or []}
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = {int(x) for x in Config.DEMONS or []}
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = {int(x) for x in Config.WOLVES or []}
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = {int(x) for x in Config.TIGERS or []}
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    EVENT_LOGS = Config.EVENT_LOGS
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    REDIS_URL = "redis://Akshay:Akshay_123@redis-11962.c301.ap-south-1-1.ec2.cloud.redislabs.com:11962/Akshay"
    API_ID = "2857558"
    API_HASH = "1038be815e038592fa2b483c13dd6c4b"

    DB_URI = "postgresql://uybtrchs:VwwG2Sm7g4hyja_hlYzpHjBkf5ZqQot9@salt.db.elephantsql.com/uybtrchs"
    MONGO_DB_URI = "mongodb+srv://Aman:Aman@cluster0.7bsvz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_KEY = "SMINJX-OXJKOS-KFXZMD-CSLZRO-ARQ"
    ARQ_API_URL = "https://arq.hamker.dev"
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    TEMP_DOWNLOAD_DIRECTORY = "./"
    OPENWEATHERMAP_ID = "7181b8a4580be607eddacd56777bf64b"
    NO_LOAD = Config.NO_LOAD
    ERROR_LOG = -1001501915559
    HEROKU_API_KEY = "bfc37ec4-f73d-45e1-b392-4141ef1974d6"
    HEROKU_APP_NAME = "null"
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    REM_BG_API_KEY = None
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = "7KH0ZPYX5HAJ"
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = "2GoYVYezU8pUt2_UvL3bIiuIleY0o22ND3oX1Pt38gZeK4iXXH8U2DbPDl_CanVE"
    SESSION_STRING = "1BVtsOL8Bu0-1HWP9xFITfMlJX3bOb4Uy8gI9eQedGAKSnTAwSi-oDtuz0mNwF1Gn7D9tgImKr0rsi0d-u6ykxVGu4nbDGYMQvOwKUpAdcyfjpsg5SJ23iWrBP6WmTMbua_UrZ8jB4R8KZy-r3KcIP0Y4ntKbk1gwsJL8G6fBIYFDsQiPug1T5FoqASWn16vTwBQWAP9sTH-bLygtCNl761-rN2Y-7cb5sQEoz5rKLW7xvvB2xL4eKd8aNaVqwP99Ganma_l-KPTh9TuTXV55NMPtGYld5JTzlv1CEZ0PogEPVYlCD3INoGlFTinWfphrlqqgwXw2V5PqBBvrvj_Ww2_lesJqOsY="
    INFOPIC = Config.INFOPIC
    BOT_USERNAME = "Toxicity_X_Bot"
    BOT_ID = "2100341884"
    STRING_SESSION = "1BVtsOL8Bu0-1HWP9xFITfMlJX3bOb4Uy8gI9eQedGAKSnTAwSi-oDtuz0mNwF1Gn7D9tgImKr0rsi0d-u6ykxVGu4nbDGYMQvOwKUpAdcyfjpsg5SJ23iWrBP6WmTMbua_UrZ8jB4R8KZy-r3KcIP0Y4ntKbk1gwsJL8G6fBIYFDsQiPug1T5FoqASWn16vTwBQWAP9sTH-bLygtCNl761-rN2Y-7cb5sQEoz5rKLW7xvvB2xL4eKd8aNaVqwP99Ganma_l-KPTh9TuTXV55NMPtGYld5JTzlv1CEZ0PogEPVYlCD3INoGlFTinWfphrlqqgwXw2V5PqBBvrvj_Ww2_lesJqOsY="
    LASTFM_API_KEY = None
    CF_API_KEY = None

    try:
        BL_CHATS = {int(x) for x in Config.BL_CHATS or []}
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

# If you forking dont remove this id, just add your id. LOL...

DRAGONS.add(OWNER_ID)
DRAGONS.add(1920507972)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1920507972)

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")

from Yuriko.modules.sql import SESSION

defaults = tg.Defaults(run_async=True)
REDIS = StrictRedis.from_url(REDIS_URL,decode_responses=True)
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
dispatcher = updater.dispatcher
print("[INFO]: INITIALIZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

pbot = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    workers=min(32, os.cpu_count() + 4),
)
apps = []
apps.append(pbot)

myclient = pymongo.MongoClient(MONGO_DB_URI)
dbn = myclient["Null"]

# MongoDB client
mongo_client = AsyncIOMotorClient(MONGO_DB_URI)
db = mongo_client.wbb

async def get_entity(client, entity):
    entity_client = client
    if not isinstance(entity, Chat):
        try:
            entity = int(entity)
        except ValueError:
            pass
        except TypeError:
            entity = entity.id
        try:
            entity = await client.get_chat(entity)
        except (PeerIdInvalid, ChannelInvalid):
            for kp in apps:
                if kp != client:
                    try:
                        entity = await kp.get_chat(entity)
                    except (PeerIdInvalid, ChannelInvalid):
                        pass
                    else:
                        entity_client = kp
                        break
            else:
                entity = await kp.get_chat(entity)
                entity_client = kp
    return entity, entity_client


async def eor(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from Yuriko.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
