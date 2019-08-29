import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$meddl'):
        await message.channel.send('Meddl Loide!')

client.run(config.token)
