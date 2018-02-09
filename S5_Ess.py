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
Token = 'MzkyODA3MzQyMjQ2MTk5Mjk3.DRsl6A.U_Ecd90uVdEpgKVoQlg5b5Th44A'
Client = Bot('!')
@Client.event
async def on_ready():
    print('Logged in as '+Client.user.name+' (ID:'+Client.user.id+') | '+str(len(Client.servers))+' servers')
    servers=str(len(Client.servers))
    print(servers)
    await Client.change_presence(game=discord.Game(name='[ALDI] | Connected to {}'.format(servers + ' server(s).')))


@Client.command(pass_context = True)
async def spank(ctx, user):
    a = ctx.message.content
    name = discord.utils.get(ctx.message.server.members, name=user)
    print(name[1:])
    await Client.say("Spanking user")
    if a.mentioned_in(user):
        print("Mentioned")
    print("Worked")
def is_me(m):
    return m.author == author
@Client.command(pass_context = True)
async def say(ctx):
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
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    em = discord.Embed(title='[ALDI] Announcement', description=a[10:], colour=0x0055FF)
    await Client.send_message(b, embed=em)
    await Client.delete_message(ctx.message)
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
    mainInfo= """[ALDI] Administrative Services, formerly known as SquarerFive_Essentials.
**Hosted Locations:**
*France [Redundency Server]*
*Sydney, Australia [Blue Mountains]*
*Hong Kong[Backup Server]*"""
    otherInfo= """Creator: SquarerFive [id #4325].
Contacts:
**http://squarerfive.tk/**
**http://www.youtube.com/SquarerFiveStudios/**
          """
    em = discord.Embed(title='[ALDI] Administrative Services', description=mainInfo, colour=0x0055FF)
    em2 = discord.Embed(title='[ALDI] Administrative Services', description=otherInfo, colour=0x0055FF)
    await Client.send_message(b, embed=em)
    await Client.send_message(b, embed=em2)
    
#@Client.event

    
Client.run(Token)
