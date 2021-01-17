#!/usr/bin/env python3.9
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

#    if message.author == client.user:
#        return


    if message.content.startswith('hello'):
        await message.channel.send('bye bitch')

    if message.content.startswith('fuck you bitch'):
        await message.channel.send('ima fuck yo ass')
        #await message.channel.send('`ima fuck yo ass`')


    if message.content.startswith("<@712028429880524902>"):
        try:
            rod_ph = ["muerto de hambre", "veneco culiao", "machete"]
            await message.channel.send(rod_ph[random.randint(1, len(rod_ph))])
        except:
            await message.channel.send("puto")

    if message.content.startswith(".ping"):
        await message.channel.send(round(client.latency * 1000))

    if message.content.startswith(".user"):
        await message.channel.send(client.user)

    if message.content.startswith(".kiss"):
        await message.channel.send("https://media.tenor.com/images/ecc8393eb89ecc1594a1e406552c5a12/tenor.gif")
    
    if message.content.startswith(".nsfwano"):
        await message.channel.send("http://images.freebuddymovies.com/pic_teasers/47970/a960b057ce/nude/01/thumbs/47970_11_tb.jpg")




    print(message.content)
@client.event
async def on_message_delete(message):
    await message.channel.send("porquevergaseliminasesemensajehijodeputa")

TOKEN = "TOKEN"
client.run(TOKEN)

