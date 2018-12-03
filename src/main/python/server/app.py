from flask import Flask, jsonify,request
from flask_cors import CORS
from main.python.server import jreader

data = jreader


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

User = data.reader()


# sanity check route
@app.route('/user', methods=['GET', 'POST'])
def all_users():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        User.append({
            'username': post_data.get('username'),
            'email': post_data.get('email'),
            'picture': post_data.get('picture')
        })
        response_object['message'] = 'User added!'
    else:
        response_object['user'] = User
    return  (response_object)




if __name__ == '__main__':
    app.run()
