from admins import CS_toolkit
import json
import requests
from gfg import GFG

bot = CS_toolkit("config.cfg")
gfg_ = GFG()

def reply(msg, sender):
	if msg is None:
		return
	if msg == "/start":
		return bot.sendMessage("Hey there!\nThis is your one-stop bot for all CP related stuff.\nType /help to see all commands.", sender, None)
	if msg == "/help":
		return bot.sendMessage("""Here is a list of possible commands:
		/start : to start the bot
		/help : to get a list of commands
		/gfg : to fetch categories of articles from GeeksforGeeks
		""",
		sender, None)
	if msg == "/gfg":
		return gfg_.options(sender)
	if msg is not None:
		return bot.sendMessage("Okay!", sender, None)

update_id = None
while True:
	updates = bot.getUpdates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id = item["update_id"]
			try:
				msg = item["message"]["text"]
				sender = item["message"]["from"]["id"]
			except:
				msg = None
				sender = None
		reply(msg, sender)