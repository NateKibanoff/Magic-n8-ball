import discord
import os
from keep_alive import keep_alive
from random import randint
import json

client = discord.Client()

responses = json.loads(os.getenv("RESPONSES"))

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game("with Matchan's fate"))
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content[:3] == "?n8":
		await message.reply(responses[randint(0,len(responses)-1)])

keep_alive()
client.run(os.getenv("TOKEN"))