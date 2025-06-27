import json
import discord
from discord.ext import commands

LOJA_FILE = "loja.json"

def carregar_loja():
    try:
        with open(LOJA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_loja(dados_loja):
    with open(LOJA_FILE, 'w') as f:
        json.dump(dados_loja, f)


class Catalogo_loja(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def loja(self, ctx):
        dados_loja = carregar_loja()  # carrega o JSON como dicionário

        embedVar = discord.Embed(title="🛒 Itens da Loja", description="Confira os itens disponíveis para compra!", color=0xffd1dc)
        embedVar.set_author(
            name="Aya",
            icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&"
        )

        for item, info in dados_loja.items():
            nome = info.get("Nome", item)
            preco = info.get("Preço", "??")
            quantidade = info.get("Quantidade", "??")
            embedVar.add_field(
                name=f"💫 {nome.capitalize()}",
                value=f"💰 Preço: {preco} Moedas\n📦 Em estoque: {quantidade}",
                inline=False
            )

        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(Catalogo_loja(bot))


