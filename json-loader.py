# Python program to read a JSON file

import json

# Opening a JSON file
file = open('data.json')

# Returns JSON object as a dictionary
data = json.load(file)

# Iterating through the JSON list
for i in data['data_list']:
    print(i['object_name'])

# Closing file
file.close()