import ujson as json
from random import random
import os
if not os.path.exists("config.json"):
    with open("config.json", "w", encoding="utf-8") as f:
        f.write("{}")
    raise Exception("No config file found, please fill out config.json")

fp = json.load(open("config.json", "r", encoding="utf-8"))
PREFIX = fp.get("prefix") or hex(random.getrandbits(128))[2:] # fallback random prefix so you can't use prefix commands
DISCORD_TOKEN = fp.get("token") or fp.get("discord_token")
NAME = fp.get("name") or "bot"

if DISCORD_TOKEN is None:
    raise Exception("No discord token provided")