import discord
from discord.ext import commands


# Source: https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/mod.py
class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument("Invalid ID") from None
        else:
            return m.id


class ActionReason(commands.Converter):
    async def convert(self, ctx, argument):
        re = argument

        if len(re) > 512:
            reason_max = 512 - len(re) - len(argument)
            raise commands.BadArgument(f'Reason is too long ({len(argument)}/{reason_max})')
        return re


class ModeratorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        try:
            self.bot.remove_command('kick')
        except:
            pass
        try:
            self.bot.remove_command('ban')
        except:
            pass
        try:
            self.bot.remove_command('mute')
        except:
            pass

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick_(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        try:
            await member.kick(reason='No reason was given' if reason is None else reason)
            await ctx.send(
                f"{ctx.message.author.mention} has kicked {member.mention}\n Reason: {'No reason was given' if reason is None else reason}")
            await ctx.send(f"Success :white_check_mark:")

        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban_(self, ctx, member: MemberID, *, reason=None):
        await ctx.message.delete()
        m = ctx.guild.get_member(member)
        if m is None:
            await ctx.send("Invalid!")
        try:
            await ctx.guild.ban(discord.Object(id=member), reason='No reason was given' if reason is None else reason)
            await ctx.send(f"<@{member}> has been banned! \nReason: {'No reason was given' if reason is None else reason}")
            await ctx.send(f"Success :white_check_mark:")

        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban_(self, ctx, member: MemberID, *, reason=None):
        await ctx.message.delete()
        try:
            await ctx.guild.unban(discord.Object(id=member), reason='No reason was given' if reason is None else reason)
            await ctx.send(f"<@{member}> has been Unbanned! \nReason: {'No reason was given' if reason is None else reason}")
            await ctx.send("Success :white_check_mark:")
        except Exception as e:
            await ctx.send(e)


def setup(bot):
    bot.add_cog(ModeratorCommands(bot))
