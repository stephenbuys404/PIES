#flask
#flask_httpauth
#flask_restful
from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

#http://localhost:5000/hello_world
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
USER_DATA = {
    'admin':'mypassword',
    'user':'myuser'
}

@auth.verify_password
def verify(username, password):
    if(not username)and(not password):
        return False
    return USER_DATA.get(username)==password

class HelloWorld(Resource):
    @auth.login_required
    def get(self):
        return { 'Hello':'World' }

api.add_resource(HelloWorld,'/hello_world')
app.run(debug=True)
