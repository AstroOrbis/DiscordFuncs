
from setuptools import setup, find_packages

def long_description():
    with open("README.md", "r") as fhandle:
        return fhandle.read()

setup(
    name="DiscordFuncs", 
    version="1.0.0", 
    author="Astro Orbis",
    author_email="astroorbis@gmail.com", 
    
    description="Some small discord.py functions for bot developers!", 
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/AstroOrbis/DiscordFuncs", 
    packages=find_packages(), 
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent",], # Enter meta data into the classifiers list!
    python_requires='>=3.6',
    keywords=['python3', 'discord', 'discord bot', 'discord webhook'],
    install_requires=[
      'discord',
      'requests',
      'aiohttp',
      'discord_webhook'
    ]
)