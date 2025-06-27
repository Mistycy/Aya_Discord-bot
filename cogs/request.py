import discord
import requests
from discord.ext import commands

class request(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def request(self, ctx):
        site = requests.get("https://www.google.com.br/")
        await ctx.send(site.status_code)

async def setup(bot):
    await bot.add_cog(request(bot))