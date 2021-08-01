# About
---

DiscordFuncs is a small project made to facilitate development of Discord.py projects.

This project requires Discord.py to be installed, and will install it if it is not present on the system.

# Usage
---
- Use the command `python3 -m pip install DiscordFuncs` in terminal to install the package. (In Windows, use `py -m pip install DiscordFuncs` instead.)
- Call functions like any other function in Python! 

# Dev Note
Thank you for using this package! Please credit it in your bot's `help` command or elsewhere so others can use this package!

# Modules

## Bot

### Bot.botInfo() (`from DiscordFuncs.Bot import *`)
- Prints useful information about your system and the bot to the console.

### Bot.setIntent(intentName, Value) (`from DiscordFuncs.Bot import *`)
- `Value` must be `True` or `False`. Anything else will return an error.
- `intentName` has to be one of the intents listed [here](https://discord.com/developers/docs/topics/gateway#gateway-intents).

# Webhook
### Webhook.sendMessage(url, content) (`from DiscordFuncs.Webhook import *`)
- `url` has to be a valid Discord webhook URL
- `content` has to be a valid string of text, or a variable that corresponds to one.