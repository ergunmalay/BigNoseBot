import discord
from discord.ext import commands


class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Mute command
    @commands.command(name="mute")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, context, member: discord.Member = None, *, reason="Reason not Specified"):
        if member == None:
            botpfp = self.bot.user.avatar_url

            await context.message.delete(delay=2)
            MuteEmbed = discord.Embed(title="mute Format", description="*Mute {Member} {Reason}",
                                      color=0x4c00ff)
            MuteEmbed.set_thumbnail(url=botpfp)

            await context.message.channel.send(embed=MuteEmbed)
        else:
            userpfp = member.avatar_url

            await context.message.delete(delay=2)
            role = discord.utils.get(member.guild.roles, name="Muted")
            await member.add_roles(role)

            MuteEmbed = discord.Embed(title="User " + member.display_name + " Has been Muted.", description=reason,
                                      color=0x4c00ff)
            MuteEmbed.set_thumbnail(url=userpfp)

            await context.message.channel.send(embed=MuteEmbed)


def setup(bot):
    bot.add_cog(MuteCommand(bot))
