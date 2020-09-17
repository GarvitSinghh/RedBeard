from discord.ext import commands
import os
import time
from utils.functions import check, getAnswer
from selenium import webdriver
import random
import asyncio
from utils.lists import activities, statuses

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 ' \
             'Safari/537.36 '

bot = commands.Bot(
    command_prefix='',
    case_insensitive=True
)

for file in os.listdir('cogs'):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")


@bot.command()
async def AI(ctx):
    sessions = 0
    talkedFile = open("talkedBefore.txt", "r")
    talkedBefore = talkedFile.read()
    talkedBefore = talkedBefore.split("\n")
    talkedFile.close()

    if sessions == 0:
        driver.get("https://www.cleverbot.com/")
        print("Reached Cleverbot")
        try:
            btn = driver.find_element_by_xpath("//*[@id=\"noteb\"]/form/input")
            btn.click()
        except:
            pass
        if not any(str(id_of_person) in str(ctx.author.id) for id_of_person in talkedBefore):
            talkedFileWrite = open("talkedBefore.txt", "a")
            talkedFileWrite.write(f"\n{ctx.author.id}")
            talkedFileWrite.close()
            async with ctx.typing():
                time.sleep((bot.latency * 2) + 1)
            await ctx.send('Hey, I guess this is our first time talking!')
            await ctx.send("Hey, you are now talking to my AI!. You can say See you later to quit!")
            async with ctx.typing():
                time.sleep((bot.latency * 2) + 2)
            await ctx.send("So.... You can start the conversation!")
            talkedBefore.append(ctx.author)
        else:
            async with ctx.typing():
                time.sleep((bot.latency * 2) + 2)
            await ctx.send("I see we've talked before. I doubt I should go over how I work and stuff again")
            async with ctx.typing():
                time.sleep((bot.latency * 2) + 1)
            await ctx.send("Okay so skipping all that, you can start! the convo!")
        sessions += 1
        while True:
            quest = await bot.wait_for('message', check=check(ctx.author), timeout=100)

            while quest.channel != ctx.message.channel:
                quest = await bot.wait_for('message', check=check(ctx.author), timeout=100)
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
                await ctx.send(getAnswer(quest.clean_content, driver))
            except:
                await ctx.send("Hmmmm")
    else:
        await ctx.send("I am talking to someone else right now... You can talk to me later!")


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
