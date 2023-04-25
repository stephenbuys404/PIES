#flask
#flask_restful
from flask import Flask
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

film_dict = {
    '1':{'Name':'Avengers: Infinity War','Year':2002,'Month':'March'},
    '2':{'Name':'Ant Man and the Wasp','Year':2020,'Month':'August'},
    '3':{'Name':'The Boss Baby','Year':2018,'Month':'May'},
    '4':{'Name':'War','Year':2012,'Month':'June'},
    '5':{'Name':'Paw Patrol the movie','Year':2000,'Month':'March'},
    '6':{'Name':'The Snowman','Year':2024,'Month':'April'},
    '7':{'Name':'Friday the 13th','Year':2001,'Month':'November'},
    '8':{'Name':'Army of Thieves','Year':2008,'Month':'October'},
}

def abort_if_todo_doesnt_exist(film_id):
    if(film_id not in film_dict):
        abort(404,message= 'Film {} doesnt exist '.format(film_id))

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('year')
parser.add_argument('month')

class Films(Resource):
    def get(self,film_id):
        abort_if_todo_doesnt_exist(film_id)
        return film_dict[film_id]

    def delete(self,film_id):
        abort_if_todo_doesnt_exist(film_id)
        del film_dict[film_id]
        return '',204

    def put(self,film_id):
        args=parser.parse_args()
        task = {'Name': args['name'],
                'Year': args['year'],
                'Month': args['month']}
        film_dict[film_id] = task
        return task, 201

class FilmDict(Resource):
    def get(self):
        return film_dict

api.add_resource(FilmDict, '/films')
api.add_resource(Films, '/films/<film_id>')

if(__name__=='__main__'):
    app.run(debug=True)