# modules
import discord
import json

# our files
import constants as constants
import utilities as utils
import gameplayCommands as gameplayCommands
import systemCommands as systemCommands

from discord.ext import commands

# Initialize Bot object
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize all commands and callbacks
callbacks = systemCommands.callbacks(bot)
initCommands = systemCommands.initCommmands(bot)
heroCommands = gameplayCommands.heroCommands(bot)

# Run bot
bot.run(constants.TOKEN)