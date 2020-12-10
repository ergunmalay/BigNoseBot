# Import discord packages
import discord
from discord.ext import commands

# Client Our Bot
client = commands.Bot(command_prefix="*",
                      case_insensitive=True)  # case_insensitive=True makes all commands case insensitive :D


# Connecting to server message
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    # Confirmation of the bot working
    general_channel = client.get_channel(743810554690273331)
    botpfp = client.user.avatar_url

    ConnectEmbed = discord.Embed(title="Connected", description="Big Nose Bot Has been connected.", color=0x4c00ff)
    ConnectEmbed.set_thumbnail(url=botpfp)
    ConnectEmbed.set_author(name=client.user)

    await general_channel.send(embed=ConnectEmbed)


# Profile Picture Command
@client.command(name="pfp")
async def pfp(context, ):
    user = context.message.mentions.users.first()
    userpfp = user.avatar_url

    MyEmbed = discord.Embed(title="This is the Profile picture of", description="{}".format(user.mention),
                            color=0x4c00ff)
    MyEmbed.set_image(url=userpfp)
    MyEmbed.set_author(name=client.user)

    await context.message.channel.send(embed=MyEmbed)


# Kick command
@client.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.User = None, *, reason="Reason not Specified"):
    if member == None:
        botpfp = client.user.avatar_url

        await context.message.delete(delay=2)
        KickEmbed = discord.Embed(title="Kick Format Format", description="*kick {Member} {Reason}", color=0x4c00ff)
        KickEmbed.set_thumbnail(url=botpfp)

        await context.message.channel.send(embed=KickEmbed)
    else:
        userpfp = member.avatar_url

        await context.message.delete(delay=2)
        KickEmbed = discord.Embed(title="User " + member.display_name + " Has been kicked.", description=reason,
                                  color=0x4c00ff)
        KickEmbed.set_thumbnail(url=userpfp)

        await context.message.channel.send(embed=KickEmbed)


# Ban command
@client.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(context, member: discord.User = None, *, reason="Reason not Specified"):
    if member == None:
        botpfp = client.user.avatar_url

        await context.message.delete(delay=2)
        BanEmbed = discord.Embed(title="Ban Format Format", description="*ban {Member} {Reason}", color=0x4c00ff)
        BanEmbed.set_thumbnail(url=botpfp)

        await context.message.channel.send(embed=BanEmbed)
    else:
        userpfp = member.avatar_url

        await context.message.delete(delay=2)
        BanEmbed = discord.Embed(title="User " + member.display_name + " Has been banned.", description=reason,
                                 color=0x4c00ff)
        BanEmbed.set_thumbnail(url=userpfp)

        await context.message.channel.send(embed=BanEmbed)


@client.event
async def on_command_error(context, error):
    if isinstance(error, commands.MissingPermissions):
        PermsEmbed = discord.Embed(title="You do not have the correct permissions.", color=0x4c00ff)
        await context.message.channel.send(embed=PermsEmbed)

    elif isinstance(error, commands.UserNotFound):
        PermsEmbed = discord.Embed(title="I could not find that member, Make sure to @ the member. \nPlease try again.",
                                   color=0x4c00ff)
        await context.message.channel.send(embed=PermsEmbed)





### DON'T REVEAL YOU FUCKING RETARDED MONKEY##
client.run('Nzg2MjM5MjI2MzA3NDExOTY4.X9DgVw.H_jrH8xz9v50ZdfpVHCvXG0tR68')
