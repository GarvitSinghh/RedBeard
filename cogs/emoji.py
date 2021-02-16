import discord
from discord.ext import commands
from discord import utils


class Emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_emoji(self, arg):
        emoji = utils.get(self.bot.emojis, name=arg.strip(":"))

        if emoji is not None:
            if emoji.animated:
                add = "a"
            else:
                add = ""
            return f"<{add}:{emoji.name}:{emoji.id}>"
        else:
            return None

    async def filter_string(self, content):
        ret = []

        spc = content.split(" ")
        cnt = content.split(":")

        if len(cnt) > 1:
            for item in spc:
                if item.count(":") > 1:
                    wr = ""
                    if item.startswith("<") and item.endswith(">"):
                        ret.append(item)
                    else:
                        cnt = 0
                        for i in item:
                            if cnt == 2:
                                aaa = wr.replace(" ", "")
                                ret.append(aaa)
                                wr = ""
                                cnt = 0

                            if i != ":":
                                wr += i
                            else:
                                if wr == "" or cnt == 1:
                                    wr += " : "
                                    cnt += 1
                                else:
                                    aaa = wr.replace(" ", "")
                                    ret.append(aaa)
                                    wr = ":"
                                    cnt = 1

                        aaa = wr.replace(" ", "")
                        ret.append(aaa)
                else:
                    ret.append(item)
        else:
            return content

        return ret

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if ":" in message.content:
            msg = await self.filter_string(message.content)
            ret = ""
            em = False
            smth = message.content.split(":")
            if len(smth) > 1:
                for word in msg:
                    if word.startswith(":") and word.endswith(":") and len(word) > 1:
                        emoji = await self.get_emoji(word)
                        if emoji is not None:
                            em = True
                            ret += f" {emoji}"
                        else:
                            ret += f" {word}"
                    else:
                        ret += f" {word}"

            else:
                ret += msg

            if em:
                try:
                    webhooks = await message.channel.webhooks()
                    webhook = utils.get(webhooks, name="Emoji Webhook")
                    if webhook is None:
                        webhook = await message.channel.create_webhook(name="Emoji Webhook")
                except Exception as e:
                    print(e)
                    webhooks = await message.channel.webhooks()
                    for webhook in webhooks:
                        await webhook.delete()
                    webhooks = await message.channel.webhooks()
                    webhook = utils.get(webhooks, name="Emoji Webhook")
                    if webhook is None:
                        webhook = await message.channel.create_webhook(name="Emoji Webhook")

                await webhook.send(ret, username=message.guild.get_member(message.author.id).nick, avatar_url=message.author.avatar_url)
                await message.delete()


def setup(bot):
    bot.add_cog(Emoji(bot))
