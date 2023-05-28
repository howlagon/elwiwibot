"""i wrote this bot just to block nitro emojis from someone named elperson. fuck you elperson. stop spamming"""
import lightbulb, hikari
import time, re
import ujson as json

plugin = lightbulb.Plugin("elpipi")

@plugin.listener(hikari.MessageCreateEvent)
async def block_elperson(event: hikari.MessageCreateEvent) -> None:
    if event.author.id != 717449386040361002:
        return
    message = event.message.content
    message = re.sub(r"<a:[a-zA-Z_-]*:[0-9]*>", "", message)
    message = re.sub(r"<:[a-zA-Z_-]*:[0-9]*>", "", message)
    message = message.replace(" ", "")
    print("message content: %r" % message)
    if message != "" or len(message) != 0:
        return
    await event.message.delete()

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)