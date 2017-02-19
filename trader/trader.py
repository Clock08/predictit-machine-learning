import time


class Trader:

    def __init__(self, config):
        self.config = config

    # Make a trade based on the result
    def handle_result(self, result):
        # TODO: call queue_result
        pass

    # Entry point for process
    def run(self, result_queue):
        while True:
            result = result_queue.get(True)     # Continuously gets results from the queue
            self.handle_result(result)          # Makes trades based on the result
