# rsg 0.0.1
# world.py


class World:
    def __init__(self):
        self.name = ""
        self.player = None
        self.regions = {}
        self.characters = {}


class Region:
    def __init__(self):
        self.locations = {}


class Location:
    def __init__(self):
        self.characters = {}
        self.items = {}
