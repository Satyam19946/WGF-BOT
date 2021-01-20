import numpy as np
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import json
gc = gspread.service_account(filename="config/credentials.json")
f = open('config/googleSheets.json')
data = json.load(f)


generalAttendanceSheet = gc.open_by_key(data['generalAttendanceSheet']).sheet1
generalAttendanceSheetData = generalAttendanceSheet.get_all_records()
artistAlleySheet = gc.open_by_key(data['artistAlleySheet']).sheet1
artistAlleySheetData = artistAlleySheet.get_all_records()
eventSheet = gc.open_by_key(data['eventSheet']).sheet1
eventSheetData = eventSheet.get_all_records()

userNameQuestion = 'Leave Your Discord Username with tag (like this xyz#1234) to access personalized Raffle features of WGF Bot.'
pidQuestion = 'If you are a UCSD Student, please enter your PID. (Leave Blank if Not)'
raffleNumber = 'Raffle Number'
firstName = 'First Name'

print(generalAttendanceSheetData)

#This will update the Raffle Numbers so every user has a raffle number.
def getTickets(username):
    ticketsFound = []
    for sheets in [generalAttendanceSheetData, artistAlleySheetData, eventSheetData]:
        if sheets[0][raffleNumber] == '':
            continue
        topTicketNumber = int(sheets[0][raffleNumber]) #Use the first entry as the beginning of raffle numbers
        print(topTicketNumber)
        for data in sheets:
            if data[userNameQuestion] == str(username):
                #Check if ticket has number if not assign it one
                ticketsFound.append(topTicketNumber)
            topTicketNumber += 1
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
                returnMessage += "Ticket {} Number: {}\n".format(counter, ticket)
                counter += 1
            await ctx.send(returnMessage)
        else:
            await ctx.send("Hello, {} I couldn't find any Raffle Tickets under your name. Contact aanyone with Tech Comm Role if you think that's wrong.".format(userName))

    
def setup(bot):
    bot.add_cog(checkNumber(bot))