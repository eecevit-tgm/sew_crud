from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from main.python.server import jreader, encoder

app = Flask(__name__)
api = Api(app)
data = jreader

USERS = data.reader()

def abort_if_user_doesnt_exist(usernmane):
    if usernmane not in USERS:
        abort(404, message="User {} doesn't exist".format(usernmane))

parser = reqparse.RequestParser()
parser.add_argument('user')



# Users
# shows a single user item and lets you delete a user item
class User(Resource):
    def get(self, usernmane):
        abort_if_user_doesnt_exist(usernmane)
        return USERS[usernmane]

    def delete(self, usernmane):
        abort_if_user_doesnt_exist(usernmane)
        del USERS[usernmane]
        data.deleate(usernmane)
        return '', 204

    def put(self, username):
        args = parser.parse_args()
        name = args['user'].split(",")
        user = {'username': name[0],'email':name[1]}
        USERS[username] = user
        return user, 201


# Userlist
# shows a list of all users, and lets you POST to add new user
class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        id = len(USERS)+1
        name = args['user'].split(",")
        image = encoder.encode(name[2])
        print(image.toString)
        USERS[name[0]] = {'id':id,'username': name[0], 'email':name[1]}
        data.writer(USERS)
        return USERS[name[0]], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<usernmane>')


if __name__ == '__main__':
    app.run(debug=True)