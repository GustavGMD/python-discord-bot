# modules
import discord
import json

# our files
import constants as constants
import utilities as utils
import gameplayCommands as gameplay

from discord.ext import commands

# Initialize Bot object
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

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

    # TODO2: Save the data to a file as JSON  
    botConfig = utils.readJSONFile(constants.BOT_DATA_PATH + constants.BOT_CONFIG_FILE)
    if not botConfig:
        file = open(constants.BOT_DATA_PATH + constants.BOT_CONFIG_FILE, 'w')
        botConfig = dict()
        botConfig[constants.INITIALIZED_FIELD] = False    

    if not botConfig[constants.INITIALIZED_FIELD]:
        # Update the JSON dictionary
        botConfig[constants.GUILD_ID_FIELD] = guildId
        botConfig[constants.CHANNEL_ID_FIELD] = channelId 
        botConfig[constants.INITIALIZED_FIELD] = True
        # Move the file handler back to the start
        file.seek(0)
        # Write back to the file
        json.dump(botConfig, file, indent = 6)
        await context.message.channel.send(utils.stringToCodeBlock(
            f'Initialization complete at:'
            f'\nGuild: [{context.guild.name}]'
            f'\nChannel: [{context.message.channel.name}]'
        ))  
        # close the file
        file.close() 
    else:
        await context.message.channel.send(utils.stringToCodeBlock(
            f'I\'m already initialized!'
            f'\nGuild: [{botConfig[constants.GUILD_ID_FIELD]}]'
            f'\nChannel: [{botConfig[constants.CHANNEL_ID_FIELD]}]'
        ))       

    # TODO3: Return a feedback message stating that the bot has been initialized
    print("command called: Init")

@bot.command(name='state', help='Returns whether the bot has been initialized or not')
async def state(context):
    # Read the bot configuration file
    # Return feedback message saying what is the current state
    print("command called: State")
#endregion

hero = gameplay.heroCommands(bot)

bot.run(constants.TOKEN)