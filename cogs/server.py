import discord
from discord.ext import commands
from utils.lists import colors
import random

class ServerCommands(commands.Cog, name='Server Commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def setSuggestionChannel(ctx):
        ctx.guild.suggestion_channel = ctx.channel
        await ctx.send("Current Channel has been set as the Suggestion Channel!")

    
    @commands.command()
    @commands.guild_only()
    async def suggest(ctx, suggestion):
        try:
            channel = ctx.guild.suggestion_channel
        except AttributeError:
            await ctx.send("Please ask a moderator to setup a suggestion channel using setSuggestionChannel!")
            return
        
        embed = discord.Embed(
            title=suggestion,
            color=random.choice(colors)
        )
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url))
        message = await ctx.guild.suggestion_channel.send(embed=embed)
        message.add_reaction("✅")
        message.add_reaction("❌")
        
        await ctx.message.delete();