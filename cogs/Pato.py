import discord 
from discord.ext import commands

class pato(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def pato(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/1254297425573838919/1372429980210036747/image.png?ex=6826be85&is=68256d05&hm=e7a0feacc88a5cc54985069051cfd0692f667fcb000eee29e6aec1ee4f800b2f&")

async def setup(bot):
    await bot.add_cog(pato(bot))