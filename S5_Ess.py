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
async def say(ctx):
    """ Use this if you want the bot to talk for you. Usage: !say {message} . """
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
        em = discord.Embed(title='[ALDI] | Say', description=a[5:], colour=0xFFD400)
        await Client.send_message(b, embed=em)
        await Client.delete_message(ctx.message)

@Client.command(pass_context = True)
async def announce(ctx):
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    em = discord.Embed(title='[ALDI] | Announcement', description=a[10:], colour=0x0055FF)
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
**Version:** 1.0.1 // //
**Hosted Locations:**
*France [Redundency Server]*
*Sydney, Australia [Blue Mountains]*
*Hong Kong[Backup Server]*"""
    otherInfo= """
Creator: SquarerFive [id #4325].
**Contacts:**
*http://squarerfive.tk/*
*http://www.youtube.com/SquarerFiveStudios/*
__**Hosted Platform:**__   __**Main Server:**__
**Linux CentOS 7**       **Europe[Currently]**
**Windows 10**             **Sydney, Autralia[Blue Mountains]**

**/-----/**
C++ is clearly better than C#.
          """
    em = discord.Embed(title='[ALDI] Administrative Services', description=mainInfo, colour=0x0055FF)
    em2 = discord.Embed(title='[ALDI] Administrative Services', description=otherInfo, colour=0x0055FF)
    await Client.send_message(b, embed=em)
    await Client.send_message(b, embed=em2)

# rules
@Client.command(pass_context = True)
async def rules(ctx):
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    rules="""
**Rules of conduct:**
**You** are responsible of what you type and say.
Any abuse against members and staff will result in a warning.
If a member reaches a threshold of **3 Warnings**, you will be **Banned** or **Kicked** depending on the violation.
Bots do not kick members randomly.

**/ Do and Don'ts /**
**You Can:**
Post Discord links in #advertisements.
Post YouTube/Twitch links in #media.
Curse passively.
Talk freely.
**/------/**
**You Can't:**
**You may not** post any images or content that is related to porn or gore/death.
**You may not** create multiple accounts for spam or to avoid the bans (IPs are tracked).
**You may not** post Discord Links in channels that are not #advertisements.

**/-----/**
These rules are subject to **change** at **any time**.
Discord ToS/Guidelines apply here too.
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
        em = discord.Embed(title='[ALDI] | Spank', description=desc, colour=0x0055FF)
        await Client.send_message(b, embed=em)
    else:
        em2 = discord.Embed(title='[ALDI] Administrative Services', description="You cannot spank users with those hands " + c.mention +".", colour=0x0055FF)
        await Client.send_message(b, embed=em2)
@Client.command(pass_context = True)
async def yell(ctx):
    a=ctx.message.content
    b=ctx.message.channel
    c=ctx.message.author
    em = discord.Embed(title='[ALDI] | Yell', description=a[4:], colour=0xFF0000)
    await Client.send_message(b, embed=em)
    await Client.delete_message(ctx.message)
#@Client.event

    
Client.run(Token)
