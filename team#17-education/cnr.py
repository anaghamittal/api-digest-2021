import requests
import json
from admins import CS_toolkit
from telegram import ForceReply
import random


bot = CS_toolkit("config.cfg")

class CNR():

    def __init__(self):
        self.base = "http://api.hackerearth.com/v3/code/"

    def run(self, chat_id, reply):
        url = self.base + "run/"
        data = {"client_secret": "e42005ddcc296225a7920b008dcd5f6011e2cd6c",
        "async": 0,
        "source": reply,
        "lang": "PYTHON3",
        "time_limit": 5,
        "memory_limit": 262144,
        }
        r = requests.post(url, data = data)
        print(r)
       # r = r.json()
        #r = r["run_status"]["output"]
        #return bot.sendMessage(r, chat_id, None)
