import discord
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import errors
import random
from utils.lists import activities, statuses
from discord import utils


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def getemote(self, arg):
        emoji = utils.get(self.bot.emojis, name=arg.strip(":"))

        if emoji is not None:
            if emoji.animated:
                add = "a"
            else:
                add = ""
            return f"<{add}:{emoji.name}:{emoji.id}>"
        else:
            return None

    async def getinstr(self, content):
        ret = []

        spc = content.split(" ")
        cnt = content.split(":")

        if len(cnt) > 1:
            for item in spc:
                if item.count(":") > 1:
                    wr = ""
                    if item.startswith("<") and item.endswith(">"):
                        ret.append(item)
                    else:
                        cnt = 0
                        for i in item:
                            if cnt == 2:
                                aaa = wr.replace(" ", "")
                                ret.append(aaa)
                                wr = ""
                                cnt = 0

                            if i != ":":
                                wr += i
                            else:
                                if wr == "" or cnt == 1:
                                    wr += " : "
                                    cnt += 1
                                else:
                                    aaa = wr.replace(" ", "")
                                    ret.append(aaa)
                                    wr = ":"
                                    cnt = 1

                        aaa = wr.replace(" ", "")
                        ret.append(aaa)
                else:
                    ret.append(item)
        else:
            return content

        return ret

    @commands.Cog.listener()
    async def on_message(self, message):
        if ":" in message.content:
            msg = await self.getinstr(message.content)
            ret = ""
            em = False
            smth = message.content.split(":")
            if len(smth) > 1:
                for word in msg:
                    if word.startswith(":") and word.endswith(":") and len(word) > 1:
                        emoji = await self.getemote(word)
                        if emoji is not None:
                            em = True
                            ret += f" {emoji}"
                        else:
                            ret += f" {word}"
                    else:
                        ret += f" {word}"

            else:
                ret += msg

            if em:
                try:
                    webhooks = await message.channel.webhooks()
                    webhook = utils.get(webhooks, name="Fake Webhook")
                    if webhook is None:
                        webhook = await message.channel.create_webhook(name="Fake webhook")
                except Exception as e:
                    print(e)
                    webhooks = await message.channel.webhooks()
                    for webhook in webhooks:
                        await webhook.delete()
                    webhooks = await message.channel.webhooks()
                    webhook = utils.get(webhooks, name="Fake Webhook")
                    if webhook is None:
                        webhook = await message.channel.create_webhook(name="Fake webhook")

                await webhook.send(ret, username=message.author.name, avatar_url=message.author.avatar_url)
                await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):

        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
            # helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
            # await ctx.send(f"Error in {helper}")
            pass

        elif isinstance(err, errors.CommandNotFound):
            pass

        elif isinstance(err, errors.CommandOnCooldown):
            ret = err.retry_after
            if ret > 60:
                await ctx.send(f"This command is on cooldown... try again in {ret//60} minutes")
            else:
                await ctx.send(f"This command is on cooldown... try again in {int(ret)} seconds")

        elif isinstance(err, TimeoutError):
            await ctx.send("Alright, I'll go now, Bye!")

    @commands.Cog.listener()
    async def on_command(self, ctx):
        try:
            print(f"{ctx.guild.name} > {ctx.author} > {ctx.message.clean_content}")
        except AttributeError:
            print(
                f"Private Message > {ctx.author} > {ctx.message.clean_content}")

    @commands.Cog.listener()
    async def on_ready(self):
        if not hasattr(self.bot, 'uptime'):
            self.bot.uptime = datetime.utcnow()
        print(f"Bot is ready, {self.bot.user}\n{len(self.bot.guilds)} Servers")
        channel = self.bot.get_channel(755657914722812004)
        await channel.send(f"Bot is ready, @{self.bot.user}\n{len(self.bot.guilds)} Servers\nLoaded Cogs:")

        extensions = self.bot.extensions
        msg = ""
        for extension in extensions:
            msg += extension + "\n"

        await channel.send(f"```css\n{msg}```")

        await self.bot.change_presence(status=random.choice(statuses), activity=random.choice(activities))


def setup(bot):
    bot.add_cog(Events(bot))
