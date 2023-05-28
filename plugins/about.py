from sys import version
import lightbulb, hikari
import ujson, os
import env

if os.path.exists(".git/COMMIT_EDITMSG"):
    commit_message = open(".git/COMMIT_EDITMSG", "r", encoding="utf-8").read().strip("\n")
    commit_hash = open(".git/FETCH_HEAD", "r", encoding="utf-8").read().split("\t")[0][:7]
else:
    commit_message = None
    commit_hash = None

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
    if commit_hash or commit_message:
        embed.add_field("Bot version", f"`{commit_hash}`", inline=True)
        embed.add_field("Latest change", commit_message, inline=True)
    embed.add_field("Python version", f"`{version}`", inline=True)
    embed.add_field("Hikari version", f"`{hikari.__version__}`", inline=True)
    embed.add_field("Lightbulb version", f"`{lightbulb.__version__}`", inline=True)
    
    await ctx.respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)