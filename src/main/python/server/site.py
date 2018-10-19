from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

USERS = {
    'eecevit':{'id':1, 'username': 'eecevit', 'email':'eecevit@student.tgm.ac.at'}
}

def abort_if_user_doesnt_exist(usernmane):
    if usernmane not in USERS:
        abort(404, message="User {} doesn't exist".format(usernmane))

parser = reqparse.RequestParser()
parser.add_argument('user')


# Todo
# shows a single user item and lets you delete a user item
class User(Resource):
    def get(self, usernmane):
        abort_if_user_doesnt_exist(usernmane)
        return USERS[usernmane]

    def delete(self, usernmane):
        abort_if_user_doesnt_exist(usernmane)
        del USERS[usernmane]
        return '', 204

    def put(self, usernmane):
        args = parser.parse_args()
        usernmane = {'id':args['id'], 'username': args['username'], 'email':args['email']}
        USERS[usernmane] = usernmane
        return user, 201


# Userlist
# shows a list of all users, and lets you POST to add new user
class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        usernmane = int(max(USERS.keys()).lstrip('user')) + 1
        usernmane = 'user:%i' % usernmane
        USERS[usernmane] = {'task': args['task']}
        return USERS[usernmane], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(UserList, '/user')
api.add_resource(User, '/users/<usernmane>')


if __name__ == '__main__':
    app.run(debug=True)