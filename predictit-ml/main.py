from multiprocessing import Process, Queue
from data_analysis import data_analysis
from data_input import data_input
from trader import trader

# Basic queue for the queue process
class DataQueue:

    trade_port = 12345      # The port for trade process TODO: Change this to a config specified port
    article_port_list = []  # The ports for scraping workers
    analysis_port_list = [] # The ports for analysis workers

    article_queue = Queue()
    score_queue = Queue()

    def __init__(self, config):
        self.config = config

    def queue_article(self, article):
        self.article_queue.put(article)

    def get_article(self):
        self.article_queue.get(True)    # Return the first article. Block until item available otherwise.

    def queue_score(self, score):
        self.score_queue.put(score)

    def get_score(self):
        self.score_queue.get(True)  # Return the first score. Block until score available otherwise.

    if __name__ == "main":
        # p = Process()
        pass