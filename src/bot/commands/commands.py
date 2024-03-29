from datetime import datetime
from log import logger
import os
import re
import yaml
import discord
from discord.ext import commands
import philomena
from . import exceptions

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
            embed.add_field(
                name=COMMAND_LIST[command]["name"], value=COMMAND_LIST[command]["description"], inline=False)
        await ctx.respond(embed=embed, ephemeral=True)


def embed_image(
        title: str,
        image_url: str,
        post_url: str,
        description: str | None = None,
        author: str | None = None,
        author_avatar: str | None = None,
        image_upvotes: int = 0,
        image_downvotes: int = 0,
        image_faves: int = 0,
        created_at: str = "") -> discord.Embed:
    embed = discord.Embed(
        title=title,
        color=discord.Colour.purple(),
        timestamp=created_at
    )
    if author:
        icon_url = author_avatar if author_avatar else ""
        embed.set_author(name=author, icon_url=icon_url)
    if description:
        embed.add_field(name="Description:", value=description, inline=False)
    embed.add_field(name="Link to the post:", value=post_url, inline=False)
    embed.set_image(url=image_url)
    embed.set_footer(
        text=f'⬆️ {image_upvotes} ⬇️ {image_downvotes} ⭐ {image_faves}')
    return embed


class DerpibooruCommands(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot
        self.board = philomena.ImageBoard(
            "https://derpibooru.org", filter_id=self.bot.filter_id)

    @commands.slash_command(description=COMMAND_LIST['derpibooru']['description'])
    async def derpibooru(self, ctx, tags, filter_id=""):
        await ctx.defer()

        try:
            images = self.board.random_image(tags, filter_id=filter_id)
            embed = None
            image = None
            uploader_name = None
            uploader_avatar = None
            image_upvotes = None
            image_downvotes = None

            if not images:
                message = f"I couldn't find anything with tags: `{tags}` :("
                await ctx.followup.send(message)
                return
            if "error_message" in images:
                raise exceptions.ImageFetchFailed(
                    f"failed to fetch image, server response: {images}")
            image = images["images"][0]
            if image["uploader_id"]:
                uploader_id = image["uploader_id"]
                uploader_name = image["uploader"]
                uploader = self.board.profile(uploader_id)
                uploader_avatar = uploader["user"]["avatar_url"]
            message = f"I found this using tags: `{tags}`"
            title = "Derpibooru"
            description = image["description"]
            image_url = image["view_url"]
            post_url = f'{self.board.base_url}/images/{image["id"]}/'
            image_upvotes = image["upvotes"]
            image_downvotes = image["downvotes"]
            image_faves = image["faves"]
            image_created_at = datetime.strptime(
                image["created_at"], '%Y-%m-%dT%H:%M:%S%z')
            if re.match(IMG_REGEX, image_url):
                embed = embed_image(
                    title=title,
                    description=description,
                    image_url=image_url,
                    post_url=post_url,
                    author=uploader_name,
                    author_avatar=uploader_avatar,
                    image_upvotes=image_upvotes,
                    image_downvotes=image_downvotes,
                    image_faves=image_faves,
                    created_at=image_created_at,
                )
            if re.match(VIDEO_REGEX, image_url):
                uploader_name = f'** **\n**Uploaded by:**\n**{uploader_name}**\n** **'
                video_description = f'**Description:**\n{description}'
                if description:
                    # doing it this way so there's no extra padding
                    video_description = f'{video_description}\n** **'
                post_url = f'**Link to the post:**\n{post_url}\n** **'
                stats = f'⬆️ {image_upvotes} ⬇️ {image_downvotes} ⭐ {image_faves} **•** {image_created_at.strftime("%d/%m/%Y %H:%M")}\n** **'
                message = f'{message}\n{uploader_name}\n{video_description}\n{post_url}\n{stats}'
            await ctx.followup.send(message, embed=embed)
        except Exception as error:
            message = "sorry something went wrong"
            logger.log(
                logger.ERROR, f"following error occured in derpibooru command: {error}")
            await ctx.followup.send("sorry something went wrong")
