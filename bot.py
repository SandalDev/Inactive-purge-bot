import discord
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.members = True
bot=commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

async def send(message):
    channel = bot.get_channel(INSET_CHANNEL_ID)
    await channel.send(message)

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def purge(ctx):
    await send("Purging Inactive Members!")
    server=ctx.message.guild
    role = discord.utils.get(ctx.guild.roles, name="Active")
    print(role)
    guild = bot.get_guild(INSERT_GUILD_ID)
    print(guild.members)
    members = (ctx.guild.fetch_members(limit=None))
    for member in guild.members:
        print("Purging")
        time.sleep(2)
        if role not in member.roles:
            print(member)
            print(member.roles)
            await ctx.guild.kick(member)
            print("Purged")
    await send("Purged Inactive Members!")

bot.run(BOT_TOKEN)
