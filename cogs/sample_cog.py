import random

import discord
from discord.ext import commands


class SampleCog(commands.Cog):

    def __init__(self, bot):
        self._bot = bot

    @commands.command()
    async def hello(self, ctx) -> None:
        await ctx.send(f'Hello world')

    @commands.command()
    async def dice(self, ctx, number):
        rnum = random.randint(1, 6)
        if int(number) == rnum:
            return await ctx.send(f'Got the right number: {rnum}')
        await ctx.send(f'Wrong number, the correct was: {rnum}')

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """
        This functions runs whenever the bot starts and is ready
        :return: None
        """
        print(f'Bot started successfully')

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        This function runs whenever a message is sent to any channel in the guild.
        :param message: The message that was sent (object)
        :return: None
        """
        if message.author == self._bot.user:
            return
        # await message.channel.send(f'User {message.author.name} sent a message')


async def setup(bot: commands.Bot):
    await bot.add_cog(SampleCog(bot))
