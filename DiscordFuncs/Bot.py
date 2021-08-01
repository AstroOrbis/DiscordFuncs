import discord
from discord import bot
import platform
import os

class Bot:
  def botInfo():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

  def setIntent(intentName, Value):
    discord.Intents.intentName = Value
