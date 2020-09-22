from discord.ext import commands
import discord
from utils.lists import colors
import random
import ast
import os
from utils.functions import insert_returns
import utils


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

# Source : https://gist.github.com/nitros12/541d35ae72f32cc59ed4fb632278db8a
    @commands.command(aliases=['*eval'])
    @commands.is_owner()
    async def eval_fn(self, ctx, *, cmd):
        """Evaluates input.
        Input is interpreted as newline seperated statements.
        If the last statement is an expression, that is the return value.
        Usable globals:
          - `bot`: the bot instance
          - `discord`: the discord module
          - `commands`: the discord.ext.commands module
          - `ctx`: the invokation context
          - `__import__`: the builtin `__import__` function
        Such that `>eval 1 + 1` gives `2` as the result.
        The following invokation will cause the bot to send the text '9'
        to the channel of invokation and return '3' as the result of evaluating
        >eval ```
        a = 1 + 2
        b = a * 2
        await ctx.send(a + b)
        a
        ```
        """
        fn_name = "_eval_expr"

        cmd = cmd.strip("` ")

        # add a layer of indentation
        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

        # wrap in async def body
        body = f"async def {fn_name}():\n{cmd}"

        parsed = ast.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        env = {
            'bot': ctx.bot,
            'discord': discord,
            'commands': commands,
            'ctx': ctx,
            'os': os,
            'utils': utils,
            '__import__': __import__
        }
        exec(compile(parsed, filename="<ast>", mode="exec"), env)

        result = (await eval(f"{fn_name}()", env))
        await ctx.send(result)


def setup(bot):
    bot.add_cog(DevCommands(bot))
