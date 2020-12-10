import discord
from discord.ext import commands


class KickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Kick command
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member = None, *, reason="Reason not Specified"):
        if member == None:
            botpfp = self.bot.user.avatar_url

            await context.message.delete(delay=2)
            KickEmbed = discord.Embed(title="Kick Format Format", description="*kick {Member} {Reason}", color=0x4c00ff)
            KickEmbed.set_thumbnail(url=botpfp)

            await context.message.channel.send(embed=KickEmbed)
        else:
            userpfp = member.avatar_url

            await context.message.delete(delay=2)
            await member.kick()
            KickEmbed = discord.Embed(title="User " + member.display_name + " Has been kicked.", description=reason,
                                      color=0x4c00ff)
            KickEmbed.set_thumbnail(url=userpfp)

            await context.message.channel.send(embed=KickEmbed)


def setup(bot):
    bot.add_cog(KickCommand(bot))
