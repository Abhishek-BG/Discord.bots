import discord
import requests
import json 

def get_quotes():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+"-"+json_data[0]['a']
  return(quote)
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("Logged in {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$hi"):
    await message.channel.send("hello")
  if message.content.startswith("$quote"):
    quote = get_quotes()
    await message.channel.send(quote)


client.run('')
