import discord
from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        if isinstance(error, commands.MissingPermissions):
            PermsEmbed = discord.Embed(title="You do not have the correct permissions.", color=0x4c00ff)
            await context.message.channel.send(embed=PermsEmbed)

        elif isinstance(error, commands.UserNotFound):
            PermsEmbed = discord.Embed(
                title="I could not find that member, Make sure to @ the member. \nPlease try again.",
                color=0x4c00ff)
            await context.message.channel.send(embed=PermsEmbed)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
