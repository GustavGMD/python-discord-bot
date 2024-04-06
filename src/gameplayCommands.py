import utilities as utils

class heroCommands:
    def __init__(self, bot):
        print("Initialize the new instance of herobot.")
        self.bot = bot

        @self.bot.command(name='heroes', help='List currently available heroes')
        async def hero(context):
            print("command called: hero")
            await context.message.channel.send(utils.stringToCodeBlock(
                f'Command not implemented: !heroes'
            ))  

        @self.bot.command(name='heroinfo', help='Gives detailed information about the specific hero')
        async def hero(context):
            print("command called: heroinfo")
            await context.message.channel.send(utils.stringToCodeBlock(
                f'Command not implemented: !heroinfo'
            ))