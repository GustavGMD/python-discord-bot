import json
import constants as constants
import utilities as utils

# Class designed to be an interface to accessing data in the project
# Initially it reads local JSON files
# But eventually we want it to communicate with remote APIs

class dataAccessWrapper:
    
    @staticmethod
    def getConfigJson():
        # Save the data to a file as JSON  
        config = utils.readJSONFile(constants.BOT_DATA_PATH + constants.BOT_CONFIG_FILE)
        if not config:
            config = dict()
            config[constants.INITIALIZED_FIELD] = False   

        return config 
    
    @staticmethod
    def setConfigJson(configDictionary):
        dataAccessWrapper.writeJsonToFile(configDictionary, constants.BOT_DATA_PATH + constants.BOT_CONFIG_FILE)

    @staticmethod
    def writeJsonToFile(jsonDictionary, path):
        file = open(path, 'w')
        file.seek(0)
        json.dump(jsonDictionary, file, indent = 6) 
        file.close() 