import discord
from discord.ext import commands

from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ajuda_adm(self, ctx):
        embedVar = discord.Embed(title="Lista de Comandos ADM", description="", color=0xffd1dc)
        embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&")
        embedVar.add_field(name=f"!ganhar <quantidade>", value=f"Seta uma quantidade de moedas para si mesmo", inline=False)
        embedVar.add_field(name=f"!retirar <quantidade>", value=f"remove uma quantidade especifica de moedas do seu inventario", inline=False)
        embedVar.add_field(name=f"!setar <membro> <quantidade>", value=f"seta uma quantidade de moedas para um usuário", inline=False)
        embedVar.add_field(name=f"!adicionar_loja <preço> <quantidade>", value=f"adiciona um item na loja", inline=False)
        embedVar.add_field(name=f"!remover_loja <preço> <quantidade>", value=f"remove um item na loja", inline=False)


        -await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(Ping(bot))








#Comando AJUDA_ADMIN