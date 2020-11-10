import discord

client = discord.Client()
token = "NzEwNDg0NTQzOTM2NjU5NTU4.Xr1ISw.-BZB0Ov1Xu0kYD9sLmMnxg2JyqQ"

@client.event
async def on_ready():
    print("started!")
    return

@client.event
async def on_message(Message):
    if len(str(Message)) >= 400:
        user = Message.author
        await user.ban()

client.run(token)
