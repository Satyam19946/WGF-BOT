import discord
from discord.ext import commands


theReactMessage = 781027866619936810
class rolesAssigner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if ( payload.message_id == theReactMessage ):
            guild = discord.utils.find( lambda x : x.id == payload.guild_id, self.bot.guilds )
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role:
                await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if ( payload.message_id == theReactMessage ):
            guild = discord.utils.find( lambda x : x.id == payload.guild_id, self.bot.guilds)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
            
            if role:
                member = guild.get_member(payload.user_id)
                if member:
                    await member.remove_roles(role)
        

def setup(bot):
    bot.add_cog(rolesAssigner(bot))
        