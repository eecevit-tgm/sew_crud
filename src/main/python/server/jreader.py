import json
from pprint import pprint

with open('user.json') as f:
    user = json.load(f)

pprint(user)