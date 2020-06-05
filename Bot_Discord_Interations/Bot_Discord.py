from random import randrange
import googletrans
import discord
import sqlite3


data = sqlite3.connect('database.db')
cursor = data.cursor()

img, style = "", ""

client = discord.Client()
token = "NzEwNDg0NTQzOTM2NjU5NTU4.XtUzSQ.MtKyuz0XmVscgwxReJWIA_EoiB0"
embed = discord.Embed

Help_Message = ("*kiss {pessoa} => todas as preferencias.\n"
                "*hug {pessoa} => todas as preferencias.\n"
                "*slap {pessoa} => todas as preferencias.\n"
                "-kiss {pessoa} => preferencia lesbica.\n"
                "-hug {pessoa} => preferencia lesbica.\n"
                "+kiss {pessoa} => preferencia homosexual.")

commands = ["*kiss", "*hug", "*slap", "-kiss", "-hug", "+kiss"]
MaxLen = [61, 51, 29, 38, 18, 38]
titles = ["amorzinho", "amorzinho", "briga briga", "Amorzinho", "Amorzinho", "Amorzinho"]
tables = ["kiss", "hugs", "slap", "kiss_yuri", "hugs_yuri", "kiss_yaoi"]
actions = ["beijou", "abraçou", "bateu em", "beijou", "abraçou", "beijou"]


def function(_title, table, max_table_len, author, person, option):
    global img, style
    element_position = randrange(0, max_table_len)
    element = cursor.execute(f"SELECT link FROM {table} WHERE id={element_position}")
    for i in element:
        img = i
        break
    img = f"{img[0]}"
    style = embed(title=f"{_title}", description=f"{author} {option} {person}")
    style.set_image(url=img)
    return style


def translator(message):
    global embed
    translator = googletrans.Translator()
    translation = translator.translate(message, dest="pt")
    translation = translation.text
    embed = discord.Embed(title=f"{message} = {translation}")



@client.event
async def on_ready():
    print("started!")
    return


@client.event
async def on_message(message):
    global embed
    message.content = message.content.lower()
    if message.content.startswith("--help"):
        embed = discord.Embed(title="HELP MESSAGE", description=Help_Message)
        await message.channel.send(embed=embed)

    if message.content.startswith("+translate"):
        msg = message.content[10:]
        translator(msg)
        await message.channel.send(embed=embed)

    for i in range(len(commands)):
        if message.content.startswith(commands[i]):
            function(titles[i], tables[i], MaxLen[i], message.author.mention, message.content[len(commands[i]):28], actions[i])
            await message.channel.send(embed=style)
            break

client.run(token)

