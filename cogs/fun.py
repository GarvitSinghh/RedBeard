import random
import discord
from discord.ext import commands
from utils.memes import get_meme
from utils.lists import colors
import time


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def meme(self, ctx, *args):
        try:
            await ctx.message.delete()
        except:
            pass
        link = get_meme(*args)
        embed = discord.Embed(
            title=None,
            description=None,
            colour=random.choice(colors)
        )
        embed.set_author(name=f"{ctx.message.author.name}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url=link)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(12, 30, commands.BucketType.user)
    async def FLAMES(self, ctx, p1, p2):
        for i in p1:
            for j in p2:
                if i == j:
                    p1 = p1.replace(i, "", 1)
                    p2 = p2.replace(j, "", 1)
                    break
        count = len(p1 + p2)

        if count > 0:
            relation = ["Friends", "Lovers", "Affair", "Marriage", "Enemy", "Siblings"]
            while len(relation) > 1:
                split = (count % len(relation)) - 1
                if split >= 0:
                    right = relation[split + 1:]
                    left = relation[:split]
                    relation = right + left
                else:
                    relation = relation[:len(relation) - 1]
            relo = relation[0]
            letter = relo[0]
            printed = '~~F~~ ~~L~~ ~~A~~ ~~M~~ ~~E~~ ~~S~~'
            printed = printed.replace(f"~~{letter}~~", f"**{letter}**")
            async with ctx.typing():
                time.sleep(2)
            await ctx.send(printed)
            async with ctx.typing():
                time.sleep(0.5)
            ans = relation[0]
            await ctx.send(f"The relationship is {ans}")
        else:
            print("Invalid name")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def ban(self, ctx, *, useless=None):
        await ctx.send("Successfully Banned! :white_check_mark:")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def kick(self, ctx, user: discord.Member = None, *, useless=None):
        if user is not None:
            await ctx.send("Successfully Kicked! :white_check_mark:")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def mute(self, ctx, user: discord.Member = None, *, useless=None):
        if user is not None:
            await ctx.send("Successfully Muted! :white_check_mark:")


def setup(bot):
    bot.add_cog(FunCommands(bot))
