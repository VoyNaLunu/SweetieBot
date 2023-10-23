import discord

class Bot(discord.Bot):
    async def on_ready(self):
        print(f'{self.user} is online')