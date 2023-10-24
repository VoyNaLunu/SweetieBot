import os
from dotenv import load_dotenv
from bot import bot
from commands import commands
import derpibooru
import json

class SweetieBot(bot.Bot):
    pass

def main():
    print(json.dumps(derpibooru.GetImages().by_tags(['human']), indent=4))
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    bot = SweetieBot()
    bot.add_cog(commands.UtilCommands(bot))
    bot.run(DISCORD_TOKEN)
if __name__ == "__main__":
    main()