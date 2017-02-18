from news_api import NewsApi
import json
import time

class DataInput:
    def __init__(self, config):
        self.config = config

        self.sources = {}
        for source in config["data_input"]["sources"]:
            self.sources["source"] = NewsApi(config["data_input"]["news_api"]["api_key"], source["news_api_name"])

    def pollForArticles(self):
        while True:
            for source in self.sources.values():
                for article in source.getArticles():
                    self.queueArticle(article)

            time.sleep(config["data_input"]["poll_interval"])

    def queueArticle(self, article):
        # TODO: Queue article in SQS
        print(article)
