# bot.py
import discord
import json
import constants

from discord.ext import commands

# Initialize Bot object
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

def stringToCodeBlock(string :str):
    return f'```{string}```'

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
        file = open(constants.BOT_DATA_PATH + constants.BOT_CONFIG_FILE, 'r+')
        botConfig = json.load(file)        
    except:
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
        await context.message.channel.send(stringToCodeBlock(
            f'Initialization complete at:'
            f'\nGuild: [{context.guild.name}]'
            f'\nChannel: [{context.message.channel.name}]'
        ))   
    else:
        await context.message.channel.send(stringToCodeBlock(
            f'I\'m already initialized!'
            f'\nGuild: [{botConfig[constants.GUILD_ID_FIELD]}]'
            f'\nChannel: [{botConfig[constants.CHANNEL_ID_FIELD]}]'
        ))       

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
async def join(context):
    print("command called: Join")
    # todo1: Get the user name or ID
    userId = context.author.id

    # todo2:Check if account already exists
    try:
        file = open(constants.ACCOUNTS_DATA_PATH + f'account-{userId}.json', 'r', encoding='utf8')
        # If the file exists, there's already an account so we should just retur
        # a message to the channel
        messageString = f'You already have an account {context.author.display_name}'
        await context.message.channel.send(stringToCodeBlock(messageString))
        file.close()
        return
    except:
        # Load template account and fill with the new player's data
        # Save file
        file = open(constants.ACCOUNTS_DATA_PATH + f'account-{userId}.json', 'w', encoding='utf8')
        templateFile = open(constants.TEMPLATES_DATA_PATH + 'account-template.json', 'r', encoding='utf8')
        account = json.load(templateFile)
        account['userid'] = userId
        file.seek(0)
        json.dump(account, file, indent = 6)

        messageString = (
            f'New account created! {context.author.display_name} \n'
            f'reactions: '
        )
        for emoji in account['emojis']:
            # messageString += f'U+{ord(emoji):X}'
            messageString += f'{emoji} '        
        await context.message.channel.send(stringToCodeBlock(messageString))

        # Close the open files
        file.close()
        templateFile.close()
        
    # todo3: Save the data to a file, with the starting account data 
    # todo4: Return a feedback message stating that player has joined the game

@bot.command(name='account', help='Displays your account data')
async def account(context):
    print("command called: Account")
    # todo1: Check if account exists
    userId = context.author.id
    try:
        file = open(constants.ACCOUNTS_DATA_PATH + f'account-{userId}.json', 'r', encoding='utf8')        
    except:
        messageString = (
            f'You don\'t have an account yet {context.author.display_name}\n'
            f'Use the !join command to create one'
        )
        await context.message.channel.send(stringToCodeBlock(messageString))
        return

    # todo2: Return message to server with account content
    account = json.load(file)
    emojis = ' '.join([emoji for emoji in account['emojis']])
    messageString = (
        f'Here\'s your account info {context.author.display_name}:\n'
        f'Reactions: {emojis}'                         
    )
    await context.message.channel.send(stringToCodeBlock(messageString))
    file.close()    

@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    await channel.send(stringToCodeBlock(f'You reacted with {payload.emoji}'))
    # Check if the user is allowed to use this emoji
    # if it is, add it to the current activity count
    # else remove the reaction
    user = bot.get_user(payload.user_id)
    message = await channel.fetch_message(payload.message_id)
    await message.remove_reaction(payload.emoji, user)

bot.run(constants.TOKEN)

# def validate_bot_config():
#     try:
#         file = open(BOT_CONFIG_FILE, 'r+')
#         botConfig = json.load(file)
#         return botConfig[INITIALIZED_FIELD]
#     except:
#         return False
