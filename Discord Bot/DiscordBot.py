# bot.py
import os
import discord
import Logic
from dotenv import load_dotenv

answer = Logic.readAnswers()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ask'):
        await message.channel.send(Logic.selectAns(answer))
    

client.run(TOKEN)
