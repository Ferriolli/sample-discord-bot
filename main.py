from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import asyncio


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
load_dotenv()


async def load_extensions():
    for file in os.listdir('cogs/'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    await load_extensions()
    await bot.start(os.getenv('bot_key'))


asyncio.run(main())
