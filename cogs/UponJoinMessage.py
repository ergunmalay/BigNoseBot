import discord
from discord.ext import commands


class UponJoinMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Connecting to server message
    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.bot))

        # Confirmation of the bot working
        general_channel = self.bot.get_channel(786696328323399712)
        botpfp = self.bot.user.avatar_url

        ConnectEmbed = discord.Embed(title="Connected", description="Big Nose Bot Has been connected.", color=0x4c00ff)
        ConnectEmbed.set_thumbnail(url=botpfp)
        ConnectEmbed.set_author(name=self.bot.user)

        await general_channel.send(embed=ConnectEmbed)


def setup(bot):
    bot.add_cog(UponJoinMessage(bot))
