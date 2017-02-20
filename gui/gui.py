import tkinter as tk

from gui.page import MainPage, StatsPage


class Gui(tk.Tk):

    def __init__(self, bot):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "PredictIt Bot")

        self.bot = bot;

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu = tk.Menu(container)
        viewmenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="Control", command=lambda: self.show_frame(MainPage))
        viewmenu.add_command(label="Stats", command=lambda: self.show_frame(StatsPage))
        tk.Tk.config(self, menu=menu)

        self.frames = {}

        for frameType in (MainPage, StatsPage):
            frame = frameType(container, self)
            self.frames[frameType] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def start(self):
        self.bot.start()

    def stop(self):
        self.bot.stop()

    def print_trade(self, str):
        self.frames[MainPage].print_trade(str)

    def print(self, str):
        self.frames[MainPage].print(str)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
