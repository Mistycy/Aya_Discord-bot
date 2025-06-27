import discord 
from discord.ext import commands
import random 
import json

GIVEWAY_FILE = "Giveway.json"


def carregar_giveway():
    try:
        with open(GIVEWAY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def salvar_giveway(giveway):
    with open(GIVEWAY_FILE, "w") as f:
        json.dump(giveway, f, indent=4)

class giveway(discord.ui.View):
    def _init__(self):
        super.__init__(timeout=None)
    @discord.ui.button(label="Participar", style=discord.ButtonStyle.blurple, emoji="🎉")
    async def botao_giveway(self, interaction: discord.Interaction, button: discord.ui.Button):
        carregar_giveway = carregar_giveway()
        salvar_giveway = salvar_giveway()
        membro = str(interaction.user.id)

        if membro not in carregar_giveway():
            carregar_giveway[membro] = {"id": membro}
            salvar_giveway(membro)
            await interaction.response.send_message("você entrou no sorteio")
        else:
            await interaction.response.send_message("você ja esta no sorteio")

class comando_giveway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def giveway(self, ctx):
        await ctx.send("sorteio", view=giveway())

async def setup(bot):
    await bot.add_cog(comando_giveway(bot))
        