import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix = 'wgf!', intents=intents)
# Add "cogs.rolesAssigner" for also doing a role assignment.
cogs = ["cogs.helloFromCogs", "cogs.checkNumber"]
allowedCommands = ['hello', 'checkNumber', 'ping']

token = open("config/botToken.txt",'r').read()

@bot.event
async def on_ready():
    print("Bot up and running!!")
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(e)

@bot.event
async def on_command_error(ctx, error):
    print(error)

@bot.command()
async def ping(ctx):
    await ctx.send("Yes, I am working! Current Latency = {:.2f}ms".format(bot.latency*1000))

bot.run(token)