import discord
from discord.ext import commands
import json

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

class Add_moedas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


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


class Comprar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def comprar(seld, ctx, nome_item: str, quantidade: int):
    # Carregar os dados da loja, usuários e inventário
        dados_loja = carregar_loja()
        user_saldo = carregar_dados()
        inventario = carregar_itens()

        usuario_id = str(ctx.author.id)  # Converter ID para string

    # Verifica se o item existe na loja
        if nome_item not in dados_loja:
            embedVar = discord.Embed(title="OPS!! 👾", description="", color=0xffd1dc)
            embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1354104616307916863/1359347708762259546/20250323_154558.png?ex=67f726b5&is=67f5d535&hm=d7affefdf238fdbf5301d68e2c3e1339e2313473771c9dd60d8014ee0a7a46cd&")
            embedVar.add_field(name=f"❌ Este item não está disponível na loja!", value=f"", inline=False)
            await ctx.send(embed=embedVar)
            return

        item = dados_loja[nome_item]
        preco_total = item['Preço'] * quantidade  # Preço total da compra

    # Verifica se o usuário já tem um saldo registrado
        if usuario_id not in user_saldo:
            user_saldo[usuario_id] = 100  # Saldo inicial para novos usuários

        saldo = user_saldo[usuario_id]

    # Verificações de compra
        if quantidade <= 0:
            embedVar = discord.Embed(title="OPS!! 👾", description="", color=0xffd1dc)
            embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1354104616307916863/1359347708762259546/20250323_154558.png?ex=67f726b5&is=67f5d535&hm=d7affefdf238fdbf5301d68e2c3e1339e2313473771c9dd60d8014ee0a7a46cd&")
            embedVar.add_field(name=f"❌ A quantidade precisa ser maior que 0.", value=f"", inline=False)
            await ctx.send(embed=embedVar)
            return

        if item['Quantidade'] < quantidade:
            embedVar = discord.Embed(title="OPS!! 👾", description="", color=0xffd1dc)
            embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1354104616307916863/1359347708762259546/20250323_154558.png?ex=67f726b5&is=67f5d535&hm=d7affefdf238fdbf5301d68e2c3e1339e2313473771c9dd60d8014ee0a7a46cd&")
            embedVar.add_field(name=f"❌ Não temos essa quantidade em estoque.", value=f"", inline=False)
            await ctx.send(embed=embedVar)
            return

        if saldo < preco_total:
            embedVar = discord.Embed(title="OPS!! 👾", description="", color=0xffd1dc)
            embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1354104616307916863/1359347708762259546/20250323_154558.png?ex=67f726b5&is=67f5d535&hm=d7affefdf238fdbf5301d68e2c3e1339e2313473771c9dd60d8014ee0a7a46cd&")
            embedVar.add_field(name=f"❌ Você não tem moedas suficientes!", value=f"", inline=False)
            await ctx.send(embed=embedVar)
            return

    # Atualiza os dados
        user_saldo[usuario_id] -= preco_total  # Deduz o saldo
        item['Quantidade'] -= quantidade  # Reduz o estoque

    # Adiciona ao inventário do usuário
        if usuario_id not in inventario:
            inventario[usuario_id] = {
                "Nome": nome_item,
                "Quantidade": quantidade
         }
        if nome_item in inventario[usuario_id]:
            inventario[usuario_id][nome_item] += quantidade
        else:
            inventario[usuario_id][nome_item] = quantidade

    # Salvar os dados atualizados
        salvar_dados(user_saldo)  # Salvar saldo atualizado
        salvar_loja(dados_loja)  # Atualizar a loja
        salvar_itens(inventario)  # Atualizar inventário do usuário

        embedVar = discord.Embed(title="Compra realizada 🛒", description="", color=0xffd1dc)
        embedVar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&")
        embedVar.add_field(name=f"✅ Você comprou {quantidade}x {nome_item} por {preco_total} moedas!", value=f"", inline=False)
        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(Comprar(bot))