from discord.ext import commands
import os
import random
import asyncio
from utils.lists import activities, statuses

bot = commands.Bot(
    command_prefix='',
    case_insensitive=True
)

for file in os.listdir('cogs'):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")


async def change_status():
    await bot.wait_until_ready()
    while not bot.is_closed():
        channel = bot.get_channel(755657914722812004)
        await bot.change_presence(status=random.choice(statuses), activity=random.choice(activities))
        await channel.send("Bot status changed")
        await asyncio.sleep(3600)


bot.loop.create_task(change_status())
try:
    bot.run(os.environ.get("TOKEN"))
except Exception as e:
    print(f"Error when logging in: {e}")
