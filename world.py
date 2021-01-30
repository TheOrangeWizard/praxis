# praxis world.py
import random


location_types = ["town",
                  "village",
                  "ruins",
                  "lair"]


class World:
    def __init__(self):
        self.name = ""
        self.player = None
        self.locations = {}
        self.characters = {}
        self.locationCount = 0
        self.characterCount = 0

    def generate_locations(self, size):
        for i in range(size):
            location = Location()
            location_id = self.locationCount
            self.locationCount += 1
            location.type = random.choice(location_types)
            self.locations[location_id] = location


class Location:
    def __init__(self):
        self.type = None
        self.characters = {}
        self.items = {}



