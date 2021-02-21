from admins import CS_toolkit
import json
import requests
from gfg import GFG

gfg_links = """{
	"Search": "https://www.geeksforgeeks.org/searching-algorithms/",
	"Sort": "https://www.geeksforgeeks.org/sorting-algorithms/",
	"DP": "https://www.geeksforgeeks.org/dynamic-programming/",
	"DnC": "https://www.geeksforgeeks.org/divide-and-conquer/"
	}"""

bot = CS_toolkit("config.cfg")
gfg_ = GFG()

def displayLink(key):
	links = json.loads(gfg_links)
	if key in links:
		return bot.sendMessage(links[key], sender, None)
	else:
		return bot.sendMessage("Ehh.. maybe a wrong spelling or command, check again.", sender, None)

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
		/search_algos : to fetch the link to learn about searching algorithms
		/sort_algos : to fetch the link to learn about sorting algorithms
		/dp : to fetch the link to learn about dynamic programming
		/dnc : to fetch the link to learn about divide and conquer
		""",
		sender, None)
	if msg == "/gfg":
		return gfg_.options(sender)
	if msg == "/search_algos":
		key = "Search"
		return displayLink(key)
	if msg == "/sort_algos":
		key = "Sort"
		return displayLink(key)
	if msg == "/dp":
		key = "DP"
		return displayLink(key)
	if msg == "/dnc":
		key = "DnC"
		return displayLink(key)
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