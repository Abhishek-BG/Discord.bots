import discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
 
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
 
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
client.run("MTAyOTQxMjI0ODkyMzQwNjM2Ng.GzDmb2.relNxyQbTeFMVm_vaCzcqYjBarsRu0QyX4OxLE")