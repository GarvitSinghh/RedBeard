import discord
from discord.ext import commands
from utils.lists import colors
import random


class ServerCommands(commands.Cog, name='Server Commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def suggest(self, ctx, *, sugg):

        try:
            channel = discord.utils.get(ctx.guild.channels, name="suggestions")
        except Exception as e:
            channel = "not found"
            print(e)

        if str(ctx.message.author.id) == "549084587855446016":
            await ctx.send(f"{channel} \n\n {self.bot.suggestion_channels}")
        if channel != "not found":
            embed = discord.Embed(
                title="Server Suggestion",
                description=sugg,
                color=random.choice(colors)
            )
            embed.set_author(name=ctx.message.author.display_name,
                             icon_url=ctx.message.author.avatar_url)
            message = await channel.send(embed=embed)
            await message.add_reaction("✅")
            await message.add_reaction("❌")

        else:
            await ctx.send("Please ask a moderator to create a channel named #suggestions")

        await ctx.message.delete()


def setup(bot):
    bot.add_cog(ServerCommands(bot))
