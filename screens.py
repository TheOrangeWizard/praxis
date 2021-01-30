# praxis screens.py


from tkinter import *
from tkinter.ttk import *


class MainScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text="praxis main menu title text")
        self.spacer = Label(text="")
        self.newgame = Button(text="new game", command=lambda: self.praxis.change_screen(NewGameScreen))
        self.resumegame = Button(text="resume game", command=lambda: self.praxis.change_screen(GameScreen))
        self.loadgame = Button(text="load game", command=lambda: self.praxis.change_screen(LoadGameScreen))
        self.options = Button(text="options", command=lambda: self.praxis.change_screen(OptionsScreen))
        self.exit = Button(text="exit", command=lambda: self.praxis.master.destroy())

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.spacer.pack(side="top", pady=50)
        self.newgame.pack(side="top")
        if self.praxis.world is not None:
            self.resumegame.pack(side="top")
        self.loadgame.pack(side="top")
        self.options.pack(side="top")
        self.exit.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.spacer.destroy()
        self.newgame.destroy()
        self.resumegame.destroy()
        self.loadgame.destroy()
        self.options.destroy()
        self.exit.destroy()


class NewGameScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text="praxis new game menu title text")
        self.back = Button(text="back to main menu", command=lambda: self.praxis.change_screen(MainScreen))
        self.begin = Button(text="begin game", command=lambda: self.praxis.begin_new_game())

        self.leftFrame = Labelframe(relief=SUNKEN, text="new character options")
        self.rightFrame = Labelframe(relief=SUNKEN, text="new world options")

        self.charNameLabel = Label(text="character name", master=self.leftFrame)
        self.charNameEntry = Entry(master=self.leftFrame)

        self.worldNameLabel = Label(text="world name", master=self.rightFrame)
        self.worldNameEntry = Entry(master=self.rightFrame)

        self.worldSizeLabel = Label(text="world size", master=self.rightFrame)
        self.worldSizeEntry = Scale(master=self.rightFrame, from_=4, to=64)
        self.worldSizeEntry.set(16)

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.back.pack(side="bottom")
        self.begin.pack(side="bottom")

        self.leftFrame.pack(side="left", expand=1, fill=BOTH)

        self.charNameLabel.pack(side="top", padx=5)
        self.charNameEntry.pack(side="top", padx=5)

        self.rightFrame.pack(side="right", expand=1, fill=BOTH)

        self.worldNameLabel.pack(side="top", padx=5)
        self.worldNameEntry.pack(side="top", padx=5)

        self.worldSizeLabel.pack(side="top", padx=5)
        self.worldSizeEntry.pack(side="top", padx=5)

    def clear(self):
        self.title.destroy()
        self.back.destroy()
        self.begin.destroy()
        self.leftFrame.destroy()
        self.rightFrame.destroy()


class LoadGameScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text="praxis load game menu title text")
        self.back = Button(text="back to main menu", command=lambda: self.praxis.change_screen(MainScreen))

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.back.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.back.destroy()


class OptionsScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text="praxis options menu title text")
        self.back = Button(text="back to main menu", command=lambda: self.praxis.change_screen(MainScreen))

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.back.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.back.destroy()


class GameScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text=self.praxis.world.player.name)
        self.menu = Button(text="menu", command=lambda: self.praxis.change_screen(MainScreen))
        self.locationsDisplay = Listbox()
        self.locationIndex = 0
        for location in self.praxis.world.locations:
            self.locationsDisplay.insert(self.locationIndex, self.praxis.world.locations[location].type)
            self.locationIndex += 1
        self.characterDisplay = Listbox()

    def update_character_display(self, location):
        pass

    def draw(self):
        self.title.pack(side="top")
        self.menu.pack(side="bottom")
        self.locationsDisplay.pack(side="left")

    def clear(self):
        self.title.destroy()
        self.menu.destroy()
        self.locationsDisplay.destroy()