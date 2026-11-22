import asyncio
import json
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

try:
    with open("datos.json", "r") as archivo:
        contador = json.load(archivo)
except FileNotFoundError:
    contador = {}

def guardar_datos():
    with open("datos.json", "w") as archivo:
        json.dump(contador, archivo)

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
    elif message.content.startswith("!saludo"):
        partes = message.content.split()
        nombre = partes[1]
        await message.channel.send("Hola " + nombre)
    elif message.content.startswith("!suma"):
        partes = message.content.split()
        numero1 = int(partes[1])
        if len(partes) == 3:
            numero2 = int(partes[2])
        else:
            numero2 = int(partes[3])
        resultado = numero1 + numero2
        await message.channel.send("El resultado de la suma es: " + str(resultado))

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        nombre = member.name
        contador[nombre] = contador.get(nombre, 0) + 1
        await asyncio.to_thread(guardar_datos)
        canal = discord.utils.get(member.guild.text_channels, name="‼️-funas-‼️")
        await canal.send(nombre + " Entró a jugar 🎮( Van " + str(contador[nombre]) + " veces Ojito)")
    elif before.channel is not None and after.channel is None:
        canal = discord.utils.get(member.guild.text_channels, name="‼️-funas-‼️")
        await canal.send(member.name + " Salio del Canal 💩")
        print(member.name, "Salió del canal")

    

if not TOKEN:
    raise RuntimeError("Configura DISCORD_TOKEN en el archivo .env")

client.run(TOKEN)
