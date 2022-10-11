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
    
client.run("MTAyOTQxMjI0ODkyMzQwNjM2Ng.GeAPpf.2XY4v0Qbhqhpx3HaeljyL57URAM9q9YQceY_B4")