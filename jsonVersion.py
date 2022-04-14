import json

file_path = "D:\MagicEdenFloorTracker\collections.json"
 
# Opening JSON file
f = open(file_path, 'r')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['Collections']:
    print(i)
    print(i['Amount'])

 
# Closing file
f.close()