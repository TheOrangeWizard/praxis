# praxis main.py


from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from screens import *
from world import *
from character import *

version = "0.0.1"


class Praxis(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.world = None
        self.master = master
        self.screen = MainScreen(self)
        self.screen.draw()

    def change_screen(self, new_screen):
        self.screen.clear()
        self.screen = new_screen(self)
        self.screen.draw()

    def begin_new_game(self):
        worldname = self.screen.worldNameEntry.get()
        playername = self.screen.charNameEntry.get()
        if len(worldname) > 0 and len(playername) > 0:
            self.world = World()
            self.world.player = Character()
            self.world.name = worldname
            self.world.player.name = playername
            self.change_screen(GameScreen)
        else:
            tkinter.messagebox.showerror("begin new ga,e", "character and world names cannot be empty")


root = Tk()
praxis = Praxis(master=root)
praxis.master.title("praxis " + version)
praxis.master.minsize(640, 480)
praxis.mainloop()
