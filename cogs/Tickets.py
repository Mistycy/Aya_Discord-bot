import discord 
from discord.ext import commands


class class_tickets(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Abrir ticket", style=discord.ButtonStyle.blurple, emoji="📩")
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        

        user = interaction.user
        role = discord.utils.get(interaction.guild.roles, name="┃Mod Chat - aya")

        embedvar = discord.Embed(title="Ticket", description=f"{user.mention}, ticket criado com sucesso.", color=0xffd1dc)
        embedvar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg?ex=67fc8df6&is=67fb3c76&hm=f8138b24706459de1be132ddc69254b2867b7391e465b98844ed9e75bacd4541&")
        embedvar.add_field(name=f"Sistema", value=f"aguarde até que um {role.mention} responda o ticket.")        
        embedvar.add_field(name="Finalizar", value="digite !encerrar para encerrar o ticket.")
        
        guild = interaction.guild
        member = interaction.user
        name = '💢┃Support da Aya╺'
        category = discord.utils.get(interaction.guild.categories, name=name)
        Ticket_ativo = discord.utils.get(guild.channels, name=f"ticket-{member.name}")
        if Ticket_ativo is not None:
            await interaction.response.send_message("você ja possui um ticket ativo.", ephemeral=True)
            return



        else:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),  # Deny @everyone
                member: discord.PermissionOverwrite(view_channel=True, send_messages=True),  # Allow the member
                    }
            ticket_channel = await guild.create_text_channel(
                name=f"ticket-{member.name}",
                overwrites=overwrites,
                category=category
                )
            await interaction.response.send_message("Ticket criado com sucesso!!", ephemeral=True,
                                                    )
            await ticket_channel.send(embed=embedvar)         
            await interaction.response.send_message("ticket já existe!!", ephemeral=True)


class command_tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command() 
    async def Ticket(self, ctx):
        embedvar = discord.Embed(title="Ticket", description="Clique no botão abaixo para abrir um novo ticket!", color=0xffd1dc)
        embedvar.set_author(name="Aya", icon_url="https://cdn.discordapp.com/attachments/1359275472457957379/1360832965663526932/58e6c4633391436f464a5193da651966.jpg")
        embedvar.add_field(name="", value="caso tenho alguma duvida ou algum problema nao exite em abrir um novo ticket :3 💜💜")
        await ctx.send(view=class_tickets(), embed=embedvar)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def encerrar(self, ctx):
        category = discord.utils.get(ctx.guild.categories, name="💢┃Support da Aya╺")
    
        if not category:
            await ctx.send("Category **'💢┃Support da Aya╺'** not found!")
            return
    
        if ctx.channel.category and ctx.channel.category.id == category.id:
            await ctx.channel.delete()
        else:
            e = discord.Embed(title="erro", description="este comando funciona somente com tickets", color=0xffd1dc)
            await ctx.send(embed=e)

async def setup(bot):
    await bot.add_cog(command_tickets(bot))
