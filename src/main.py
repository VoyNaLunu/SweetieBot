import os
from dotenv import load_dotenv
from bot import bot
from commands import commands
from philomena import ImageBoard
import json
from log import logger


class SweetieBot(bot.Bot):
    pass

def main():
    discord_logger = logger.getLogger('discord')
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    bot = SweetieBot()
    bot.add_cog(commands.UtilCommands(bot))
    bot.add_cog(commands.DerpibooruCommands(bot))
    bot.run(DISCORD_TOKEN)
if __name__ == "__main__":
    main()