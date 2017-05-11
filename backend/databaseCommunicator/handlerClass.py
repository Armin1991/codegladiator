import flask

from mongoclient import Mongo
from flask_restful import Resource
class List(Resource):
    def get(self):
        mongo = Mongo()
        cursor = mongo.listAll()
        list =[{m:str(x[m]) for m in x}  for x in cursor]
        return flask.jsonify({"total records":len(list),"data":list})
class HelloWorld(Resource):
    def get(self):
        return flask.jsonify({"Success":"true","Message":"Hello World"})
