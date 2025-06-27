import discord
from discord.ext import commands

class mensagemdireta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mnd(self, ctx, msg):
        await ctx.author.send(msg)
        await ctx.send("Mensagem enviada com sucesso!")

async def setup(bot):
    await bot.add_cog(mensagemdireta(bot))