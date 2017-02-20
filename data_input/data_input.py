from data_input import news_api

import time
import arrow


class DataInput:

    def __init__(self, controller, config):
        self.controller = controller
        self.config = config

        self.sources = []
        for source in config["data_input"]["sources"]:
            self.sources.append({
                "news_api_name": source,
                "news_api_instance": news_api.NewsApi(
                    config["data_input"]["news_api"]["api_key"], source
                ),
                "last_time_checked": None
            })

    # Continuously polls for new articles and adds them to the article queue
    def poll_for_articles(self):
        while True:
            for source in self.sources:
                # Pull any new articles from that source
                max_time = None

                articles = source["news_api_instance"].get_articles()
                if articles is not None:
                    for article in articles:
                        article_time = arrow.get(article["publishedAt"]).datetime

                        # Only handle articles created after max time checked
                        if source["last_time_checked"] is None or source["last_time_checked"] < article_time:
                            self.queue_article(article)

                            if max_time is None or max_time < article_time:
                                max_time = article_time

                # Update max_time, if set
                if max_time is not None:
                    # This will update it in the sources array,
                    # because it points to the same object.
                    source["last_time_checked"] = max_time

            # Sleep for interval time
            time.sleep(self.config["data_input"]["poll_interval"])

    # Adds the given article to the given queue
    def queue_article(self, article):
        self.controller.put_article(article)

    # Entry point for process
    def run(self):
        self.poll_for_articles()
