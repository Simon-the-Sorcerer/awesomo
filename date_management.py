'''
Modul zum Verwalten des Zockkalenders ACHTUNG: WIP!
'''

import datetime
import sqlite3
import discord

async def show(ctx):
    '''
    Termine ausgeben
    '''
    connection = sqlite3.connect('calendar.db')
    cursor = connection.cursor()
    sql = 'SELECT Date, Description FROM dates'
    cursor.execute(sql)
    rows = cursor.fetchall()

    embed = discord.Embed(title='Anstehende Zocktermine', description='', color=0xab4642)
    dates = ''
    descriptions = ''
    for row in rows:
        dates += row[0] + '\n'
        descriptions += row[1] + '\n'
    embed.add_field(name='Termin', value=dates, inline=True)
    embed.add_field(name='Beschreibung', value=descriptions, inline=True)
    connection.commit()
    connection.close()

    await ctx.send(embed=embed)
    await ctx.message.delete()

async def add(ctx, date, time, args):
    '''
    Termin hinzufügen
    '''
    if date == '' or not args:
        await ctx.send('Datum und/oder Beschreibung leer')
    else:
        connection = sqlite3.connect('calendar.db')
        cursor = connection.cursor()

        description = ''
        for arg in args:
            description += '{} '.format(arg)

        sql = 'INSERT INTO dates (Date, Description) VALUES ("{} {}",\
        "{}")'.format(date, time, description)
        cursor.execute(sql)

        connection.commit()
        connection.close()

        await ctx.send('Termin "{}" am {} um {} gespeichert'.format(description,
                                                                    date, time))
        await ctx.message.delete()

async def remind(channel):
    '''
    Anstehende Termine ausgeben
    '''
    connection = sqlite3.connect('calendar.db')
    cursor = connection.cursor()
    sql = 'SELECT Date, Description FROM dates'
    cursor.execute(sql)
    rows = cursor.fetchall()
    today = datetime.datetime.now().date().isoformat()
    dates = ''
    descriptions = ''
    for row in rows:
        if today in row[0]:
            dates += row[0] + '\n'
            descriptions += row[1] + '\n'
    embed = discord.Embed(title='Heute anstehende Zocktermine', description='', color=0xab4642)
    embed.add_field(name='Termin', value=row[0], inline=True)
    embed.add_field(name='Beschreibung', value=row[1], inline=True)

    connection.commit()
    connection.close()

    await channel.send(embed=embed)
