import time


class Trader:

    def __init__(self, config):
        self.config = config

    # Make a trade based on the result
    def handle_result(self, result):
        # TODO: call queue_result
        pass

    def queue_result(self, message):
        # TODO: queue in SQS           --  What is it queueing exactly? It only needs to take from the queue
        pass

    # Entry point for process
    def run(self, result_queue):
        while True:
            result = result_queue.get()     # Continuously gets results from the queue
            self.handle_result(result)      # Makes trades based on the result
            time.sleep(self.config["trader"]["poll_interval"])  # Do we need to sleep, or shall we trade as soon as we have results?
