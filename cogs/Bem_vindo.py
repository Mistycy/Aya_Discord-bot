import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class WelcomeMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    load_dotenv()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = int(os.getenv("CHAT_BEM_VINDO"))
        canal = self.bot.get_channel(channel)
        if canal:
            embedVar = discord.Embed(
                title="Novo membro 🎉🎉", 
                description="", 
                color=0xffd1dc
            )
            embedVar.set_author(
                name="Aya", 
                icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&"
            )
            embedVar.add_field(
                name=f"A pessoinha {member.name} entrou no servidor", 
                value=f"SEJA BEM VINDO!!! {member.mention}", 
                inline=False
            )
            if member.avatar:
                embedVar.set_image(url=member.avatar.url)

            await canal.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(WelcomeMessage(bot))