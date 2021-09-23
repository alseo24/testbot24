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

print('*** Bot started ***')
client.run('ODkwNTExNDAwMDQ3MzUzODU2.YUw3Xg.AfW58hQ-5DKNVmyVMaBAgQv0IRc')
print('*** Bot stopped ***')

