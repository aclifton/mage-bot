import discord
from discord.ext import commands
import os
import random
import sys

red_die_url = "https://cf.geekdo-images.com/original/img/8vtZaagQ2VJFtSqcoEBLXqNSK38=/0x0/pic1554401.jpg"
green_die_url = "https://cf.geekdo-images.com/original/img/707hBm7V_9kfCRLTYilZhrL1OgM=/0x0/pic1554402.jpg"
blue_die_url = "https://cf.geekdo-images.com/original/img/W4gA5CFcVgcnIIZ46wnFMj0W9gw=/0x0/pic1554404.jpg"
white_die_url = "https://cf.geekdo-images.com/original/img/V4r-VJ947Mgt3BMNU_e8GT8uhPM=/0x0/pic1554399.jpg"
black_die_url = "https://cf.geekdo-images.com/original/img/n426rPLtbuAQQx2QxAoCkmkq6Uc=/0x0/pic1554405.jpg"
gold_die_url = "https://cf.geekdo-images.com/original/img/LE_fBgkU_nU5GfmHpLpYONvc78A=/0x0/pic1554403.jpg"

number_url_map = {\
    1:red_die_url,\
    2:green_die_url,\
    3:blue_die_url,\
    4:white_die_url,\
    5:black_die_url,\
    6:gold_die_url}

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
    for e in bot.emojis:
        if e.name == "red_die":
            bot.red_emoji = e
        if e.name == "green_die":
            bot.green_emoji = e
        if e.name == "blue_die":
            bot.blue_emoji = e
        if e.name == "white_die":
            bot.white_emoji = e
        if e.name == "black_die":
            bot.black_emoji = e
        if e.name == "gold_die":
            bot.gold_emoji = e
    
    bot.die_emoji_map = {\
    1:bot.red_emoji,\
    2:bot.green_emoji,\
    3:bot.blue_emoji,\
    4:bot.white_emoji,\
    5:bot.black_emoji,\
    6:bot.gold_emoji}

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
async def mana(ctx, count: int):
    """Rolls a mana dice."""
    # result = random.randint(1,6)
    # die_embed = discord.Embed().set_thumbnail(url=number_url_map[result])
    # await ctx.send(embed=die_embed)
    result = ', '.join(str(bot.die_emoji_map[random.randint(1, 6)]) for r in range(count))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

if len(sys.argv) != 2:
    print("usage:\n\t{0} {{discord_key}}".format(sys.argv[0]))
else:
    bot.run(sys.argv[1])
