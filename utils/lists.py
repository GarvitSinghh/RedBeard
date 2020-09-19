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

responses = ["Fuck you, go away. Why do you think this piece of floating plastic has the answers you're looking for? Die in a fire.",
             "Please ask again.", "Why do you ask me? I'm just a friggin 8-ball! Get a life, loser...", "Can't you figure that out yourself?", "She's a murderer, dumbass.",
             "Can't you figure that out yourself?", "You sick idiot.", "How Do You Keep An Idiot Amused and Waste his time?? Ask again.", "What are you, stupid?", "Abducted By Aliens",
             "Pay Off Your Loans First", "Please die", "Wtf no", "Isn't that obvious? Dumbass"]

statuses = [discord.Status.online, discord.Status.idle]
