import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!wgfbot ')

@client.event
async def on_ready():
    print("Bot up and running!!")

@client.command()
async def working(ctx):
    await ctx.send("Yes, I am working! Current Latency = {:.2f}ms".format(client.latency*1000))

@client.command()
async def welcome(ctx):
    await ctx.send("Hello from the other side.")


client.run('Nzc5NzA4MTgyNDg1NjYzNzY0.X7kd1A._uD246D4Uq7z1OfA7xWE_WIExRs')
