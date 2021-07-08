# About
---

DiscordDefs is a small project made to facilitate development of Discord.py projects.

This project requires Discord.py to be installed, and will install it if it is not present on the system.

# Usage
---
- Use the command `pip3 install DiscordDefs` to install the package.
- Make sure the line `import DiscordDefs` is somewhere at the top of your file.
- Call functions like any other function in Python! 

# Dev Note
Thank you for using this package! Please credit it in your bot's `help` command or elsewhere so others can use this package!

# Modules

### botInfo() (from DiscordDefs import botInfo)
- Prints useful information about your system and the bot to the console.

### setIntent(intentName, Value) (from DiscordDefs import setIntent)
- `Value` must be `True` or `False`. Anything else will return an error.
- `intentName` has to be one of the intents listed [here](https://discord.com/developers/docs/topics/gateway#gateway-intents).

### sendMessage(url, content) (from DiscordDefs import sendMessage)
- `url` has to be a valid Discord webhook URL
- `content` has to be a valid string of text, or a variable that corresponds to one.