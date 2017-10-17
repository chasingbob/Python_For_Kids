# Example showing how to work with JSON files in Python


import json

with open('json_data.json') as json_data:
    d = json.load(json_data)
    print(d)