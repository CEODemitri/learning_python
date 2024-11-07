import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file) # reads file and converts to dictionary

file.close()

print(file_contents['friends'][0])

# add content to json file
cars = [
    {'make': 'Ferrari', 'model': '488'},
    {'make': 'Bentley', 'model': 'Echo1'}
]