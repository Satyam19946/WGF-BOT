import numpy as np
from discord.ext import commands

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# The config files can be found in the botftuff folder in logistics folder of the WGF 2021.
gc = gspread.service_account(filename="config/credentials.json")
attendanceSheetKey = open("config/attendanceSheetKey.txt",'r').read()
# raffleSheetKey = open("config/raffleSheetKey.txt", "r").read()

attendanceSheet = gc.open_by_key(attendanceSheetKey).sheet1
# raffleSheet = gc.open_by_key(raffleSheetKey).sheet1

#This will update the Raffle Numbers so every user has a raffle number.
def updateRaffleNumbers():
    myData = np.array(attendanceSheet.get_all_values())
    print(myData)
    start = int(myData[1][-2])
    for i in range(2,len(myData)):
        print(myData[i][-2])
        if str(myData[i][-2]) == "" or int(myData[i][-2]) != start+i-1:
            if i == 1:
                myData[i][-2] = '10000'
            else:
                myData[i][-2] = str(int(myData[i-1][-2]) + 1)
            myData[i][-1] = 0
    attendanceSheet.update("K2:L" + str(len(myData)), myData[1:,-2:].tolist())
    # raffleSheet.update(myData.tolist())
    return myData

class checkNumber(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def checkNumber(self, ctx):
        myData = updateRaffleNumbers()
        ticketsFound = []
        userName = ctx.author
        print(myData)
        for i in range(1,len(myData)):
            if myData[i][3] == str(userName):
                ticketsFound.append(myData[i][-2])
        
        numberOfTickets = len(ticketsFound)
        if numberOfTickets:
            returnMessage = "Hello {}, we found {} ticket(s) under your name: \n".format(userName, numberOfTickets)
            counter = 1
            for ticket in ticketsFound:
                returnMessage += "Ticket {} Number: {}\n".format(counter, ticket)
                counter += 1
            await ctx.send(returnMessage)
        else:
            await ctx.send("Hello, {}, We didn't find any tickets under your username. \n Contact a person with a Tech Comm role if you signed up with your discord username correctly.".format(userName))

    
def setup(bot):
    bot.add_cog(checkNumber(bot))