import utilities as utils
import constants as constants
import dataAccessWrapper as dataAccess

class initCommmands:
    def __init__(self, bot):
        self.bot = bot    
        dataAccessObject = dataAccess.dataAccessWrapper()
    
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

            configJson = dataAccessObject.getConfigJson()
            result = ""
            if configJson[constants.INITIALIZED_FIELD]:
                result = utils.stringToCodeBlock(
                    f'I\'m already initialized!'
                    f'\nGuild: [{configJson[constants.GUILD_ID_FIELD]}]'
                    f'\nChannel: [{configJson[constants.CHANNEL_ID_FIELD]}]'
                )
            else:
                result = utils.stringToCodeBlock(f'I\'m not already initialized!'
                )

            print("command called: State")

class callbacks:
    def __init__(self, bot):
        self.bot = bot    
        
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