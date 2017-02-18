from news_api import NewsApi
import json
import time
import arrow

class DataInput:
    def __init__(self, config):
        self.config = config

        self.sources = []
        for source in config["data_input"]["sources"]:
            self.sources.append({
                "news_api_name": source["news_api_name"],
                "news_api_instance": NewsApi(config["data_input"]["news_api"]["api_key"], source["news_api_name"]),
                "last_time_checked": None
            })

    def pollForArticles(self):
        while True:
            for source in self.sources:
                # Pull any new articles from that source
                maxTime = None
                for article in source["news_api_instance"].getArticles():
                    articleTime = arrow.get(article["publishedAt"]).datetime

                    # Only handle articles created after max time checked
                    if source["last_time_checked"] is None or source["last_time_checked"] < articleTime:
                        self.queueArticle(article)

                        if maxTime is None or maxTime < articleTime:
                            maxTime = articleTime

                # Update max_time, if set
                if maxTime is not None:
                    # This will update it in the sources array,
                    # because it points to the same object.
                    source["last_time_checked"] = maxTime

            # Sleep for interval time
            time.sleep(config["data_input"]["poll_interval"])

    def queueArticle(self, article):
        # TODO: Queue article in SQS
        print(article)

if __name__ == "main":
    config = json.load(open("../config.json"))
    DataInput(config).pollForArticles()
