import discord
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
    
    
client.run("MTAyOTQxMjI0ODkyMzQwNjM2Ng.G9XLgv.gk5uhpnRc6WsvEJjDfIQyHxy2gjkeFb3tH2jRA")