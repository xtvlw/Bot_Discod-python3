from random import randrange
from time import sleep
import discord
import sqlite3


element, NoneNumbers = "", []

args = ["lolis_images", "oppais_images", "hentai_images",
        "lolis_gifs", "oppais_gifs", "hentai_gifs"]

Commands = [".loli", ".oppai", ".hentai",
            ".gif-loli", ".gif-oppai", ".gif-hentai"]
Max_lens = [100, 100, 100, 100, 37, 100]

data = sqlite3.connect("DataBase.db")
cursor = data.cursor()

client = discord.Client()
token = "NzEwNDg0NTQzOTM2NjU5NTU4.XtBbiQ.zWAb4N-JTY6RFPVY3J75J4Aptjg"

Help_Message = (".loli => send a loli photo\n"
                ".oppai => send a oppai phote\n"
                ".hentai => send a hentai photo\n"
                ".gif-loli => send a loli gif\n"
                ".gif-oppai => send a oppai gif\n"
                ".gif-hentai => send a hentai gif\n")


def function(max_len, table):
    global element, NoneNumbers
    element_position = randrange(1, max_len)

    sleep(0.5)
    while element_position in NoneNumbers:
        element_position = randrange(1, max_len)
    NoneNumbers += [element_position]
    if len(NoneNumbers) == 20:
        NoneNumbers = []
    sleep(0.5)

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
    global element
    if message.author == client.user:
        return

    for i in range(len(Commands)):
        if message.content.startswith("-h") or message.content.startswith("--help"):
            await message.channel.send(Help_Message)
            break
        if message.content.startswith(Commands[i]):
            function(Max_lens[i], args[i])
            if i == 2 or i == 5:
                element = f"||{element}||"
            await message.channel.send(element)
            break


client.run(token)
data.close()
