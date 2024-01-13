import discord
from log import logger


class Bot(discord.Bot):
    def __init__(self, filter_id, *args, **options):
        super().__init__(*args, **options)

        self.filter_id = filter_id

    async def on_ready(self):
        logger.info(f'{self.user} is online')
