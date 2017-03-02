from multiprocessing import Process, Queue
import json
import tkinter as tk

from gui.page import MainPage, StatsPage
from data_analysis.data_analysis import DataAnalysis
from data_input.data_input import DataInput
from trader.trader import Trader


# Main process
class Bot:

    # Process variables
    scraper_process = None
    analysis_processes = []
    trader_process = None

    # Queues to be delegated to sub-processes
    message_queue = Queue()
    article_queue = Queue()
    result_queue = Queue()

    running = False

    # Initializes all of the processes
    def __init__(self, config):
        self.config = config

        self.scraper_process = Process(target=DataInput(self.article_queue, self.message_queue, self.config).run)
        for num in range(config["data_analysis"]["num_workers"]):
            self.analysis_processes.append(
                Process(target=DataAnalysis(self.article_queue, self.result_queue, self.message_queue, self.config).run)
            )
        self.trader_process = Process(target=Trader(self.result_queue, self.message_queue, self.config).run)

        self.gui = tk.Tk()
        self.gui.geometry("1080x720")

        tk.Tk.wm_title(self.gui, "PredictIt Bot")

        container = tk.Frame(self.gui)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu = tk.Menu(container)
        viewmenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="Control", command=lambda: self.show_frame(MainPage))
        viewmenu.add_command(label="Stats", command=lambda: self.show_frame(StatsPage))
        tk.Tk.config(self.gui, menu=menu)

        self.frames = {}

        for frameType in (MainPage, StatsPage):
            frame = frameType(container, self)
            self.frames[frameType] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

        self.gui.after(10, self.poll_messages)

        while True:
            try:
                self.gui.mainloop()
            except UnicodeDecodeError:
                pass

    def poll_messages(self):
        try:
            msg = self.message_queue.get(False)
            if msg is not None:
                self.print(msg)
                self.gui.after(100, self.poll_messages)
            else:
                self.gui.after(100, self.poll_messages)
        except Exception:
            pass
        self.gui.after(100, self.poll_messages)

    # Starts the processes
    def start(self):
        self.running = True
        self.print('Starting bot...')
        self.scraper_process.start()
        for process in self.analysis_processes:
            process.start()
        self.trader_process.start()

    # Shuts down the program
    def stop(self):
        self.running = False
        self.scraper_process.terminate()
        for process in self.analysis_processes:
            process.terminate()
        self.trader_process.terminate()
        exit()

    def print_trade(self, str):
        self.frames[MainPage].print_trade(str)

    def print(self, str):
        self.frames[MainPage].print(str)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    bot = Bot(json.load(open("../config.json")))

