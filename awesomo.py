import logging
import config
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

# Logging Einstellungen
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user.name))

@bot.command()
async def meddl(ctx):
    await ctx.send('Meddl Loide')
    await bot.delete_message(ctx.message)

bot.run(config.token)
