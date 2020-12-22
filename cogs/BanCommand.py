import discord
from discord.ext import commands


class BanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ban command
    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member = None, *, reason="Reason not Specified"):
        if member == None:
            botpfp = self.bot.user.avatar_url

            await context.message.delete(delay=2)
            BanEmbed = discord.Embed(title="Ban Format", description="*ban {Member} {Reason}", color=0x4c00ff)
            BanEmbed.set_thumbnail(url=botpfp)

            await context.message.channel.send(embed=BanEmbed)
        else:
            userpfp = member.avatar_url

            await context.message.delete(delay=2)
            await member.ban()
            BanEmbed = discord.Embed(title="User " + member.display_name + " Has been banned.", description=reason,
                                     color=0x4c00ff)
            BanEmbed.set_thumbnail(url=userpfp)

            await context.message.channel.send(embed=BanEmbed)


def setup(bot):
    bot.add_cog(BanCommand(bot))
