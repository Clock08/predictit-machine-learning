import json

class DataAnalsyis:
    def __init__(self, config):
        self.config = config

    def poll_for_messages(self):
        while True:
            # TODO: call handle_message
            sleep(config["data_analysis"]["poll_interval"])

    def handle_message(self, message):
        # TODO: call queue_result

    def queue_result(self, message):
        # TODO: queue in SQS

if __name__ = "main":
    trader = Trader(json.load(open("../config.json")))
