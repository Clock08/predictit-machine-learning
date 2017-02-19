import json
from multiprocessing import Process, Queue

import data_analysis
import data_input
import trader


# Basic queue for the queue process
class Bot:

    scraper_processes = []
    analysis_processes = []
    trader_process = None

    article_queue = Queue()
    score_queue = Queue()

    def __init__(self, config):
        self.config = config

        for num in range(0, config["data_input"]["num_workers"]):
            self.scraper_processes.append(
                Process(target=data_input.DataInput(self.config).run, args=self.article_queue)
            )
        for num in range(0, config["data_analysis"]["num_workers"]):
            self.analysis_processes.append(
                Process(target=data_analysis.DataAnalysis(self.config).run, args=(self.article_queue, self.score_queue))
            )

        self.trader_process = Process(target=trader.Trader(self.config).run, args=self.score_queue)

    def shutdown(self):
        for process in self.scraper_processes:
            process.join()
        for process in self.analysis_processes:
            process.join()
        self.trader_process.join()

if __name__ == "main":
    config = json.load(open("../config.json"))
    Bot(config)