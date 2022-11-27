import discord
import os
from dotenv import load_dotenv
#from discord.ext.commands import Bot

load_dotenv()

TOKEN = os.environ.get('TOKEN')

print(TOKEN)

client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    user_message = str(message.content)

    if message.author == client.user:
        return

    if message.channel.name == 'general' or message.channel.id == 1005944053562617887:
        if 'forgor' in user_message.lower():
            await message.add_reaction('\N{skull}')
            return
        elif 'did i ask' in user_message.lower():
            await message.channel.send('shut the fuck up')
            return
        elif 'when' in user_message.lower():
            await message.channel.send('Did u mean wenomechaindasama?')
            await message.channel.send(
                file=discord.File('wenomechainsama-dog.jpg'))
            return
        elif '?' in user_message.lower():
            await message.channel.send(
                'Teacher I suspect the answer to your question is four teacher'
            )
            await message.channel.send(file=discord.File('cover1.jpg'))
            return
        else:
            return

client.run(TOKEN)
