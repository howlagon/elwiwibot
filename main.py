import traceback
import lightbulb, hikari

import env

token = env.DISCORD_TOKEN
prefix = env.PREFIX

bot = lightbulb.BotApp(
    token=token,
    prefix=prefix,
    intents=hikari.Intents.ALL_UNPRIVILEGED + hikari.Intents.MESSAGE_CONTENT,
    # logs=None,
    owner_ids=[266751215767912463],
    suppress_optimization_warning=True,
    help_slash_command=True,
    banner=None,
)

@bot.listen(hikari.StartedEvent)
async def on_start(event: hikari.StartedEvent) -> None:
    user = await event.app.rest.fetch_my_user()
    print(f"Logged in as {user.username}#{user.discriminator}")

@bot.command
@lightbulb.command("ping", "Calls the bot with its delay")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! Bot ping is {round(ctx.bot.heartbeat_latency*1000, 1)}ms")

@bot.command
@lightbulb.command("reload", "reloads all extensions")
@lightbulb.implements(lightbulb.PrefixCommand)
async def reload(ctx: lightbulb.Context) -> None:
    message = await ctx.respond(embed=hikari.Embed(description="**Reloading all extensions**", color=0x8aadff))
    try:
        bot.reload_extensions(*bot.extensions)
        await message.edit(embed=hikari.Embed(description="**:white_check_mark: Reloaded**", color=0x29ff70))
    except Exception as e:
        await message.edit(embed=hikari.Embed(description=f"**:x: Error reloading**\n{e}", color=0xff3838))

bot.load_extensions_from("plugins")
bot.run()