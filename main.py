import os
from dotenv import load_dotenv
import discord
import json

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  server_status_channel = client.get_channel(1058740765636968500)
  print(server_status_channel)
  await server_status_channel.send(file=discord.File('online.png'))

# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return

#   print(message.content)
#   if message.content.startswith('$bitch'):
#     print(message)
#     await message.channel.send('Was geht bitch')


client.run(os.getenv('TOKEN'))