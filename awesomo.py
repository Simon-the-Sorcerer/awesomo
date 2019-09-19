import logging
import config
import discord
from discord.ext import commands

import date_management as dm

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
    await ctx.message.delete()

@bot.command()
async def hello(ctx):
    await ctx.send('Greetings, I am the A.W.E.S.O.M.-O 4000')
    await ctx.send('You could tell A.W.E.S.O.M.-O all of your most personal\
                   secrets.')
    await ctx.message.delete()

@bot.command()
async def info(ctx):
    embed = discord.Embed(title='A.W.E.S.O.M.-O 4000', description='Greetings,\
                          I am the A.W.E.S.O.M.-O 4000', color=0xab4642)

    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)
    await ctx.message.delete()

# Zockkalender
@bot.command()
async def dates(ctx, command='', date='', description=''):
    if command == '':
        await dm.show(ctx)
    elif command == 'add':
        await dm.add(ctx, date, description)

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='A.W.E.S.O.M.-O 4000', description='Verfügbare\
                          Befehle:', color=0xab4642)

    embed.add_field(name='$meddl', value='Grußform, häufig angewendet in\
                    Mittelfranken', inline=False)
    embed.add_field(name='$hello', value='A.W.E.S.O.M-O stellt sich vor',
                    inline=False)
    embed.add_field(name='$help', value='Gibt diese Hilfe aus', inline=False)

    await ctx.send(embed=embed)
    await ctx.message.delete()

bot.run(config.token)
