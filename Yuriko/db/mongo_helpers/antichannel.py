from pymongo import MongoClient

from Shadow.confing import get_str_key

MONGO_DB_URI = get_str_key("MONGO_URI")
client = MongoClient(MONGO_DB_URI)
dbd = client["missjuliarobot"]
approved_users = dbd.approve
db = dbd
chnldb = db.antichnldb

################################
##   Anti-Channel (ON/OFF)    ##
################################
async def anti_chnl(chat_id):
    sed = chnldb.find_one({f"antichnl": chat_id})
    return sed


async def add_anti_chnl(chat_id):
    sed = chnldb.insert_one({f"antichnl": chat_id})
    return sed


async def rem_anti_chnl(chat_id):
    sed = chnldb.delete_one({f"antichnl": chat_id})
    return sed


############################
##    Restriction: Ban    ##
############################
async def ban_chnl(chat_id):
    sed = chnldb.find_one({"ban_chnl": chat_id})
    return sed


async def add_ban_chnl(chat_id):
    sed = chnldb.insert_one({"ban_chnl": chat_id})
    return sed


async def rem_ban_chnl(chat_id):
    sed = chnldb.delete_one({"ban_chnl": chat_id})
    return sed


#############################
##   Restriction: Delete   ##
#############################
async def dlt_chnl(chat_id):
    sed = chnldb.find_one({"dlt_chnl": chat_id})
    return sed


async def add_dlt_chnl(chat_id):
    sed = chnldb.insert_one({"dlt_chnl": chat_id})
    return sed


async def rem_dlt_chnl(chat_id):
    sed = chnldb.delete_one({"dlt_chnl": chat_id})
    return sed
