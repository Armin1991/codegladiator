from flask import Flask
from flask_restful import Api
from handlerClass import List
from handlerClass import HelloWorld
from logger import Logger
# import FMJ
app = Flask(__name__)

app.config['DEBUG'] = True
api = Api(app)
api.add_resource(List, '/codegladiator/api/list')
api.add_resource(HelloWorld, '/codegladiator/api/hello')

if __name__ == '__main__':
    log = Logger()
    log.message("Starting the application")
    app.run(debug=True, host='0.0.0.0')
