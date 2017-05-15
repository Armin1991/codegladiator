import logging
import datetime
from config import config as con


class Logger(object):

    def __init__(self):
        self.format = '%(asctime)-15s -INFO- %(message)s'
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

        logging.basicConfig(filename= con.log_dir+'/log-' + self.date + '-error.log', filemode='a', level=logging.DEBUG, format=self.format)
        self.logger = logging.getLogger(__name__)

    def message(self, string):
        self.logger.info(string)

    def error(self, error):
        self.logger.error(error)
