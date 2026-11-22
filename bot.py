import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot conectado como", client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author, "dijo:", message.content)

    if message.content == "hola":
        await message.channel.send("¡Hola! ¿Cómo estás?")
    elif message.content == "!dado":
        numero = random.randint(1,6)
        await message.channel.send("Salió el " + str(numero))
    elif message.content == "kael":
        await message.channel.send("Es un novato sin duda el compa jajj")
    

if not TOKEN:
    raise RuntimeError("Configura DISCORD_TOKEN en el archivo .env")

client.run(TOKEN)
