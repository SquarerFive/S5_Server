import discord
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
    voice = await client.join_voice_channel(channel)
    state = client.get_voice_state(channel.server)
    state.voice = voice
@client.event
async def on_message(message):
    if message.content.startswith('!BotInfo'):
        await client.send_message(message.channel, 'Bot programmed by SquarerFive, made in Python 3. I am an A.I and I will destroy all humans | More features coming soon.')
    
    elif not message.author.bot:
     #   await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, r['response'] )
    
print('Starting...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('MzgwNjA3NDc0MTA3MTU0NDM1.DO7D3w.WA1SjqA0KjyFup0868ddHY6FldU')

@client.event
async def on_exit():
    await client.send_message(message.channel, 'ALDI bot has gone offline :(')


print("test")

quit()
