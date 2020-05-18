# rsg 0.0.1
# menus.py

from tkinter import *
from tkinter.ttk import *


class MainScreen:
    def __init__(self, rsg):
        self.rsg = rsg
        self.title = Label(text="rsg main menu title text")
        self.spacer = Label(text="")
        self.newgame = Button(text="new game", command=lambda: self.rsg.change_screen(NewGameScreen))
        self.loadgame = Button(text="load game", command=lambda: self.rsg.change_screen(LoadGameScreen))
        self.options = Button(text="options", command=lambda: self.rsg.change_screen(OptionsScreen))
        self.exit = Button(text="exit", command=lambda: self.rsg.master.destroy())

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.spacer.pack(side="top", pady=50)
        self.newgame.pack(side="top")
        self.loadgame.pack(side="top")
        self.options.pack(side="top")
        self.exit.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.spacer.destroy()
        self.newgame.destroy()
        self.loadgame.destroy()
        self.options.destroy()
        self.exit.destroy()


class NewGameScreen:
    def __init__(self, rsg):
        self.rsg = rsg
        self.title = Label(text="rsg new game menu title text")
        self.back = Button(text="back to main menu", command=lambda: self.rsg.change_screen(MainScreen))
        self.leftFrame = Frame(relief=SUNKEN)
        self.rightFrame = Frame(relief=SUNKEN)
        self.leftHeader = Label(text="new character options", master=self.leftFrame)
        self.rightHeader = Label(text="new world options", master=self.rightFrame)
        self.charNameLabel = Label(text="character name", master=self.leftFrame)
        self.worldNameLabel = Label(text="world name", master=self.rightFrame)
        self.charNameEntry = Entry(master=self.leftFrame)
        self.worldNameEntry = Entry(master=self.rightFrame)


    def draw(self):
        self.title.pack(side="top", pady=5)
        self.back.pack(side="bottom")
        self.leftFrame.pack(side="left", expand=1, fill=BOTH)
        self.rightFrame.pack(side="right", expand=1, fill=BOTH)
        # self.leftHeader.grid(row=1, column=1, columnspan=2, pady=5)
        # self.rightHeader.grid(row=1, column=1, columnspan=2, pady=5)
        # self.charNameLabel.grid(row=2, column=1, padx=5)
        # self.worldNameLabel.grid(row=2, column=1, padx=5)
        # self.charNameEntry.grid(row=2, column=2)
        # self.worldNameEntry.grid(row=2, column=2)
        self.leftHeader.pack(side="top", pady=5)
        self.rightHeader.pack(side="top", pady=5)
        self.charNameLabel.pack(side="left", anchor="n", padx=5)
        self.worldNameLabel.pack(side="left", anchor="n", padx=5)
        self.charNameEntry.pack(side="right", anchor="n", padx=5)
        self.worldNameEntry.pack(side="right", anchor="n", padx=5)

    def clear(self):
        self.title.destroy()
        self.back.destroy()
        self.leftFrame.destroy()
        self.rightFrame.destroy()


class LoadGameScreen:
    def __init__(self, rsg):
        self.rsg = rsg
        self.title = Label(text="rsg load game menu title text")
        self.back = Button(text="back to main menu", command=lambda: self.rsg.change_screen(MainScreen))

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.back.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.back.destroy()


class OptionsScreen:
    def __init__(self, rsg):
        self.rsg = rsg
        self.title = Label(text="rsg options menu title text")
        self.back = Button(text="back to main menu", command=lambda: self.rsg.change_screen(MainScreen))

    def draw(self):
        self.title.pack(side="top", pady=5)
        self.back.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.back.destroy()


class GameScreen:
    def __init__(self, rsg):
        self.rsg = rsg
        self.title = Label(text="rsg")
        self.menu = Button(text="menu", command=lambda: self.rsg.change_screen(MainScreen))

    def draw(self):
        self.title.pack(side="top")
        self.menu.pack(side="bottom")

    def clear(self):
        self.title.destroy()
        self.menu.destroy()