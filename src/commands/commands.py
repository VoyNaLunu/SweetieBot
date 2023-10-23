import os
import discord
import yaml
import discord
from discord.ext import commands

WORKDIR = os.getcwd()

def load_commands() -> dict:
    """returns dictionary of commands and their descriptions"""
    with open(f'{WORKDIR}/src/commands/commands.yaml', encoding="UTF-8") as data:
        return yaml.load(data, Loader=yaml.loader.SafeLoader)

COMMAND_LIST = load_commands()

class UtilCommands(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @commands.slash_command(description=COMMAND_LIST['help']['description'])
    async def help(self, ctx):
        """returns list of commands"""
        embed = discord.Embed(
            title="Hello I am SweetieBot, here are my commands:",
            color=discord.Colour.purple()
        )
        for command in COMMAND_LIST.keys():
            embed.add_field(name=COMMAND_LIST[command]["name"], value=COMMAND_LIST[command]["description"], inline=False)
        await ctx.respond(embed=embed, ephemeral=True)