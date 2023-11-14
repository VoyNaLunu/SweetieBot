# SweetieBot

## Usage
1. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```
3. Create .env with your discord bot token
```bash
cp .env.example .env
```
3. Start the bot
```bash
python3 ./src/main.py
```

## Commands
Currently bot has only these commands(and is very limited and buggy):
- /help - shows list of available commands
- /derpibooru <tags> - gets a random image with specified tags, example: /derpibooru tags:pony, cute

Image:  
  
![showcase](https://github.com/VoyNaLunu/SweetieBot/assets/93346826/7c047052-d452-4b5e-97d2-678d85432ff2)

Video (since discord doesn't allow to add videos to embeds it has to be a little uglier and rely on discord doing the embedding which doesn't always work):  
  
![изображение](https://github.com/VoyNaLunu/SweetieBot/assets/93346826/7285a57a-e305-46e8-981a-676d39837af6)

