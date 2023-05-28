import platform

import lightbulb, hikari
import ujson
import env

plugin = lightbulb.Plugin("about")

@plugin.command
@lightbulb.command("about", "Sends bot info")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def about(ctx: lightbulb.Context) -> None:

    authorids = ', '.join([f"<@{i}>" for i in ctx.bot.owner_ids])

    embed = hikari.Embed(
        title=f"About {env.NAME}",
        description=(
            f"Authored by {authorids}"
        ),
        url="https://github.com/howlagon/elwiwibot",
        colour=0xe9d5b5
    )
    embed.set_thumbnail(ctx.bot.get_me().avatar_url)
    embed.set_author(name="Bot Information")
    embed.set_footer(f"Requested by {ctx.member.display_name}", icon=ctx.member.avatar_url)
    # embed.add_field("Bot version", f"`{commithash}`", inline=True)
    # embed.add_field("Latest change", commitmsg, inline=True)
    embed.add_field("Python version", f"`{platform.python_version()}`", inline=True)
    embed.add_field("Hikari version", f"`{hikari.__version__}`", inline=True)
    embed.add_field("Lightbulb version", f"`{lightbulb.__version__}`", inline=True)
    
    await ctx.respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)