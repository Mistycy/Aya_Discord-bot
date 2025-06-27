import discord
from discord.ext import commands

class Ajuda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Comando AJUDA
    @commands.command()
    async def ajuda(self, ctx):
        embedVar = discord.Embed(title="Lista de Comandos", description="", color=0xffd1dc)
        embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&")
        embedVar.add_field(name=f"!itens", value=f"mostra seu inventario", inline=False)
        embedVar.add_field(name=f"!saldo", value=f"mostra seu saldo atual", inline=False)
        embedVar.add_field(name=f"!loja", value=f"mostra o catalogo da loja", inline=False)
        embedVar.add_field(name=f"!comprar <item> <quantidade>", value=f"compra um item da loja", inline=False)
        embedVar.add_field(name=f"!transferir <membro> <quantidade>", value=f"Transfere moedas para outros jogadores", inline=False)

        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(Ajuda(bot))