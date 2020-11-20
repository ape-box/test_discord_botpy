# bot.py
import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        await message.channel.send(f'hey {message.author.display_name}')
    if message.content == 'ping':
        await message.channel.send('pong')
    if message.author.display_name == 'SillyVan84':
        await message.channel.send('Grande Ale!')


client.run(TOKEN)
