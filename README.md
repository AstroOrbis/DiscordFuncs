# About
---

DiscordFuncs is a small project made to facilitate development of Discord.py projects.

This project requires the latest version of Python3 to be installed.

# Usage
---
- Use `git clone https://www.github.com/AstroOrbis/DiscordFuncs` in the root of your project directory.

If you are on Linux/MacOS:
`cd DiscordFuncs/Setup && chmod a+x setup && ./setup`

If you are on Windows:
Navigate to the DiscordFuncs/Setup folder and double-click the `setup.bat` file.

(PyPi doesn't seem to work for me, so this will have to do for now!)

# Dev Note
Thank you for using this package! Please credit it in your bot's `help` command or elsewhere so others can use this package!

# Modules

### botInfo() (`from DiscordFuncs.Modules.Bot import botInfo`)
- Prints useful information about your system and the bot to the console.

### setIntent(intentName, Value) (`from DiscordFuncs.Modules.Bot import setIntent`)
- `Value` must be `True` or `False`. Anything else will return an error.
- `intentName` has to be one of the intents listed [here](https://discord.com/developers/docs/topics/gateway#gateway-intents).

### sendMessage(url, content) (`from DiscordFuncs.Modules.Webhook import sendMessage`)
- `url` has to be a valid Discord webhook URL
- `content` has to be a valid string of text, or a variable that corresponds to one.