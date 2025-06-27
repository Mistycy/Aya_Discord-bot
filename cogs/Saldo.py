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

class Saldo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def saldo(self, ctx):
        dados = carregar_dados()
        usuario_id = str(ctx.author.id)
        

        if usuario_id not in dados:
            dados[usuario_id] = 100
            salvar_dados(dados)
        
        saldo = dados[usuario_id]

        embedVar = discord.Embed(title="Saldo de moedas 🪙", description="", color=0xffd1dc)
        embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&")
        embedVar.add_field(name=f"Jogador: {ctx.author.name}", value=f"O seu saldo de moedas é de: {saldo} moedas", inline=False)
        await ctx.send(embed=embedVar)


async def setup(bot):
    await bot.add_cog(Saldo(bot))