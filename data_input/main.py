import json

class DataInput:
    def __init__(self, config):
        self.config = config

    def poll_for_articles(self):
        while True:
            # TODO: call queue_article
            sleep(config["data_input"]["poll_interval"])

    def queue_article(self, article):
        # TODO: Queue article in SQS

if __name__ = "main":
    trader = Trader(json.load(open("../config.json")))
