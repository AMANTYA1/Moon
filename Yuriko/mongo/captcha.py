# Copyright (C) 2022 szsupunma
# Copyright (C) 2021 @szrosebot

# This file is part of @szrosebot (Telegram Bot)

from pymongo import MongoClient
from Yuriko import MONGO_DB_URI

class captchas():
    def __init__(self):
        self.db = MongoClient(MONGO_DB_URI)["captcha"]
        self.chats = self.db["Chats"]
        
    def chat_in_db(self, chat_id):
        chat = self.chats.find_one({"chat_id":chat_id})
        return chat
        
    def add_chat(self, chat_id, captcha):
        if self.chat_in_db(chat_id):
            return 404
        self.chats.insert_one({"chat_id":chat_id, "captcha": captcha})
        return 200
    
    def delete_chat(self,chat_id):
        self.chats.delete_many({"chat_id": chat_id})
        return True
