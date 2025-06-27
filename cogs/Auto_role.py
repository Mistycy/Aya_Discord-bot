import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_name = os.getenv("AUTO_ROLE")
        
        if not self.role_name:
            logger.warning("AUTO_ROLE environment variable not set - automatic role assignment disabled")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not self.role_name:
            return
            
        guild = member.guild
        role = discord.utils.get(guild.roles, name=self.role_name)

        if not role:
            logger.error(f"Auto-role '{self.role_name}' not found in server {guild.name}")
            return

        try:
            await member.add_roles(role)
            logger.info(f"Assigned role '{role.name}' to {member.name} in {guild.name}")
            
            # Optional: Send to a log channel
            # log_channel = guild.get_channel(YOUR_CHANNEL_ID)
            # if log_channel:
            #     await log_channel.send(f"Assigned {role.name} to {member.mention}")
                
        except discord.Forbidden:
            logger.error(f"Missing permissions to assign roles in {guild.name}")
        except discord.HTTPException as e:
            logger.error(f"Failed to assign role to {member.name}: {e}")

async def setup(bot):
    await bot.add_cog(AutoRole(bot))