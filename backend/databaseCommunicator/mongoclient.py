import flask
import pymongo



class Mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="172.29.9.8",port=27017)
        self.database = self.client.codeGladiator
        self.collection = self.database.testdata

    def insert(self,json):
        id = self.collection.insert_one(json)
        return id
    def listAll(self):
        cursor = self.collection.find()
        return cursor
# data = pandas.read_excel("/home/subhasishp/Documents/codegladiator.xlsx")
# rows = len(data.index)
#
# for row in range(rows):
#     dict = {}
#     for d in data:
#         dict[d] = data[d][row]
#
#     id = mongo.insert(dict)
#     print id

