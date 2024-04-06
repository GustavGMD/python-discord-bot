import os
from dotenv import load_dotenv

# Constants
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

BOT_DATA_PATH = 'data/bot/'
ACCOUNTS_DATA_PATH = 'data/accounts/'
TEMPLATES_DATA_PATH = 'data/templates/'

# Bot config
BOT_CONFIG_FILE = 'bot-config.json'
INITIALIZED_FIELD = 'initialized'
GUILD_ID_FIELD = 'guild_id'
CHANNEL_ID_FIELD = 'channel_id'

# Encounters
ENCOUNTERS_FILE = BOT_DATA_PATH + 'encounters.json'