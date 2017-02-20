from multiprocessing import Process, Queue
import json

from gui.gui import Gui
from data_analysis.data_analysis import DataAnalysis
from data_input.data_input import DataInput
from trader.trader import Trader


# Main process
class Bot:

    # Process variables
    scraper_processes = []
    analysis_processes = []
    trader_process = None

    # Queues to be delegated to sub-processes
    article_queue = Queue()
    result_queue = Queue()

    # Initializes all of the processes
    def __init__(self, config):
        self.config = config

        for num in range(config["data_input"]["num_workers"]):
            self.scraper_processes.append(
                Process(target=DataInput(self, self.config).run)
            )
        for num in range(config["data_analysis"]["num_workers"]):
            self.analysis_processes.append(
                Process(target=DataAnalysis(self, self.config).run, args=(self.article_queue,))
            )
        self.trader_process = Process(target=Trader(self, self.config).run, args=(self.result_queue,))

        self.gui = Gui(self)
        self.gui.geometry("1080x720")
        self.gui.mainloop()

    def put_article(self, article):
        self.article_queue.put(article)
        self.gui.print('Got article')

    def put_result(self, result):
        self.result_queue.put(result)
        self.gui.print(result)

    # Starts the processes
    def start(self):
        self.gui.print('Starting bot...')
        for process in self.scraper_processes:
            process.start()
        for process in self.analysis_processes:
            process.start()
        self.trader_process.start()

    # Shuts down the program
    def stop(self):
        for process in self.scraper_processes:
            process.terminate()
        for process in self.analysis_processes:
            process.terminate()
        self.trader_process.terminate()
        exit()

if __name__ == "__main__":
    bot = Bot(json.load(open("../config.json")))

