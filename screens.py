# praxis screens.py


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from world import World
from character import Character


class MainScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text="praxis main menu title text")
        self.spacer = Label(text="")
        self.newgame = Button(text="new game", command=lambda: self.praxis.change_screen(NewGameScreen))
        self.savegame = Button(text="save game", command=lambda: self.praxis.change_screen(SaveGameScreen))
        self.resumegame = Button(text="resume game", command=lambda: self.praxis.change_screen(GameScreen))
        self.loadgame = Button(text="load game", command=lambda: self.praxis.change_screen(LoadGameScreen))
        self.options = Button(text="options", command=lambda: self.praxis.change_screen(OptionsScreen))
        self.exit = Button(text="exit", command=lambda: self.praxis.master.destroy())

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.spacer.pack(side="top", pady=50)
        self.newgame.pack(side="top")
        if self.praxis.world is not None:
            self.savegame.pack(side="top")
            self.resumegame.pack(side="top")
        self.loadgame.pack(side="top")
        self.options.pack(side="top")
        self.exit.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.spacer.destroy()
        self.newgame.destroy()
        self.resumegame.destroy()
        self.savegame.destroy()
        self.loadgame.destroy()
        self.options.destroy()
        self.exit.destroy()


class NewGameScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text="praxis new game menu title text")
        self.back = Button(text="back to main menu", command=lambda: self.praxis.change_screen(MainScreen))
        self.begin = Button(text="begin game", command=lambda: self.begin_new_game())

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

    def begin_new_game(self):
        worldname = self.worldNameEntry.get()
        playername = self.charNameEntry.get()
        if len(worldname) > 0 and len(playername) > 0:
            self.praxis.world = World()
            self.praxis.world.player = Character()
            self.praxis.world.name = worldname
            self.praxis.world.player.name = playername
            self.praxis.world.generate_locations(int(self.worldSizeEntry.get()))
            self.praxis.change_screen(GameScreen)
        else:
            messagebox.showerror("begin new ga,e", "character and world names cannot be empty")


class SaveGameScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text="save game not yet implemented")
        self.back = Button(text="back to main menu", command=lambda: self.praxis.change_screen(MainScreen))

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.back.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.back.destroy()


class LoadGameScreen:
    def __init__(self, praxis):
        self.praxis = praxis
        self.title = Label(text="load game not yet implwejntomn")
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

        self.locationsFrame = Labelframe(relief=SUNKEN, text="locations")
        self.locationsDisplay = Listbox(master=self.locationsFrame)
        self.locationIndex = 0
        for location in self.praxis.world.locations:
            self.locationsDisplay.insert(self.locationIndex, location.type)
            self.locationIndex += 1
        self.locationsDisplay.bind("<<ListboxSelect>>", self.update_character_display)

        self.charactersFrame = Labelframe(relief=SUNKEN, text="characters")
        self.charactersDisplay = Listbox(master=self.charactersFrame)

    def update_character_display(self, event):
        selection = event.widget.curselection()
        if selection:
            self.charactersDisplay.delete(0, END)
            characters_index = 0
            index = selection[0]
            for character in self.praxis.world.locations[index].characters:
                self.charactersDisplay.insert(characters_index, self.praxis.world.characters[character].name)
                characters_index += 1

    def draw(self):
        self.title.pack(side="top")
        self.menu.pack(side="bottom")

        self.locationsFrame.pack(side="left", padx=5)
        self.locationsDisplay.pack(side="left")

        self.charactersFrame.pack(side="left", padx=5)
        self.charactersDisplay.pack(side="left")

    def clear(self):
        self.title.destroy()
        self.menu.destroy()
        self.locationsFrame.destroy()
        self.charactersFrame.destroy()
