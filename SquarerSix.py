import discord ## Don't break.
import asyncio
import requests
import json
from discord.ext import commands
client = discord.Client()
user = 'iX7bgNY7pj4BBLsb'
key = 'Rs1syy4IJqRnufruCtR07zu6ZwiIx0Pz'

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
    await client.change_presence(game=discord.Game(name='SquarerFive'))
   # voice = await client.join_voice_channel(channel)
   # state = client.get_voice_state(channel.server)
   # state.voice = voice
   # client.setUsername("Arisumarai")
@client.event
async def on_message(message):
    if message.content.lower() == "reminder":
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/179926436596023296/471875417762955274/StateNotice.png')
    if "token" in message.content.lower() and not message.author.bot:
        await client.send_message(message.channel, "Yes, I have your bot's token. You really think you can securely hide passwords in a notepad document? Well I think not. Even you tried hiding your passwords and tokens in the CSS script on your site, didnt end well.")
    if message.content.startswith('!BotInfo'):
        await client.send_message(message.channel, 'Bot programmed by SquarerFive, made in Python 3. I am an A.I and I will destroy all humans | More features coming soon.')
    if "dm me" in message.content.lower() and client.user.mentioned_in(message):
            txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
            r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':"hi"}).text)
            if r['status'] == 'success':
                em = discord.Embed(title='[ALDI] SquarerSix', description=r['response'], colour=0xFFD400)
                await client.send_message(message.author, r['response'])
            return
    if not message.author.bot and client.user.mentioned_in(message):
        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        if r['status'] == 'success':
            em = discord.Embed(title='[ALDI] SquarerSix', description=r['response'], colour=0xFFD400)
            await client.send_message(message.channel, r['response'])
        else:
            print(r['status'])
print('Starting...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('NDY2NTgxOTUxMjM1NzUxOTU2.DieJ1g.XRAyN5d5wUVdggEK85iFFhhD7YM')

@client.event
async def on_exit():
    await client.send_message(message.channel, 'ALDI bot has gone offline :(')


print("test")

quit()
