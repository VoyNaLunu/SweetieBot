import os
from dotenv import load_dotenv
from bot import bot
from bot.commands import commands
from log import logger


class SweetieBot(bot.Bot):
    pass


def main():
    discord_logger = logger.getLogger('discord')
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    FILTER_ID = os.getenv('FILTER_ID')
    client_bot = SweetieBot(filter_id=FILTER_ID)
    client_bot.add_cog(commands.UtilCommands(client_bot))
    client_bot.add_cog(commands.DerpibooruCommands(client_bot))
    client_bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
