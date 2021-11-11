import discord
import re
import requests
from io import BytesIO
from PIL import Image



intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


icon_size = 64


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_connect():
    game = discord.Game("*help - Try me!")
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!get server'):
        guild = message.guild
        k = 0
        for member in guild.members:
            response = requests.get(member.avatar_url)
            img = Image.open(BytesIO(response.content)).resize((64,64)).convert('RGB')
            img = img
            img.save(f"./Icons/Icon_{k}.jpg")
            k += 1
if __name__ == "__main__":
    client.run('OTA4MTM4MTUyMTk0MTEzNTc3.YYxXjw.KT3DZrYlCuBPRzM2x5G85cNM48k')