import os
from dotenv import load_dotenv
import discord

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    server_status_channel = client.get_channel(1058740765636968500)

    await server_status_channel.send(file=discord.File('down.gif'))

    os.system("shutdown /s /t 1")


client.run(os.getenv('TOKEN'))