# Last edit CV
# most of this is... inspired by
# https://github.com/therealOri/d-logger/blob/main/d-logger.py

import discord
from discord.ext import commands
import datetime, os, configparser, uuid

config = configparser.ConfigParser()
config.read('jarvis.conf')
bot_config = config['DISCORD BOT']

BOT_TOKEN = bot_config['token']
BOT_ID = bot_config['id']
BOT_PERMISSIONS = bot_config['permissions']

BOT_Prefix=tuple(bot_config['prefix'].split(' '))
#https://stackoverflow.com/questions/73458847/discord-py-error-message-discord-ext-commands-bot-privileged-message-content-i
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=BOT_Prefix, intents=intents)
client.remove_command("help")

@client.command()
async def help(ctx):
    author = ctx.message.author
    helpembed = discord.Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    helpembed.set_author(name="Help")
    helpembed.add_field(name="j.ping", value = "Standard ping pong command", inline=False)
    await ctx.send(embed=helpembed)

@client.event
async def on_ready():
    watching = discord.Streaming(type=1, url="https://ins.uni-bonn.de",
                                 name=f"j.help") # this is the bots status
    await client.change_presence(status=discord.Status.online, activity=watching)
    print(f"connection established, logged in as: {client.user.name}")

@client.event
async def on_guild_join(guild):
    print(f"i was invited to and have joined {guild}!")

image_types = bot_config['mediatype'].split(' ')
@client.event
async def on_message(message: discord.Message):
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            attach_dir = f"{message.author}"
            attach_path = f"{attach_dir}/{attachment.filename}"
            if not os.path.exists(attach_dir):
                os.makedirs(attach_dir)
            # if an attachment with this name exists, alter the name and report it
            if os.path.exists(attach_path):
                rnd_name = str(uuid.uuid4().hex)
                file_type = attachment.filename.split('.')[-1]
                attach_path = f"{attach_dir}/{rnd_name}.{file_type}"
                print(f'attachment renamed to {rnd_name}.{file_type}')
            await attachment.save(attach_path) # '{message.author}/{filename}' is the PATH to where the attachmets/images will be saved. Example: home/you/Desktop/civvi#5035/image.jpg
            print(f'attachment {attach_path} saved')
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")

client.run(BOT_TOKEN)