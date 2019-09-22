'''
Modul zum Verwalten des Zockkalenders ACHTUNG: WIP!
'''

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

async def add(ctx, date, description):
    '''
    Termin hinzufügen
    '''
    if date == '' or description == '':
        await ctx.send('Datum und/oder Beschreibung leer')
    else:
        connection = sqlite3.connect('calendar.db')
        cursor = connection.cursor()

        sql = 'INSERT INTO dates (Date, Description) VALUES ("{}", "{}")'.format(date, description)
        cursor.execute(sql)

        connection.commit()
        connection.close()

        await ctx.send('Termin {} am {} gespeichert'.format(description, date))
        await ctx.message.delete()
