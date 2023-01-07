import os
from dotenv import load_dotenv
import discord
import sys
import re
import datetime
import time

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def isTimeNow(time):
    now = datetime.datetime.now() + datetime.timedelta(seconds=30)
    time_str = now.strftime('%H:%M')

    return time_str == time

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    server_status_channel = client.get_channel(int(os.getenv('CHANNEL')))

    
    if len(sys.argv) == 1:
        await server_status_channel.send(file=discord.File('down.gif'))
    
        os.system("shutdown now")
    elif len(sys.argv) == 2:
        shutdownTime = sys.argv[1]

        match = re.search(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', shutdownTime)

        if match:
            os.system("shutdown {0}".format(sys.argv[1]))

            while not isTimeNow(shutdownTime):
                time.sleep(1)

            await server_status_channel.send(file=discord.File('down.gif'))
        else:
            print("ERROR: Wrong time format, please use: HH:MM")
    else:
        print('ERROR: Wrong number of arguments')



client.run(os.getenv('TOKEN'))