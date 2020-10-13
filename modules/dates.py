'''
Modul zum VErstellen von Terminen
'''

import discord
from discord.utils import get


async def create(ctx, date, time, args):
    '''
    Termine erstellen
    '''

    reactions = ['✅', '❌']

    description = ''
    for arg in args:
        description += '{} '.format(arg)

    title = '{} am {} um {} Uhr'.format(description, date, time)

    embed = discord.Embed(title=title, color=0xab4642)
    embed.add_field(name='Zusagen:', value='✅', inline=True)
    embed.add_field(name='Absagen:', value='❌', inline=True)

    message = await ctx.send(embed=embed)

    for name in reactions:
        emoji = get(ctx.guild.emojis, name=name)
        await message.add_reaction(emoji or name)

    await ctx.message.delete()
