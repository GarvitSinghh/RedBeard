import discord
from discord.ext import commands
from utils.lists import colors
import random


class ServerCommands(commands.Cog, name='Server Commands'):

    def __init__(self, bot):
        self.bot = bot
        self.bot.suggestion_channels = {}

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def setSuggestionChannel(self, ctx):
        self.bot.suggestion_channels[ctx.guild] = ctx.channel
        await ctx.send("Current Channel has been set as the Suggestion Channel!")

    @commands.command()
    @commands.guild_only()
    async def suggest(self, ctx, suggestion):

        await ctx.message.delete()

        channel = self.bot.get(ctx.guild, "not found")
        if channel != "not found":
            embed = discord.Embed(
                title=suggestion,
                color=random.choice(colors)
            )
            embed.set_author(name=ctx.message.author.display_name,
                             icon_url=ctx.message.author.avatar_url)
            message = await channel.send(embed=embed)
            message.add_reaction("✅")
            message.add_reaction("❌")

        else:
            await ctx.send("Please ask a moderator to set up a suggestion channel using `setSuggestionChannel`")


def setup(bot):
    bot.add_cog(ServerCommands(bot))
