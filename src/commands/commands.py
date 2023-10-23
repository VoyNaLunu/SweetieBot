import os
import discord
import yaml
import discord
from discord.ext import commands

WORKDIR = os.getcwd()

class UtilCommands(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @commands.slash_command(description="shows all available commands")
    async def help(self, ctx):
        """returns list of commands"""
        embed = discord.Embed(
            title="Hello I am SweetieBot, here are my commands:",
            color=discord.Colour.purple()
        )
        with open(f'{WORKDIR}/src/commands/commands.yaml') as data:
            command_list = yaml.load(data, Loader=yaml.loader.SafeLoader)
        for command in command_list.keys():
            embed.add_field(name=command_list[command]["name"], value=command_list[command]["description"], inline=False)
        await ctx.respond(embed=embed, ephemeral=True)