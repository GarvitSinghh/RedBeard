import random
import discord
from discord.ext import commands
from datetime import datetime
from utils.lists import colors
import time
import asyncio


class BasicCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command(aliases=['helpme'])
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def help(self, ctx,  what='Everything'):
        if what.lower() == 'everything':
            embed = discord.Embed(
                    title='Basic Help',
                    description='I have no prefix! Just consider me another member of this server!',
                    colour=random.choice(colors)
            )

            embed.add_field(name='Know my commands', value="You'll learn them as you talk haha", inline=False)
            embed.add_field(name="Anime GIF Commands", value="Kill, Stare, Punch, Slap, Hug and Poke", inline=False)
            embed.add_field(name="Other GIF Commands", value="Usage: GIF search\n(Tenor API)", inline=False)
            embed.add_field(name='AI', value="Takes some time to start, so wait!\nUsage: Just type ai", inline=True)
            embed.add_field(name="Description", value="Connects you to an Artificial Intelligence\n(Cleverbot)",
                            inline=True)
            embed.add_field(name="FLAMES", value="Usage: FLAMES \"name\" \"name2\"",
                            inline=False)
            embed.add_field(name="MEME", value="Usage: meme \"template\" \"text1\" \"text2\" ...")
            embed.add_field(name="Others", value="Invite: Invite the bot to your server\nSource: Get source code\nHelp: Get this help embed",
                            inline=False)

            embed.set_author(name="RedBeard", icon_url=self.bot.user.avatar_url)
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            embed.set_footer(text=f"(Page 1/1)\tToday at {current_time}\nnatsudragneel_x#6754")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def ping(self, ctx):
        ping = self.bot.latency * 1000
        before = time.monotonic()
        msg = await ctx.send(f"Pongg! :ping_pong: \nDiscord API Ping: {str(ping)[:5]}ms\n")
        after = time.monotonic()
        await msg.edit(content=f"Pongg! :ping_pong: \nDiscord API Ping: {str(ping)[:5]}ms\nMessage Roundtrip: {str((after-before)*1000)[:5]}ms")

    @commands.command()
    @commands.cooldown(1, 10)
    async def pong(self, ctx):
        await ctx.send("Pingg! :ping_pong:")

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def invite(self, ctx):
        link = discord.utils.oauth_url(self.bot.user.id)
        a = link.split('&')
        link = a[0] + "&permissions=8&" + a[1]
        await ctx.send(f"**{ctx.author.name}**, You can use this URL to invite me\n<{link}>")

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def source(self, ctx):
        link = "https://github.com/natsudragneel-x/RedBeard"
        await ctx.send(f"**{ctx.author.name}**, You can find my source code at\n<{link}>\nPlease star if you like it!")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number):
        await ctx.channel.purge(limit=int(number), check=lambda x: not x.pinned)
        msg = await ctx.send(f"Cleared {int(number)} messages")
        await asyncio.sleep(10)
        await msg.delete()
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(BasicCommands(bot))
