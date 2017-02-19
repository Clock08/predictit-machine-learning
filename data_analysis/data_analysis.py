import time


class DataAnalysis:

    def __init__(self, config):
        self.config = config

    # Processes the given article and stores the results in the queue
    def handle_article(self, article, result_queue):
        # TODO: call queue_result
        # queue_result(score, result_queue)
        pass

    # Stores the result in the result queue
    def queue_result(self, result, result_queue):
        result_queue.put(result)

    # Entry point for process
    def run(self, article_queue, score_queue):
        while True:
            article = article_queue.get()
            self.handle_article(article, score_queue)
            time.sleep(self.config["data_analysis"]["poll_interval"])
