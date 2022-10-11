import discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
 
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
 
@client.eventxss
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
    
 
# client.run("MTAyOTQxMjI0ODkyMzQwNjM2Ng.GoCrIo.ZbUTnn_ebiUkBT-JONBfAoDYaMJ23lW-xOWPgc")