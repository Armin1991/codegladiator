import pymongo
from logger import Logger
from requests import Requests


class Mongo(object):

    def __init__(self):
        self.logger = Logger()
        self.request = Requests()
        self.hostPort = self.request.getHostPort("mongoDB")
        self.client = pymongo.MongoClient(host=self.hostPort['Host'], port=self.hostPort["Port"])
        self.database = self.client.codeGladiator
        self.collection = self.database.testdata

    def insert(self, json):
        id = self.collection.insert_one(json)
        return id

    def listAll(self):
        cursor = self.collection.find()
        return cursor
