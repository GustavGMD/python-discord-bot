# modules
import discord
import json

# our files
import constants as constants
import utilities as utils
import gameplayCommands as gameplay
import dataAccessWrapper as dataAccess

from discord.ext import commands

# Initialize Bot object
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

dataAccessObject = dataAccess.dataAccessWrapper()

#region Basic bot callbacks
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'error':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
#endregion

#region Bot initialization
@bot.command(name='init', help='Initializes bot to post in this channel')
async def init(context):
    # TODO1: Get channel and guild name, or maybe IDs?
    channelId = context.message.channel.id
    guildId = context.guild.id

    configJson = dataAccessObject.getConfigJson()

    if not configJson[constants.INITIALIZED_FIELD]:
        configJson[constants.GUILD_ID_FIELD] = guildId
        configJson[constants.CHANNEL_ID_FIELD] = channelId 
        configJson[constants.INITIALIZED_FIELD] = True

        dataAccessObject.setConfigJson(configJson)
        await context.message.channel.send(utils.stringToCodeBlock(
            f'Initialization complete at:'
            f'\nGuild: [{context.guild.name}]'
            f'\nChannel: [{context.message.channel.name}]'
        )) 
    else:
        await context.message.channel.send(utils.stringToCodeBlock(
            f'I\'m already initialized!'
            f'\nGuild: [{configJson[constants.GUILD_ID_FIELD]}]'
            f'\nChannel: [{configJson[constants.CHANNEL_ID_FIELD]}]'
        ))     

    print("command called: Init")

@bot.command(name='state', help='Returns whether the bot has been initialized or not')
async def state(context):
    # Read the bot configuration file
    # Return feedback message saying what is the current state
    print("command called: State")
#endregion

hero = gameplay.heroCommands(bot)

bot.run(constants.TOKEN)