import requests
from logger import Logger
from config import config as con

class Requests(object):

    def __init__(self):
        self.logger = Logger()
        self.request = None

    def getHostPort(self, serviceName):
        try:
            self.request = requests.get(con.consul_services)
        except Exception as error:
            self.logger.error(error)
        if self.request:
            services = self.request.json()
            self.logger.message("Searching for service %s" % serviceName)
            service = [x for x in services if serviceName in x]
            host = str(services[service[0]]['Address'])
            port = services[service[0]]['Port']
            self.logger.message("Returning (host, port) = (%s, %s)" % (host, port))
            return {'Host': host, 'Port': port}
        else:
            return None
