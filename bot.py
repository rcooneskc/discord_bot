import os
import random
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='ron')
async def ron_swanson(ctx):
    response = requests.get(
        'http://ron-swanson-quotes.herokuapp.com/v2/quotes'
    )

    await ctx.send(response.json()[0])


@bot.command(name='kanye')
async def kanye_west(ctx):
    response = requests.get(
        'https://api.kanye.rest/'
    )

    await ctx.send(response.json()['quote'])


@bot.command(name='dump')
async def tronald_dump(ctx):
    response = requests.get(
        'https://www.tronalddump.io/random/quote'
    )

    await ctx.send(response.json()['value'])


@bot.command(name='test')
async def test_run(ctx, arg):
    print(arg)
    await ctx.send(f'Your arg: {arg}')


bot.run(TOKEN)
