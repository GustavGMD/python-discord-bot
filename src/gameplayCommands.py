class heroCommands:
    def __init__(self, bot):
        print("Initialize the new instance of herobot.")
        self.bot = bot
        #define all class methods here?

        # this works!
        @self.bot.command(name='hero', help='Testing using decorators inside a class')
        async def hero(context):
            # Just print something to debug in discord
            print("command called: hero")