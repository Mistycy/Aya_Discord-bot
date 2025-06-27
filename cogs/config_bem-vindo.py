
import discord
from discord.ext import commands
import os
from dotenv import set_key
from pathlib import Path

env_path = Path(".env")

class configurar_bem_vindo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def config_welcome(self, ctx, id):
        set_key(env_path, "CHAT_BEM_VINDO", id)
        await ctx.send(f"Configurado com sucesso, canal de bem-vindos {id}")
    


async def setup(bot):
    await bot.add_cog(configurar_bem_vindo(bot)) 