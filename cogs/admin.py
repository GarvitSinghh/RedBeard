from discord.ext import commands
import discord
from utils.lists import colors
import random


class DevCommands(commands.Cog, name='Developer Commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rl'])
    @commands.is_owner()
    async def reload(self, ctx, cog):
        extensions = self.bot.extensions
        if cog == 'all':
            for extension in extensions:
                self.bot.unload_extension(extension)
                self.bot.load_extension(extension)
            await ctx.send('Done')
        if cog in extensions:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await ctx.send('Done')
        else:
            await ctx.send('Unknown Cog')

    @commands.command(aliases=['ul'])
    @commands.is_owner()
    async def unload(self, ctx, cog):
        extensions = self.bot.extensions
        if cog not in extensions:
            await ctx.send("Cog is not loaded!")
            return
        self.bot.unload_extension(cog)
        await ctx.send(f"`{cog}` has successfully been unloaded.")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog):
        try:
            self.bot.load_extension(cog)
            await ctx.send(f"`{cog}` has successfully been loaded.")

        except commands.errors.ExtensionNotFound:
            await ctx.send(f"`{cog}` does not exist!")

    @commands.command(aliases=['lc'])
    @commands.is_owner()
    async def listcogs(self, ctx):
        base_string = "```css\n"
        base_string += "\n".join([str(cog) for cog in self.bot.extensions])
        base_string += "\n```"
        await ctx.send(base_string)

    @commands.command()
    @commands.is_owner()
    async def sm(self, ctx, title, desc, url):
        embed = discord.Embed(
            title=title,
            description=desc,
            colour=random.choice(colors)
        )
        embed.set_image(url=url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(DevCommands(bot))
