import json
from pprint import pprint

users = ''

'''
Lieset die Daten aus dem JSON File heraus
'''
with open('user.json', 'r') as f:
     users = json.load(f)

'''
Gib die Daten aus dem File zurueck
'''
def reader():
    return users

'''
Loescht einen User mit einem spezifischen namen raus
'''
def deleate(name):
    if name in users:
        users.pop(name)
    writer()

'''
Erstellt einen User mit einem Namen einer Id und einer emailadresse
'''
def create(name, id, email):
    users.update({name:{'id':id,'username':name,'email':email}})
    writer()

def writer(user):
    users = user
    with open('user.json', 'w') as f:
        f.write(json.dumps(users))
