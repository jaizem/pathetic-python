"""
Discord Bot Code 
J. Miller
3-15-2022
"""
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#check that its running
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    
@client.event
async def on_message(message):
    #ignore bot messages
    if message.author == client.user:
        return

    tired_quotes = [
        'me2 lol',
        'aren\'t we all?',
        'when are you not',
    ]

    apex_quotes = [
        'YOOOOOOO',
        'someone say apex???',
        'on my way',
    ]

    if 'tired' in message.content:
        response = random.choice(tired_quotes)
        await message.channel.send(response)
    
    if 'apex' in message.content:
        response = random.choice(apex_quotes)
        await message.channel.send(response)

client.run(TOKEN)