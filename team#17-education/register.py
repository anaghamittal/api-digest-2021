import requests
import json
from admins import CS_toolkit
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from codeforces import Codeforces
from github import Github
from cnr import CNR

bot = CS_toolkit("config.cfg")
codeforces = Codeforces()
github = Github()
cnr = CNR()
class Register():

    def __init__(self):
        self.platforms = ["Codeforces", "Github", "Compile n Run"]

    def chosen_platform(self, chat_id, update_id):
        callback = bot.getUpdates(offset=update_id)
        update_id += 1
        callback = callback["result"][0]["callback_query"]["data"]
        if(callback == "cf"):
            codeforces.show_options(chat_id, update_id)
        if(callback == "gh"):
            github.show_options(chat_id, update_id)
        if(callback == "cr"):
            bot.sendMessage("Please enter your code", chat_id, None)
            reply = bot.getUpdates(offset=update_id)
            update_id += 1
            reply = reply["result"][0]["message"]["text"]
            cnr.run(chat_id, reply)

    def show_options(self, chat_id, update_id):
        keyBoard = { "inline_keyboard": [
                [
                    {"text": self.platforms[0], "callback_data": "cf"},
                    {"text": self.platforms[1], "callback_data": "gh"}
                ],
                [
                    {"text": self.platforms[2], "callback_data": "cr"}
                ]
            ]
        }
        bot.sendMessage("Please select one of the following:", chat_id, reply_markup=json.dumps(keyBoard))
        self.chosen_platform(chat_id, update_id)
