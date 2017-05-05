from flask import Flask
from flask_restful import Api
from handlerClass import List

# import FMJ


app = Flask(__name__)



app.config['DEBUG'] = True
api = Api(app)
api.add_resource(List,'/codegladiator/api/list')
# api.add_resource(KeyTerms,'/termextractor/api/keyTerms')
# api.add_resource(Scores,'/termextractor/api/scores')
# api.add_resource(Phrases,'/termextractor/api/phrases')
#api.add_resource(FMJ,'/termextractor/api/fmj')


app.run(debug=True,host='127.0.0.1')

if __name__ == '__main__':
    app.run(debug=True)