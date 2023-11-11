# bot.py
import os
import random
import discord
import json
from dotenv import load_dotenv

from discord.ext import commands

# Constants
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

BOT_CONFIG_FILE = 'bot-config.json'
INITIALIZED_FIELD = 'initialized'
GUILD_ID_FIELD = 'guild_id'
CHANNEL_ID_FIELD = 'channel_id'


# Initialize Bot object
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='init', help='Initializes bot to post in this channel')
async def init(context):
    # TODO1: Get channel and guild name, or maybe IDs?
    channelId = context.message.channel.id
    guildId = context.guild.id

    # TODO2: Save the data to a file as JSON  
    try:
        file = open(BOT_CONFIG_FILE, 'r+')
        botConfig = json.load(file)        
    except:
        file = open(BOT_CONFIG_FILE, 'w')
        botConfig = dict()
        botConfig[INITIALIZED_FIELD] = False    

    if not botConfig[INITIALIZED_FIELD]:
        # Update the JSON dictionary
        botConfig[GUILD_ID_FIELD] = guildId
        botConfig[CHANNEL_ID_FIELD] = channelId 
        botConfig[INITIALIZED_FIELD] = True
        # Move the file handler back to the start
        file.seek(0)
        # Write back to the file
        json.dump(botConfig, file, indent = 6)
        await context.message.channel.send(
            f'Initialization complete at:'
            f'\nGuild: [{context.guild.name}]'
            f'\nChannel: [{context.message.channel.name}]'
        )   
    else:
        await context.message.channel.send(
            f'I\'m already initialized!'
            f'\nGuild: [{context.guild.name}]'
            f'\nChannel: [{context.message.channel.name}]'
        )       

    # close the file
    file.close()

    # TODO3: Return a feedback message stating that the bot has been initialized
    print("command called: Init")

@bot.command(name='state', help='Returns whether the bot has been initialized or not')
async def state(context):
    # Read the bot configuration file
    # Return feedback message saying what is the current state
    print("command called: State")

@bot.command(name='join', help='Joins the game! The bot creates an account for the user')
async def init(context):
    # Save the user nmame or ID
    # Save the data to a file, with the starting account data 
    # Return a feedback message stating that player has joined the game
    print("command called: Join")

@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    await channel.send(f'You reacted with {payload.emoji}')
    # Check if the user is allowed to use this emoji
    # if it is, add it to the current activity count
    # else remove the reaction
    user = bot.get_user(payload.user_id)
    message = await channel.fetch_message(payload.message_id)
    await message.remove_reaction(payload.emoji, user)

# @bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
# async def nine_nine(context):
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         )
#     ]

#     response = random.choice(brooklyn_99_quotes)
#     await context.channel.send(response)

# @bot.command(name='roll_dice', help='Simulates rolling dice.')
# async def roll(context, number_of_dice : int, number_of_sides : int):
#     dice = [
#         str(random.choice(range(1, number_of_sides + 1)))
#         for _ in range(number_of_dice)
#     ]
#     await context.send(', '.join(dice))

bot.run(TOKEN)

# def validate_bot_config():
#     try:
#         file = open(BOT_CONFIG_FILE, 'r+')
#         botConfig = json.load(file)
#         return botConfig[INITIALIZED_FIELD]
#     except:
#         return False