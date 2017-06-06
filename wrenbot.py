""" -----------------------------------------
Wrenbot - an autoresponder for Discord

This bot is designed to respond automatically
whenever the role for Overwatch is mentioned
in any given server.

Things to update: Call the name of the role
properly instead of the hack-y way using
str(value).
----------------------------------------- """
import discord

client = discord.Client()

@client.event
async def on_message(message):
    #Per the discord.py docs this is to not have the bot respond to itself
    if message.author == client.user:
        return
    #Test command.
    if message.content.startswith('!help'):
        msg = '{0.author.mention}, this bot is designed to auto-reply to any mention of the Overwatch role.'.format(message)
        await client.send_message(message.channel, msg)
    #Autoresponder for pinging Overwatch.
    for value in message.role_mentions:
        if str(value) == "Overwatch":
            msg = "Wrenbot says: Working so no."
            await client.send_message(message.channel, msg)
            return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run("TOKENID")
