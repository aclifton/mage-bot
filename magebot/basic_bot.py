import discord
from discord.ext import commands
import os
import random
import sys
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.mana_dice = []
    for e in bot.emojis:
        if e.name.startswith('die_'):
            bot.mana_dice.append(e)
            
@bot.command(enabled=False)
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description="Rolls a mana dice using custom emojis as display")
async def mana(ctx, count: int = None):
    """Rolls a mana dice."""
    if not count:
        count = 1
    result = ' '.join(str(random.choice(bot.mana_dice)) for r in range(count))
    result = str(ctx.message.author.mention)+ " rolled " + ' '.join(str(random.choice(bot.mana_dice)) for r in range(count))
    await ctx.send(result)

@bot.command(description="Picks n options from list.  Returns selected and remaining options")
async def pick(ctx, pick: int, *args):
    """Pick X from options"""
    options = list(args)
    selected = list()
    if pick > len(options):
        await ctx.send("Not enough options provided.")
        return
    while pick > 0 and len(options) > 0:
        selection = random.choice(options)
        selected.append(selection)
        options.remove(selection)
        pick = pick - 1
    reply = "remaining: {0}\nselected : {1}\n".format(" ".join(options)," ".join(selected))
    await ctx.send(reply)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def hand(ctx, command: str, *args):
    pass
    # await ctx.message.author.send(message)

bot.run(DISCORD_TOKEN)