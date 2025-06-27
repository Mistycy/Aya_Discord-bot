import json
import discord
from discord.ext import commands

INVENTARIO_FILE = "Inventario.json"

def carregar_itens():
    try:
        with open(INVENTARIO_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_itens(dados_itens):
    with open(INVENTARIO_FILE, 'w') as f:
        json.dump(dados_itens, f, indent=4)

class Inventario(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inventario(self, ctx):
        itens = carregar_itens()
        usuario_id = str(ctx.author.id)

        if usuario_id not in itens or not itens[usuario_id]:
            embedVar = discord.Embed(title="OPS! ❌ 🎒", description="", color=0xffd1dc)
            embedVar.set_author(
                name="Aya", 
                icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg"
            )
            embedVar.add_field(name="Você não tem nenhum item.😢", value="", inline=False)
            await ctx.send(embed=embedVar)
            return

        inventario = itens[usuario_id]
        resposta = ""

        for nome_item, quantidade in inventario.items():
            # Ignora qualquer chave que não seja item real
            if nome_item.lower() not in ['nome', 'quantidade']:
                resposta += f"- {nome_item}: {quantidade}\n"

        embedVar = discord.Embed(title="Inventário 🎒", description="", color=0xffd1dc)
        embedVar.set_author(
            name="Aya", 
            icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg"
        )
        embedVar.add_field(name=f"Mochila de {ctx.author.name}:", value=resposta or "Vazia.", inline=False)
        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(Inventario(bot))
