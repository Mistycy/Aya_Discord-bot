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

class Adicionar_loja(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def adicionar_loja(self, ctx, nome_item: str, preco: int, quantidade: int ):
        dados_loja = carregar_loja()
        if nome_item in dados_loja:
            embedVar = discord.Embed(title="OPS!! 👾", description="", color=0xffd1dc)
            embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&")
            embedVar.add_field(name=f"❌ Este item ja existe na loja.", value=f"", inline=False)
            await ctx.send(embed=embedVar)
        else:
            dados_loja[nome_item] = {
                "Nome": nome_item,
                "Preço": preco,
                "Quantidade": quantidade
            }
            salvar_loja(dados_loja)
            embedVar = discord.Embed(title="Adicionar loja 🛒", description="", color=0xffd1dc)
            embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&")
            embedVar.add_field(name=f"✅Item {nome_item} adicionado com sucesso!", value=f"", inline=False)
            await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(Adicionar_loja(bot))