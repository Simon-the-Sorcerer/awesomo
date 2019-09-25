'''
Discord Bot für den NERDSquad-Discord-Server
'''

import logging
import sqlite3
import sys
import os
from discord.ext import commands, tasks
import discord
import config

import date_management as dm

bot = commands.Bot(command_prefix='$')

# Datenbank für Zockkalender erstellen, falls sie nicht schon existiert
if not os.path.exists('calendar.db'):
    print('Neue Kalenderdatenbank wird erstellt')
    connection = sqlite3.connect('calendar.db')
    cursor = connection.cursor()
    sql = 'CREATE TABLE dates(\
            id INTEGER PRIMARY KEY,\
            Date DATE,\
            Description TEXT)'
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('Neue Kalenderdatenbank angelegt')
else:
    print('Vorhandene Kalenderdatenbank gefunden')


# Logging Einstellungen
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    '''
    Kurze Meldung, wenn der Login auf dem Server erfolgreich war
    '''
    date_reminder.start()
    print('We have logged in as {} '.format(bot.user.name))

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

# Zockkalender
@bot.command()
async def dates(ctx, command='', date='', time='', *args):
    '''
    Kommando zum Verwalten vom Zockkalender ACHTUNG: WIP!
    '''
    if command == '' or command == 'show':
        await dm.show(ctx)
    elif command == 'add':
        await dm.add(ctx, date, time, args)

@tasks.loop(hours=24)
async def date_reminder():
    logger.info('Reminder ausgeführt')
    channel = bot.get_channel(config.remind_channel)
    await dm.remind(channel)

# Eingebautes Hilfe-Kommando deaktivieren
bot.remove_command('help')
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
    embed.add_field(name='$dates show', value='Gibt Termine im Zockkalender aus', inline=False),
    embed.add_field(name='$dates add DATUM UHRZEIT BESCHREIBUNG', value='Trägt\
                    Termin in Zockkalender ein\n\
                    BEISPIEL: $dates add 2020-02-20 20:20 Rudi aus Buddeln\
                    grüßen', inline=False),
    embed.add_field(name='$help', value='Gibt diese Hilfe aus', inline=False)

    await ctx.send(embed=embed)
    await ctx.message.delete()

bot.run(config.token)
