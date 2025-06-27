"""⠀                    
Feito com amor - 𝓑𝔂 𝓶𝓪𝓽𝓱𝔂 💕💕💕💕💕💕💕💕
"""

"""

DECLARAÇÃO DAS BIBLIOTECAS


"""
import requests
import openai
import discord
from discord.ext import commands
import json
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Permissão para ler mensagens
bot = commands.Bot(command_prefix='!', intents=intents)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("BOT_TOKEN"))

@bot.event
async def on_ready():    
    print(f'Bot {bot.user} está online e pronto para uso! ')
    await bot.change_presence(activity=discord.Game(name="Fazendo chá e biscoitos para meus amigos."))
    # Coloque o token do seu bot abaixo
asyncio.run(main())




