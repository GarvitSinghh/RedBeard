import discord
from discord.ext import commands
from utils.functions import search_gif, get_gif_link
from utils.lists import colors
import random
import time


class GIFCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(2, 30, commands.BucketType.user)
    async def kill(self, ctx, *, person):

        GIF = search_gif('kill anime', 50)

        if 'redbeard' in person.lower():
            await ctx.send("Do you seriously think you can kill me? Idiot ")
        else:
            desc = ctx.author.name + ' kills ' + person
            embed = discord.Embed(
                title=None,
                description=desc,
                colour=random.choice(colors)
            )
            embed.set_image(url=get_gif_link(GIF))
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(2, 30, commands.BucketType.user)
    async def punch(self, ctx, *, person):
        GIF = search_gif('punch anime', 30)
        if 'redbeard' in person.lower():
            await ctx.send("You think you can punch me? Lol :joy:\nYou get punched now ")
            desc = "RedBeard punches " + ctx.author.name
        else:
            desc = ctx.author.name + ' punches ' + person
        embed = discord.Embed(
            title=None,
            description=desc,
            colour=random.choice(colors)
        )
        embed.set_image(url=get_gif_link(GIF))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(2, 30, commands.BucketType.user)
    async def slap(self, ctx, *, person):
        GIF = search_gif('slap anime', 20)
        if 'redbeard' in person.lower():
            await ctx.send("You think you can slap me? Lol :joy:\nYou get slapped now ")
            desc = "RedBeard punches " + ctx.author.name
        else:
            desc = ctx.author.name + ' slaps ' + person
        embed = discord.Embed(
            title=None,
            description=desc,
            colour=random.choice(colors)
        )
        embed.set_image(url=get_gif_link(GIF))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(2, 30, commands.BucketType.user)
    async def stare(self, ctx, *, person):
        GIF = search_gif('anime stare', 20)
        if person != "":
            desc = ctx.author.name + ' stares at ' + person
        else:
            desc = ctx.author.name + ' stares at the world'
        embed = discord.Embed(
            title=None,
            description=desc,
            colour=random.choice(colors)
        )
        embed.set_image(url=get_gif_link(GIF))
        await ctx.send(embed=embed)

        if 'redbeard' in person.lower():
            async with ctx.typing():
                time.sleep(1)
            await ctx.send(":eyes:")

    @commands.command()
    @commands.cooldown(2, 30, commands.BucketType.user)
    async def hug(self, ctx, *, person):
        GIF = search_gif('anime hug', 25)
        desc = ctx.author.name + ' hugs ' + person
        embed = discord.Embed(
            title=None,
            description=desc,
            colour=random.choice(colors)
        )
        embed.set_image(url=get_gif_link(GIF))
        await ctx.send(embed=embed)

        if 'redbeard' in person.lower():
            async with ctx.typing():
                time.sleep(1)
            await ctx.send("Alright I can give u a hug :hugging:")

    @commands.command()
    @commands.cooldown(2, 30, commands.BucketType.user)
    async def poke(self, ctx, *, person):
        GIF = search_gif('anime poke', 15)
        if 'redbeard' in person.lower():
            await ctx.send("Nah nah nah, you dont poke me :) I poke you")
            desc = "Redbeard pokes " + ctx.author.name
        else:
            desc = ctx.author.name + ' pokes ' + person
        embed = discord.Embed(
            title=None,
            description=desc,
            colour=random.choice(colors)
        )
        embed.set_image(url=get_gif_link(GIF))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(5, 30, commands.BucketType.user)
    async def GIF(self, ctx, *, search_item):
        try:
            await ctx.message.delete()
        except AttributeError:
            pass
        if ',' in search_item:
            a = search_item.split(",")
            GIF = search_gif(a[0], 25)
            desc = a[1]
            if not GIF:
                await ctx.send("No results found..")
                return
            else:
                embed = discord.Embed(
                    title=None,
                    description=desc,
                    colour=random.choice(colors)
                )
        else:
            GIF = search_gif(search_item, 25)
            embed = discord.Embed(
                colour=random.choice(colors)
            )
        embed.set_image(url=get_gif_link(GIF))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(GIFCommands(bot))
