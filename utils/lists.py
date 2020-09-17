import discord

colors = [discord.Colour.blue(), discord.Colour.dark_gold(), discord.Colour.green(), discord.Colour.blurple(),
          discord.Colour.red(), discord.Colour.orange(), discord.Colour.magenta(), discord.Colour.dark_purple(),
          discord.Colour.purple(), discord.Colour.dark_teal(), discord.Colour.gold(), discord.Colour.teal(),
          discord.Colour.dark_blue(), discord.Colour.dark_green()]

activities = [discord.Game('Human | Type help for help'), discord.Game('Osu! | Type help for help'),
              discord.Game('with FBI | Type help for help'), discord.Game('Human | Type help for help'),
              discord.Activity(type=discord.ActivityType.watching, name="anime | Type help for help"),
              discord.Activity(type=discord.ActivityType.watching, name="Netflix | Type help for help"),
              discord.Activity(type=discord.ActivityType.watching, name="a movie | Type help for help"),
              discord.Activity(type=discord.ActivityType.listening, name="music | Type help for help"),
              discord.Game('Human | Type help for help')]

statuses = [discord.Status.online, discord.Status.idle]
