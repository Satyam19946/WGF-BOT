from discord.ext import commands

import gspread
from oauth2client.service_account import ServiceAccountCredentials

gc = gspread.service_account(filename="config/credentials.json")

attendanceSheet = gc.open_by_key("1fLjLH3Eiw4xb-Rei0YChxJrggPhdM2cGKxdIoKt3_Nc")
userNameQuestion = 'Leave Your Discord Username to access personalized features of our Bot!!'
raffleNumber = 'Raffle Number'

myData = attendanceSheet.sheet1.get_all_records()

#This will update the Raffle Numbers so every user has a raffle number.
def updateRaffleNumbers():
    pass

class checkNumber(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def checkNumber(self, ctx):
        updateRaffleNumbers()
        ticketsFound = []
        userName = ctx.author
        for data in myData:
            if data[userNameQuestion] == str(userName):
                ticketsFound.append(data[raffleNumber])
        
        numberOfTickets = len(ticketsFound)
        if numberOfTickets:
            returnMessage = "Hello {}, we found {} ticket(s) under your name: \n".format(userName, numberOfTickets)
            counter = 1
            for ticket in ticketsFound:
                returnMessage += "Ticket {} Number: {}\n".format(counter, ticket)
                counter += 1
            await ctx.send(returnMessage)
        else:
            await ctx.send("Hello, {} Your Number is something".format(userName))

    
def setup(bot):
    bot.add_cog(checkNumber(bot))