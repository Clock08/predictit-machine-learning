import json

class Trader:
    def __init__(self, config):
        self.config = config

    def poll_for_messages(self):
        while True:
            sleep(config["trader"]["poll_interval"])

    def handle_message(self, message):
        # TODO: call queue_result
        pass

    def queue_result(self, message):
        # TODO: queue in SQS
        pass

    def run(self, score_queue):
        while True:
            # TODO: Handle all trading functions
            pass