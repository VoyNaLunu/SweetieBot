import os
import re
import yaml
import discord
from discord.ext import commands
from philomena import ImageBoard


WORKDIR = os.getcwd()
IMG_REGEX = r"(.*)(\.png|.jpg|.jpeg|.gif)"
VIDEO_REGEX = r"(.*)(\.mp4|.webm)"


def load_commands() -> dict:
    """returns dictionary of commands and their descriptions"""
    with open(f'{WORKDIR}/src/bot/commands/commands.yaml', encoding="UTF-8") as data:
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


def embed_image(title, description, image_url, author, post_url) -> discord.Embed:
    embed = discord.Embed(
        title=title,
        color=discord.Colour.purple(),
    )
    embed.set_author(name=author)
    embed.add_field(name="Description:", value=description, inline=False)
    embed.add_field(name="Link to the post:", value=post_url, inline=False)
    embed.set_image(url=image_url)
    return embed


class DerpibooruCommands(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot
        self.board = ImageBoard("https://derpibooru.org")

    @commands.slash_command(description=COMMAND_LIST['derpibooru']['description'])
    async def derpibooru(self, ctx, tags):
        images = self.board.random_image(tags)
        embed = None
        message = "I couldn't find anything :("
        if "error_message" in images:
            message = "sorry something went wrong"
        else:
            image = images["images"][0]
        print(images)
        if re.match(IMG_REGEX, image["view_url"]):
            message = f"I found this using tags: {tags}"
            embed=embed_image("Derpibooru", images["images"][0]["description"], images["images"][0]["view_url"], images["images"][0]["uploader"], f'{self.board.base_url}/images/{images["images"][0]["id"]}/')
        await ctx.respond(message, embed=embed)
