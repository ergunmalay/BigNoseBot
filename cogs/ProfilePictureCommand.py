import discord
from discord.ext import commands


class ProfilePictureCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Profile Picture Command

    @commands.command(name="pfp")
    async def pfp(self, context, member: discord.Member = None):
        if member == None:

            Person = context.message.author

            userpfp = Person.avatar_url

            MyEmbed = discord.Embed(title="This is the Profile picture of", description="{}".format(Person.mention),
                                    color=0x4c00ff)
            MyEmbed.set_image(url=userpfp)
            MyEmbed.set_author(name=self.bot.user)

            await context.message.channel.send(embed=MyEmbed)
        else:
            userpfp = member.avatar_url

            MyEmbed = discord.Embed(title="This is the Profile picture of", description="{}".format(member.mention),
                                    color=0x4c00ff)
            MyEmbed.set_image(url=userpfp)
            MyEmbed.set_author(name=self.bot.user)

            await context.message.channel.send(embed=MyEmbed)


def setup(bot):
    bot.add_cog(ProfilePictureCommand(bot))
