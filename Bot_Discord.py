import discord
from random import randrange
import sqlite3

element, NoneNumbers = "", []
args = ["lolis_images", "oppais_images", "hentai_images",
        "lolis_gifs", "oppais_gifs", "hentai_gifs"]

data = sqlite3.connect("DataBase.db")
cursor = data.cursor()

client = discord.Client()
token = "put your token here"


def function(max_len, table):
    global element, NoneNumbers
    element_position = randrange(1, max_len)

    while element_position in NoneNumbers:
        element_position = randrange(1, max_len)
    NoneNumbers += [element_position]

    element = cursor.execute(f"SELECT link FROM {table} WHERE id={element_position}")
    for i in element:
        element = i
        break
    element = f"{element[0]}"


@client.event
async def on_ready():
    print("STARTED")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.loli'):
        function(100, args[0])
        await message.channel.send(element)
    if message.content.startswith(".oppai"):
        function(100, args[1])
        await message.channel.send(element)
    if message.content.startswith(".hentai"):
        function(100, args[2])
        await message.channel.send(f'||{element}||')
    if message.content.startswith(".gif-loli"):
        function(100, args[3])
        await message.channel.send(element)
    if message.content.startswith(".gif-oppai"):
        function(37, args[4])
        await message.channel.send(element)
    if message.content.startswith(".gif-hentai"):
        function(100, args[5])
        await message.channel.send(f'||{element}||')
    if message.content.startswith("-h") or message.content.startswith("--help"):
        await message.channel.send(".loli => send a loli photo\n"
                                   ".oppai => send a oppai phote\n"
                                   ".hentai => send a hentai photo\n"
                                   ".gif-loli => send a loli gif\n"
                                   ".gif-oppai => send a oppai gif\n"
                                   ".gif-hentai => send a hentai gif\n")

client.run(token)
