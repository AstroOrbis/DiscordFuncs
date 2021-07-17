@ECHO OFF 

ECHO Installing packages...

pip3 install discord
pip3 install requests
pip3 install asyncio
pip3 install discord_webhook

ECHO Packages installed! Opening repo...
START https://github.com/AstroOrbis/DiscordFuncs

PAUSE