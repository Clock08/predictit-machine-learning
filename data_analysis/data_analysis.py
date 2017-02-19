import time


class DataAnalysis:

    def __init__(self, config):
        self.config = config

    def handle_article(self, message, score_queue):
        # TODO: call queue_result
        # queue_result(score, score_queue)
        pass

    def queue_result(self, message, score_queue):
        score_queue.put(message)

    # Entry point for process
    def run(self, article_queue, score_queue):
        while True:
            article = article_queue.get()
            self.handle_article(article, score_queue)
            time.sleep(self.config["data_analysis"]["poll_interval"])
