'''
Modul zum Verwalten des Zockkalenders ACHTUNG: WIP!
'''
async def show(ctx):
    '''
    Termine ausgeben
    '''
    await ctx.send('dates: show')
    await ctx.message.delete()

async def add(ctx, date, description):
    '''
    Termin hinzufügen
    '''
    if date == '' or description == '':
        await ctx.send('Datum und/oder Beschreibung leer')
    else:
        await ctx.send('dates: add Datum: {}, Beschreibung: {}'.format(date,
                                                                       description))
        await ctx.message.delete()
