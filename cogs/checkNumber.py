from discord.ext import commands

import gspread
from oauth2client.service_account import ServiceAccountCredentials

gc = gspread.service_account(filename='../passwords/credentials.json')

attendanceSheet = gc.open_by_key("1fLjLH3Eiw4xb-Rei0YChxJrggPhdM2cGKxdIoKt3_Nc")

myData = attendanceSheet.sheet1.get_all_records()
print(myData)

class simpleCommand(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello")
    
def setup(bot):
    bot.add_cog(simpleCommand(bot))