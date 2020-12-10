# Import discord packages
from discord.ext import commands

# Client Our Bot
client = commands.Bot(command_prefix="*",
                      case_insensitive=True)  # case_insensitive=True makes all commands case insensitive :D

client.load_extension("cogs.ErrorHandler")
client.load_extension("cogs.UponJoinMessage")
client.load_extension("cogs.KickCommand")
client.load_extension("cogs.ProfilePictureCommand")
client.load_extension("cogs.BanCommand")

### DON'T REVEAL YOU FUCKING RETARDED MONKEY##
client.run('Nzg2MjM5MjI2MzA3NDExOTY4.X9DgVw.H_jrH8xz9v50ZdfpVHCvXG0tR68')
