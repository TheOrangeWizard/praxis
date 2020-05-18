# rsg 0.0.1
# main.py

from tkinter import *
from tkinter.ttk import *
from screens import *

version = "0.0.1"


class Rsg(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.screen = MainScreen(self)
        self.screen.draw()

    def change_screen(self, new_screen):
        self.screen.clear()
        self.screen = new_screen(self)
        self.screen.draw()


root = Tk()
rsg = Rsg(master=root)
rsg.master.title("RSG "+version)
rsg.master.minsize(640, 480)
rsg.mainloop()
