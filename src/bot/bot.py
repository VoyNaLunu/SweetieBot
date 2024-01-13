import discord
from log import logger

class Bot(discord.Bot):
    async def on_ready(self):
        logger.info(f'{self.user} is online')