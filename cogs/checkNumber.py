from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
gc = gspread.service_account(filename="config/credentials.json")

f = open('config/googleSheets.json')
data = json.load(f)


generalAttendanceSheet = gc.open_by_key(data['generalAttendanceSheet'])
# artistAlleySheet = gc.open_by_key(data['artistAlleySheet'])
# raffleTicketSheet = gc.open_by_key(data['raffleTicketSheet'])
# panelEventSheet = gc.open_by_key(data['panelEventSheet'])
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
            await ctx.send("Hello, {} I couldn't find any Raffle Tickets under your name. Contact aanyone with Tech Comm Role if you think that's wrong.".format(userName))

    
def setup(bot):
    bot.add_cog(checkNumber(bot))