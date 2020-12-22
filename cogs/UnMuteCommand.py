import discord
from discord.ext import commands


class UnUnMuted(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # UnUnMuted command
    @commands.command(name="unmute")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, context, member: discord.Member = None, *, reason="Reason not Specified"):
        if member == None:
            botpfp = self.bot.user.avatar_url

            await context.message.delete(delay=2)
            UnMutedEmbed = discord.Embed(title="mute Format", description="*UnMuted {Member} {Reason}",
                                         color=0x4c00ff)
            UnMutedEmbed.set_thumbnail(url=botpfp)

            await context.message.channel.send(embed=UnMutedEmbed)
        else:
            userpfp = member.avatar_url

            await context.message.delete(delay=2)
            role = discord.utils.get(member.guild.roles, name="Muted")
            await member.remove_roles(role)

            UnMutedEmbed = discord.Embed(title="User " + member.display_name + " Has been UnMutedd.",
                                         description=reason,
                                         color=0x4c00ff)
            UnMutedEmbed.set_thumbnail(url=userpfp)

            await context.message.channel.send(embed=UnMutedEmbed)


def setup(bot):
    bot.add_cog(UnUnMuted(bot))
