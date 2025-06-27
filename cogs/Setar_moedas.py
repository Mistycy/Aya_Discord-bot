import json
import discord
from discord.ext import commands

DATA_FILE = "economia.json"

def carregar_dados():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_dados(dados):
    with open(DATA_FILE, 'w') as f:
        json.dump(dados, f)

class Setar_moedas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setar(self, ctx, membro: discord.Member, quantidade: int):
        dados = carregar_dados()
        usuario_id = str(ctx.author.id)
        membro_id = str(membro.id)
    
        if membro_id not in dados:
            dados[membro_id] = 100


        dados[membro_id] += quantidade    
        salvar_dados(dados)

        embedVar = discord.Embed(title="Transferir ADM!! 🪙", description="", color=0xffd1dc)
        embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&")
        embedVar.add_field(name=f"⚒️O Administrador {ctx.author.name} ", value=f"transferiu {quantidade} moedas para o jogador {membro.name}", inline=False)
        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(Setar_moedas(bot))