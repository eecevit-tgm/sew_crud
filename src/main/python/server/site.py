"""

.. module:: site
   :synopsis: Restful User-Service outgoing point
.. moduleauthor:: Ecevit Emre Okan <github.com/eecevit-tgm>


"""

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from main.python.server import jreader, encoder

app = Flask(__name__)
api = Api(app)
data = jreader

USERS = data.reader()

def abort_if_user_doesnt_exist(usernmane):
    """
    Check if user exists
    :param usernmane: username
    :return: User doesn't exist error in JSONs
    """
    if usernmane not in USERS:
        abort(404, message="User {} doesn't exist".format(usernmane))

parser = reqparse.RequestParser()
parser.add_argument('user')



class User(Resource):

    def get(self, username):
        """
        **Get information of a specific user**

        This function allows user to get a specific user's information through their username.
        :param username: id of the teacher
        :return: user's information accessed by user in json and http status code
        - Example::
            curl http://127.0.0.1:5000/user/eecevit
        - Expected Success Response::
             {
             "id": "1",
             "username": "eecevit",
             "email": "eecevit@student.tgm.ac.at"
             "picture":"..."
             }
        - Expected Fail Response::
            HTTP Status Code: 404

        """
        abort_if_user_doesnt_exist(username)
        return USERS[username]

    def delete(self, username):
        """
        **Delete User Record**

        This function allows user to delete a user record.

        :param username: name of the user
        :return: delete status in json and http status code

        - Example::
            curl http://127.0.0.1:5000/user/eecevit -X DELETE -v

        - Expected Success Response::
            HTTP Status Code: 204

        - Expected Fail Response::
            HTTP Status Code: 404

        """
        abort_if_user_doesnt_exist(username)
        del USERS[username]
        data.delete(username)
        return '', 204

    def put(self, username):
        """
         **Update Information of a Specific User Record**
        This function allows user to update a specific users's information through their username.
        :param username: name of the user
        :return: users's information updated
        - Example::
            curl http://127.0.0.1:5000/user/eecevit -d "name=newName,mail@mail.com, eecevit.jpg" -X PUT -v
        - Expected Success Response::
            HTTP Status Code: 201
            {
                "username": "newName",
                "email": "mail@mail.com",
                "picture": "....."
            }
        - Expected Fail Response::
            HTTP Status Code: 404
        """
        args = parser.parse_args()
        name = args['user'].split(",")
        user = {'username': name[0],'email':name[1]}
        USERS[username] = user
        return user, 201


# Userlist
# shows a list of all users, and lets you POST to add new user
class UserList(Resource):
    def get(self):
        """
         **Get List of Users**
            This function allows users to get a list of users and their id, username, email and image.
            :return: user's information in json and http status code
            - Example::
                  curl http://localhost:5000/users -X GET -v
            - Expected Success Response::
                HTTP Status Code: 200
                {
                    "eecevit": {"id": "1", "username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "...."},
                    "danho": {"id": "2", "username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "...."},
                    "dsunaric": {"id": "3", "username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "...."},
                    "elshal": {"id": "4", "username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "...."}
                }
        """
        return USERS

    def post(self):
        """
        **Create User Record**

        This function allows user to create(post) a user record.

        :return: user's information added by the user in json
        - Example::
            curl http://localhost:5000/user -d "name=newUser,newUser@mail.at,eecevit.jpg" -X POST -v
        - Expected Success Response::
            HTTP Status Code: 201
            {
                "username": "newUser",
                "email": "newUser@mail.at",
                "picture": "....."
            }
        - Expected Fail Response::
            HTTP Status Code: 400
        """
        args = parser.parse_args()
        id = len(USERS)+1
        name = args['user'].split(",")
        image = str(encoder.encode(name[2]))
        USERS[name[0]] = {'id':id,'username': name[0], 'email':name[1],'picture':image}
        data.writer(USERS)
        return USERS[name[0]], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<usernmane>')


if __name__ == '__main__':
    app.run(debug=True)