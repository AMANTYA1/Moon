from motor.motor_asyncio import AsyncIOMotorClient as AvengerMongoClient
from Avenger import MONGO_DB_URI

avengermongo = AvengerMongoClient(MONGO_DB_URI)
avengerdb = avengermongo.szrose

#Indexes for Plugins
coupledb = avengerdb.couple
karmadb = avengerdb.karma
nsfwdb = avengerdb.nsfw
chatbotdb = avengerdb.chatbot
torrentdb = avengerdb.torrentdb
AIbotdb = avengerdb.AIbotdb
anitcdb = avengerdb.antichnl
captchadb = avengerdb.captcha
urllockdb = avengerdb.urllock
