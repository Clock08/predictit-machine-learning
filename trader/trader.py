import time
from trader.web_interface import WebInterface


class Trader:

    def __init__(self, result_queue, message_queue, config):
        self.result_queue = result_queue
        self.message_queue = message_queue
        self.config = config
        self.web_interface = WebInterface(config["trader"]["user"], config["trader"]["pass"])

    # Make a trade based on the result
    def handle_result(self, result):
        # TODO: call make_trade based on result
        #self.web_interface.make_trade(contract, YES/NO, quantity, maxprice)
        pass

    # Entry point for process
    def run(self):
        while True:
            try:
                result = self.result_queue.get(True, 1)     # Continuously gets results from the queue
                self.handle_result(result)             # Makes trades based on the result
            except Exception:
                pass
