import time


class DataAnalysis:

    def __init__(self, controller, config):
        self.controller = controller
        self.config = config

    # Processes the given article and stores the results in the queue
    def handle_article(self, article):
        # TODO: call queue_result
        # queue_result(score, result_queue)
        pass

    # Stores the result in the result queue
    def queue_result(self, result):
        self.controller.put_result(result)

    # Entry point for process
    def run(self, article_queue):
        while True:
            try:
                article = article_queue.get(True, 1)           # Gets articles from the queue and analyzes them
                self.handle_article(article)
            except Exception:
                pass

