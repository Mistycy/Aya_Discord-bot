import discord
from discord.ext import commands
import os 
from dotenv import set_key
from pathlib import Path

env_path = Path(".env")
class configurar_autorole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def configurar_autorole(self, ctx, *, name: str):
        set_key(env_path, "AUTO_ROLE", name)
        await ctx.send("configurado")



async def setup(bot):
    await bot.add_cog(configurar_autorole(bot))
