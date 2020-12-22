import discord
from discord.ext import commands


class UnBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # UnBan command
    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban(self, context, id, *, reason="Reason not Specified"):
        botpfp = self.bot.user.avatar_url
        member = discord.Object(id)

        if member == None:
            await context.message.delete(delay=2)

            UnBanEmbed = discord.Embed(title="UnBan Format", description="*unban {Member ID} {Reason}", color=0x4c00ff)
            UnBanEmbed.set_thumbnail(url=botpfp)

            await context.message.channel.send(embed=UnBanEmbed)
        else:

            await context.message.delete(delay=2)

            #Unban
            await context.guild.unban(member)


            UnBanEmbed = discord.Embed(title="User with id " + id + " Has been unbanned.", description=reason,
                                       color=0x4c00ff)
            UnBanEmbed.set_thumbnail(url=botpfp)

            await context.message.channel.send(embed=UnBanEmbed)


def setup(bot):
    bot.add_cog(UnBan(bot))
