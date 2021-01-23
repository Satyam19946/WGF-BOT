import numpy as np
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import json
gc = gspread.service_account(filename="config/credentials.json")
f = open('config/googleSheets.json')
data = json.load(f)


userNameQuestion = 'Recommended: Discord Username With Tag (like this: xyz#1234)'
pidQuestion = 'Please enter your PID'
firstName = 'First Name'
startingNumbers = [300000, 400000, 500000]
sheetsName = ['Attendance', 'Artist Alley', 'Panelists & Events']

def getTickets(username):
    generalAttendanceSheet = gc.open_by_key(data['generalAttendanceSheet']).sheet1
    generalAttendanceSheetData = generalAttendanceSheet.get_all_records()
    artistAlleySheet = gc.open_by_key(data['artistAlleySheet']).sheet1
    artistAlleySheetData = artistAlleySheet.get_all_records()
    eventSheet = gc.open_by_key(data['eventSheet']).sheet1
    eventSheetData = eventSheet.get_all_records()
    ticketsFound = []
    for sheets, sheetNumber in zip([generalAttendanceSheetData, artistAlleySheetData, eventSheetData], range(3)):
        start = startingNumbers[sheetNumber]
        for sheetData in sheets:
            if sheetData[userNameQuestion] == str(username):
                #Check if ticket has number if not assign it one
                ticketsFound.append((start, sheetsName[sheetNumber]))
            start += 1
    return ticketsFound

class checkNumber(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def checkNumber(self, ctx):
        ticketsFound = getTickets(ctx.author)
        userName = ctx.author
        print(ticketsFound)
        numberOfTickets = len(ticketsFound)
        if numberOfTickets:
            returnMessage = "Hello {}, we found {} ticket(s) under your name: \n".format(userName, numberOfTickets)
            counter = 1
            for ticket in ticketsFound:
                returnMessage += "Ticket {} Number: {} From: {}\n".format(counter, ticket[0], ticket[1])
                counter += 1
            await ctx.send(returnMessage)
        else:
            await ctx.send("Hello, {} I couldn't find any Raffle Tickets under your name. Contact anyone with Tech Comm Role if you think that's wrong.".format(userName))

    
def setup(bot):
    bot.add_cog(checkNumber(bot))