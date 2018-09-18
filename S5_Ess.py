##########################################################################
# SquarerFive Essentials | Running as a seperate module for redundency.  #
# SquarerFive - 2018     | Python36 Discord.py                           #
##########################################################################
##                                                                       #
## Contact at squarerfive.tk                                             #
##                       https://www.youtube.com/SquarerFiveStudios      #
##########################################################################
message=("")
import asyncio
import discord
author=('')
from discord.ext.commands import Bot
import sys
Token = 'MzkyODA3MzQyMjQ2MTk5Mjk3.DoIsRA.Ht-U4Tlku0gdyYkaZl1f9nQ31GA'
Prefix = '!'
Client = Bot(Prefix)
@Client.event
async def on_ready():
    print('Logged in as '+Client.user.name+' (ID:'+Client.user.id+') | '+str(len(Client.servers))+' servers')
    servers=str(len(Client.servers))
    print(servers)
    await Client.change_presence(game=discord.Game(name='[ALDI] | Connected to {}'.format(servers + ' server(s).')))



@Client.command(pass_context = True)
async def say(ctx):
    """ Use this to send messages without yourself. """
    a=ctx.message.content
    print(a[5:])
    b=ctx.message.channel
    c=ctx.message.author
    if a[5:] == "C# > C++":
       await Client.say("C++ is clearly better")
       await Client.delete_message(ctx.message)
    if a[5:] == "C# > C++ > Python":
        await Client.say("C++ is clearly better")
        await Client.delete_message(ctx.message)
    else:
        em = discord.Embed(title='[ALDI] Administrative Services', description=a[5:], colour=0xFFD400)
        await Client.send_message(b, embed=em)
        await Client.delete_message(ctx.message)

@Client.command(pass_context = True)
async def announce(ctx):
    if(ctx.message.author.server_permissions.administrator):
        a=ctx.message.content
        b=ctx.message.channel
        c=ctx.message.author
        em = discord.Embed(title='[ALDI] Announcement', description=a[10:], colour=0x0055FF)
        await Client.send_message(b, embed=em)
        await Client.delete_message(ctx.message)
    else:
        a=ctx.message.content
        b=ctx.message.channel
        c=ctx.message.author
        em = discord.Embed(title='Error', description="Permissions Invalid! [E1:48P:32]")
@Client.command(pass_context = True)
async def s5fps(ctx):
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    em = discord.Embed(title='S5FPS', description=a[7:], colour=0x00ff11)
    await Client.send_message(b, embed=em)
    await Client.delete_message(ctx.message)
@Client.command(pass_context = True)
async def info(ctx):
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    em = discord.Embed(title='[ALDI] Administrative Services', description=mainInfo, colour=0x0055FF)
    em.set_author(name="[ALDI] SquarerFive", url="https://www.squarerfive.tk")
    em.add_field(name="About:", value="[ALDI] Administration is a bot specifically designed for the [ALDI] Discord Server. It will continually be updated over the months adding many features.", inline=False)
    em.add_field(name="Last Updated:", value="18 September 2018", inline=False)
    em.add_field(name="Prefix:", value=Prefix, inline=True)
    em.add_field(name="Hosted Servers:", value="H16 Europe", inline=False)
    em.add_field(name="Version:", value="1.1.0a", inline=False)
# em2 = discord.Embed(title='[ALDI] Administrative Services', description=otherInfo, colour=0x0055FF)
    await Client.send_message(b, embed=em)
   # await Client.send_message(b, embed=em2)

# rules
@Client.command(pass_context = True)
async def rules(ctx):
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    rules="""
[R14:982:F5]
"""
    em = discord.Embed(title='[ALDI] Administrative Services', description=rules, colour=0x0055FF)
    await Client.send_message(b, embed=em)

@Client.command(pass_context = True)
async def spank(ctx, user):
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    d=user
    desc=c.mention + " has spanked " + user + " " + a[29:]
   # await Client.say(desc)
    print(c.id)
    print(desc)
    if c.id == "176869575709687808":
        em = discord.Embed(title='[ALDI] Administrative Services', description=desc, colour=0x0055FF)
        await Client.send_message(b, embed=em)
    else:
        em2 = discord.Embed(title='[ALDI] Administrative Services', description="You cannot spank users with those hands " + c.mention +".", colour=0x0055FF)
        await Client.send_message(b, embed=em2)
@Client.command(pass_context = True)
async def purge(ctx, number):
    if(ctx.message.author.server_permissions.administrator):
        mgs = [] 
        number = int(number) 
        async for x in Client.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await Client.delete_messages(mgs)
    else:
        await Client.send_messsage(ctx.message.channel,"[E1:48P:32]")

@Client.command(pass_context = True)
async def iam(ctx):
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    print(a[5:])
    role=a[5:]
    roles=['YouTuber', 'sick dard', 'Subscribers']
    real_roles=['YouTubers/Streamers', 'sick dard', 'Subscribers']
    roleid=['350934547858325504']
    if a[5:] in roles:
        index = roles.index(role)
        print(index)
       # chosen = roleid[index]
        chosen_role = real_roles[index]
        role_name = roles[index]
        print(role_name)
        print(chosen_role)
        get_role = discord.utils.get(ctx.message.server.roles, name=chosen_role)
        await Client.add_roles(c, get_role)

@Client.command(pass_context = True)
async def commands(ctx):
    b=ctx.message.channel
    embed=discord.Embed(title="[ALDI] Administration Service", url="https://www.squarerfive.tk/", description="Here you will find all of the commands for my bot.", color=0x006fe8)
    embed.set_author(name="[ALDI] SquarerFive", url="https://www.squarerfive.tk")
    embed.add_field(name="Commands:", value="!say | Usage: !say {message}", inline=False)
    embed.add_field(name="!spank ", value="!spank | Usage: !spank {user.mention}", inline=False)
    embed.add_field(name="!iam ", value="!iam | Usage: !iam {role name}", inline=False)
    embed.add_field(name="!yell ", value="!yell | Usage: !yell {message}", inline=False)
    embed.add_field(name="!commands ", value="!commands | Used to display this.", inline=False)
    embed.add_field(name="!roles ", value="!roles | Used to display roles that are obtainable.", inline=False)
    embed.set_footer(text="© SquarerFive - 2018")
    await Client.send_message(b, embed=embed)

@Client.command(pass_context = True)
async def roles(ctx):
    b=ctx.message.channel
    embed=discord.Embed(title="[ALDI] Administration Service",url="https://www.squarerfive.tk/", description="Available roles: (Roles are case sensitive!)", color=0x006fe8)
    embed.set_author(name="[ALDI] SquarerFive", url="https://www.squarerfive.tk")
    embed.add_field(name="DEPRECIATED COMMAND", value="[D2:575:65]", inline=False)
    embed.add_field(name="DEPRECIATED COMMAND", value="[D2:575:65]", inline=False)
    embed.add_field(name="DEPRECIATED COMMAND", value="[D2:575:65]", inline=False)
    embed.set_footer(text="© SquarerFive - 2017")
    await Client.send_message(b, embed=embed)
    
Client.run(Token)
