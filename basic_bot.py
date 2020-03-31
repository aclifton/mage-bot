import discord
from discord.ext import commands
import os
import random
import sys

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

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def mana(ctx, count: int = None):
    """Rolls a mana dice."""
    if not count:
        count = 1
    result = ' '.join(str(random.choice(bot.mana_dice)) for r in range(count))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

if len(sys.argv) != 2:
    print("usage:\n\t{0} {{discord_key}}".format(sys.argv[0]))
else:
    bot.run(sys.argv[1])
