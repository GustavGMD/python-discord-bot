import json

def stringToCodeBlock(string :str):
    return f'```{string}```'

def readJSONFile(path):
    try:
        file = open(path, 'r+')
        botConfig = json.load(file)  
        file.close()   
        return botConfig   
    except:
        return False   