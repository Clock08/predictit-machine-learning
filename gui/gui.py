import tkinter as tk

from gui import page


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
        viewmenu.add_command(label="Control")
        viewmenu.add_command(label="Stats")
        menu.add_cascade(label="View", menu=viewmenu)

        tk.Tk.config(self, menu=menu)

        self.frames = {}

        for frameType in (page.MainPage, page.StatsPage):
            frame = frameType(container, self)
            self.frames[frameType] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(page.MainPage)

    def start(self):
        self.bot.start()

    def stop(self):
        self.bot.stop()

    def print(self, str):
        self.frames[page.MainPage].print(str)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
