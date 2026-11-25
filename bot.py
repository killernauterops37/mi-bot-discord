#Imports
#=======================================================================================================================
#=======================================================================================================================
import asyncio
import json
import os
import random

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Variables
#=======================================================================================================================
#=======================================================================================================================
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
#=======================================================================================================================
#=======================================================================================================================
try:
    with open("datos.json", "r") as archivo:
        contador = json.load(archivo)
except FileNotFoundError:
    contador = {}
#Def
#=======================================================================================================================
#=======================================================================================================================
def guardar_datos():
    with open("datos.json", "w") as archivo:
        json.dump(contador, archivo)
#=======================================================================================================================
#=======================================================================================================================
# Rama de @client.event
@client.event
async def on_ready():
    print("Bot conectado como", client.user)
    await tree.sync()
    print("Comandos / sincronizados")

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
        await canal.send(member.name + " 🏃 Salio del Canal el rata 💩🏃")
        print(member.name, "Salió del canal")
#=======================================================================================================================
#=======================================================================================================================
# Rama de @tree.command
@tree.command(name="saludo", description="El bot saluda")
async def saludo(interaction: discord.Interaction):
    nombre = interaction.user.name
    await interaction.response.send_message("🤖🎉¡Hola " + nombre + " 🎉🤖")
#=======================================================================================================================
#=======================================================================================================================
@tree.command(name="suma", description="Suma dos números 1️⃣➕1️⃣")
async def suma(interaction: discord.Interaction, numero1: int, numero2: int):
    resultado = numero1 + numero2
    await interaction.response.send_message("‼️El resultado es: " + str(resultado) + "✏️✏️")
#=======================================================================================================================
#=======================================================================================================================
@tree.command(name="dado", description="🎲Juego Del dado🎲")
async def dado(interaction: discord.Interaction):
    numero = random.randint(1,6)
    await interaction.response.send_message("🎲 Salio el: " + str(numero) + " 🎲 🎲")
#=======================================================================================================================
#=======================================================================================================================
@tree.command(name="ranking", description="🏆Muestra quíen ha entrado más veces a jugar🏆")
async def ranking(interaction: discord.Interaction):
    ordenado = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    texto = "=====🔥Ranking\n"
    for posicion, (nombre, cantidad) in enumerate(ordenado[:3], start=1):
        texto = texto + str(posicion) + ".🏆 " + nombre + " - " + str(cantidad) + "veces\n"
    await interaction.response.send_message(texto)
#=======================================================================================================================
#=======================================================================================================================






#=======================================================================================================================
#=======================================================================================================================
if not TOKEN:
    raise RuntimeError("Configura DISCORD_TOKEN en el archivo .env")

client.run(TOKEN)
