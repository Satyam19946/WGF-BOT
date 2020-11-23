import discord
from discord.ext import commands

class rolesAssigner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload.message_id)
        # Changes here for the role reaction
        

def setup(bot):
    bot.add_cog(rolesAssigner(bot))
        