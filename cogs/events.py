import discord
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import errors
import random
from utils.lists import activities, statuses


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        # block knight from spamming
        if message.content.upper().startswith("$SPAM"):
            knight = message.guild.get_member(740235240399962123)
            role = discord.utils.get(message.guild.roles, name='Spammer')
            await knight.remove_roles(role)
            await message.channel.send("No spamming idiot")

        self.bot.process_commands(message)

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
            print(f"Private Message > {ctx.author} > {ctx.message.clean_content}")

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
