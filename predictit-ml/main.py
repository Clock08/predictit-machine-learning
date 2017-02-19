from multiprocessing import Process, Queue
import json
import tkinter

from gui import gui
from data_analysis import data_analysis
from data_input import data_input
from trader import trader


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
                Process(target=data_input.DataInput(self.config).run, args=self.article_queue)
            )
        for num in range(config["data_analysis"]["num_workers"]):
            self.analysis_processes.append(
                Process(target=data_analysis.DataAnalysis(self.config).run,
                        args=(self.article_queue, self.result_queue))
            )
        self.trader_process = Process(target=trader.Trader(self.config).run, args=self.result_queue)

    # Starts the processes
    def start(self):
        for process in self.scraper_processes:
            process.start()
        for process in self.analysis_processes:
            process.start()
        self.trader_process.start()

    # Shuts down the program
    def shutdown(self):
        for process in self.scraper_processes:
            process.join()
        for process in self.analysis_processes:
            process.join()
        self.trader_process.join()
        exit()

if __name__ == "__main__":
    bot = None#Bot(json.load(open("../config.json")))

    g = gui.Gui(bot)
    g.geometry("1280x720")
    g.mainloop()

