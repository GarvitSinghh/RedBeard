from discord.ext import commands
import os
import random
import asyncio
import time
from selenium import webdriver
from utils.lists import activities, statuses
from utils.functions import get_answer, check

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get(
    "CHROMEDRIVER_PATH"), chrome_options=chrome_options)


intents = discord.Intents().all()

bot = commands.Bot(
    command_prefix='',
    case_insensitive=True,
    intents=intents
)


@bot.command()
async def ai(ctx):
    driver.get("https://www.cleverbot.com/")
    try:
        btn = driver.find_element_by_xpath("//*[@id=\"noteb\"]/form/input")
        btn.click()
    except Exception as error:
        print(error)

    await ctx.send("Hi!")
    while True:
        quest = await bot.wait_for('message', check=check(ctx.author), timeout=300)
        while quest.channel != ctx.message.channel:
            quest = await bot.wait_for('message', check=check(ctx.author), timeout=300)
            quest = quest.clean_content
            quest.replace(">", '')
            quest.replace(":", '')
        if 'see you' in quest.clean_content.lower() or 'bye' in quest.clean_content.lower() or \
                'cya' in quest.clean_content.lower():
            await ctx.send("I'll talk to you later!")
            sessions = 0
            if sessions == 0:
                print(f"Sessions have been reset to {sessions}")
            break
        async with ctx.typing():
            time.sleep((bot.latency * 2) + 0.5)
        try:
            await ctx.send(get_answer(quest.clean_content, driver))
        except Exception as error:
            await ctx.send("Hmmm")
            print(error)


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
