import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
 
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    list =[]
    if message.author == client.user:
        return
        
    if 'says what' in message.content:
        
        await message.channel.send(message.content.split()[0]+' says suck these nuts')
    
    
client.run(TOKEN)