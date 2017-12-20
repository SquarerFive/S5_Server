import discord
import asyncio
import requests
import json
from discord.ext import commands
from random import randint
x = 0

client = discord.Client()
user = 'iX7bgNY7pj4BBLsb'
key = 'Rs1syy4IJqRnufruCtR07zu6ZwiIx0Pz'
def generate_number():
    global x
    t = randint(0,99999)
    x = x + t
def reset_number():
    global x
    x = 0
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
    #await client.change_presence(game=discord.Game(name='ALDI Verification'))

@client.event
async def on_message(message):
    if message.content.startswith('!BotInfo'):
        await client.send_message(message.channel, 'You must type !help for info. !verify to verify your user.')
    correct = 0
    #392596605947215873
    
    if message.content.startswith('!verify'):
        generate_number()
        xc = str(x)
       # print(t)
        print(x)
        await client.send_message(message.author, xc)
        await client.send_message(message.channel, 'You have been send a code through direct message. Please enter it below. (Example: 123456)')
    xs = str(x)
    if not message.author.bot:
        if message.content.startswith(xs):
            print('correct')
            roles = 392596605947215873
            try:
                role = discord.utils.get(message.server.roles, name="Verified")
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
                reset_number()
            except discord.Forbidden:
                await client.send_message(message.channel, "I don't have perms to add roles. {BOT GLITCH} BEING RESOLVED")
                
    
            
        
            
        
            
    
print('Starting...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('MzkyODA3MzQyMjQ2MTk5Mjk3.DRsl6A.U_Ecd90uVdEpgKVoQlg5b5Th44A')

@client.event
async def on_exit():
    await client.send_message(message.channel, 'ALDI bot has gone offline :(')


print("test")

quit()
