"""
Discord Bot Code 
J. Miller
"""
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#check that client is connected and running
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    
@client.event
async def on_message(message):
    #use to ignore bot messages
    if message.author == client.user:
        return

    if 'hi' in message.content:
        await message.channel.send("Hello World")

client.run(TOKEN)
