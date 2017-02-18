import json

class Trader:
    def __init__(self, config):
        self.config = config

    def poll_for_messages(self):
        while True:
            sleep(config["trader"]["poll_interval"])

    def handle_message(self, message):
        # TODO: call queue_result

    def queue_result(self, message):
        # TODO: queue in SQS

if __name__ = "main":
    trader = Trader(json.load(open("../config.json")))
