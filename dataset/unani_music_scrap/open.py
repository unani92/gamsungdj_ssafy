from pprint import pprint
import json

with open('moviedata.json') as json_file:
    songs = json.load(json_file)

pprint(songs)