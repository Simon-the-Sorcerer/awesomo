'''
Modul zum Erstellen von Abstimmungen
'''

import discord


async def create(ctx, title, args):
    '''
    Abstimmung erstellen
    '''

    embed = discord.Embed(title=title, color=0xab4642)
    number = 1
    options = ""
    for arg in args:
        options += "{}\N{COMBINING ENCLOSING KEYCAP} {}\n".format(number, arg)
        number += 1

    embed.add_field(name='Optionen', value=options, inline=False)

    message = await ctx.send(embed=embed)

    for number in range(len(args)):
        await message.add_reaction("{}\N{COMBINING ENCLOSING KEYCAP}".format(number + 1))

    await ctx.message.delete()
