# praxis world.py


class World:
    def __init__(self):
        self.name = ""
        self.player = None
        self.locations = {}
        self.characters = {}


class Location:
    def __init__(self):
        self.characters = {}
        self.items = {}
