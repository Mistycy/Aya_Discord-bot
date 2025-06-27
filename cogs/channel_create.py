import discord
from discord.ext import commands

class channel_create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)

    async def create(self, ctx):
        guild = ctx.guild
        await guild.create_text_channel("oi")


async def setup(bot):
    await bot.add_cog(channel_create(bot))

