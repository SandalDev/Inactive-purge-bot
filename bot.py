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
    channel = bot.get_channel(808745742729609259)
    await channel.send(message)

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def purge(ctx):
    await send("Purging Inactive Members!")
    server=ctx.message.guild
    role = discord.utils.get(ctx.guild.roles, name="Active")
    print(role)
    guild = bot.get_guild(808745737890168885)
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

bot.run('ODU2MTA1NjU0MjM3NzkwMjI4.YM8MhQ.3IJxN_kSZtqTr9kY_jmuTrHWnz4')