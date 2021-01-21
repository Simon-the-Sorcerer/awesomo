'''
Discord Bot für den NERDSquad-Discord-Server
'''

import logging
from discord.ext import commands
import discord
import config

import modules.dates as dates
import modules.polls as polls

bot = commands.Bot(command_prefix='$')


# Logging Einstellungen
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:\
                                        %(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    '''
    Kurze Meldung, wenn der Login auf dem Server erfolgreich war
    '''
    print('We have logged in as {} '.format(bot.user.name))
    
    await bot.change_presence(activity=discord.Activity(name="Sending you $help", type=discord.ActivityType.competing))

# Eingebaute Kommandos deaktivieren
bot.remove_command('help')
bot.remove_command('next')


# Kommandos
@bot.command()
async def meddl(ctx):
    '''
    Mittelfränkische Begrüßung
    '''
    await ctx.send('Meddl Loide')
    await ctx.message.delete()


@bot.command()
async def hello(ctx):
    '''
    Der Bot stellt sich vor
    '''
    await ctx.send('Greetings, I am the A.W.E.S.O.M.-O 4000')
    await ctx.send('You could tell A.W.E.S.O.M.-O all of your most personal\
                   secrets.')
    await ctx.message.delete()


@bot.command()
async def info(ctx):
    '''
    Informationen über verbundene Server und den Autor
    '''
    embed = discord.Embed(title='A.W.E.S.O.M.-O 4000', description='Greetings,\
                          I am the A.W.E.S.O.M.-O 4000', color=0xab4642)

    # Informationen über den Autor
    embed.add_field(name="Author", value="MadPsymon")

    # Informationen über Anzahl der verbundenen Server
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)
    await ctx.message.delete()


@bot.command()
async def shrug(ctx):
    '''
    ¯\_(ツ)_/¯
    '''
    await ctx.send(r'¯\_(ツ)_/¯')
    await ctx.message.delete()


@bot.command()
async def next(ctx):
    '''
    Customer support
    '''
    await ctx.send('Another satisfied customer! Next!')
    await ctx.message.delete()


# Termine
@bot.command()
async def date(ctx, command='', date='', time='', *args):
    '''
    Kommando zum Erstellen von Terminen
    '''
    if command == 'create':
        await dates.create(ctx, date, time, args)


# Abstimmungen
@bot.command()
async def poll(ctx, command='', title='', *args):
    '''
    Kommando zum Erstellen von Terminen
    '''
    if command == 'create':
        await polls.create(ctx, title, args)


@bot.command()
async def help(ctx):
    '''
    Informationen über verfügbare Befehle
    '''
    embed = discord.Embed(title='A.W.E.S.O.M.-O 4000', description='Verfügbare\
                          Befehle:', color=0xab4642)

    embed.add_field(name='$meddl', value='Grußform, häufig angewendet in\
                    Mittelfranken', inline=False)
    embed.add_field(name='$hello', value='A.W.E.S.O.M-O stellt sich vor',
                    inline=False)
    embed.add_field(name='$next', value='Customer Support', inline=False)
    embed.add_field(name='$shrug', value=r'¯\_(ツ)_/¯', inline=False)
    embed.add_field(name='$help', value='Gibt diese Hilfe aus', inline=False)
    embed.add_field(name='$date create DATUM UHRZEIT BESCHREIBUNG', value='Erstellt\
                    einen neuen Termin\n\
                    z.B.: $dates create 2020-02-20 20:20 Rudi aus Buddeln grüßen',
                    inline=False)
    embed.add_field(name='$poll create "TITEL" Optionen', value='Erstellt\
                    eine neue Abstimmung\n\
                    z.B.: $poll create "Neues Radlfideo?" Ja Nein "zu kalt"',
                    inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()

bot.run(config.token)
