import time


class Trader:

    def __init__(self, result_queue, message_queue, config):
        self.result_queue = result_queue
        self.message_queue = message_queue
        self.config = config

    # Make a trade based on the result
    def handle_result(self, result):
        # TODO: call queue_result
        pass

    # Entry point for process
    def run(self):
        while True:
            try:
                result = self.result_queue.get(True, 1)     # Continuously gets results from the queue
                self.handle_result(result)             # Makes trades based on the result
            except Exception:
                pass
