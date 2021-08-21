import os
import math
import random
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class StrikeriaBotClient(commands.Bot):

    def __init__(self, command_prefix):
        commands.Bot.__init__(
            self,
            command_prefix=command_prefix,
        )

        @self.command(name='99')
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
            await ctx.channel.send(response)

        @self.command(name='ron')
        async def ron_swanson(ctx):
            response = requests.get(
                'http://ron-swanson-quotes.herokuapp.com/v2/quotes'
            )

            await ctx.send(response.json()[0])

        @self.command(name='kanye')
        async def kanye_west(ctx):
            response = requests.get(
                'https://api.kanye.rest/'
            )

            await ctx.send(response.json()['quote'])

        @self.command(name='dump')
        async def tronald_dump(ctx):
            response = requests.get(
                'https://www.tronalddump.io/random/quote'
            )

            await ctx.send(response.json()['value'])

        @self.command(name='share')
        async def test_run(ctx, arg):
            player_level = int(arg)
            min_level = int(round(player_level * 2 / 3, 0))
            max_level = int(round(player_level * 3 / 2, 0))
            await ctx.send(
                f'You can share with players between level {min_level} and '
                f'level {max_level}'
            )


bot = StrikeriaBotClient(command_prefix="!")
bot.run(TOKEN)
