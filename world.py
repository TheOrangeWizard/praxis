# praxis world.py
import random

from character import Character


location_types = ["town",
                  "village",
                  "ruins",
                  "lair"]

first_names = ["Allen",
               "Square",
               "Topher",
               "Ahme",
               "Amanda",
               "Orange",
               "Henry",
               "Dr"]

last_names = ["Y",
              "Blob",
              "3001",
              "64",
              "CC",
              "Wizard",
              "Draton",
              "Oracle"]


class World:
    def __init__(self):
        self.name = ""
        self.player = None
        self.locations = []
        self.characters = []

    def generate_locations(self, size):
        for i in range(size):
            location = Location()
            location.id = len(self.locations)
            location.type = random.choice(location_types)
            if location.type == "town":
                for j in range(4):
                    location.characters.append(self.generate_character(location.id))
            elif location.type == "village":
                for j in range(3):
                    location.characters.append(self.generate_character(location.id))
            elif location.type == "lair":
                for j in range(1):
                    location.characters.append(self.generate_character(location.id))

            self.locations.append(location)

    def generate_character(self, location):
        character = Character()
        character.name = "{} {}".format(random.choice(first_names), random.choice(last_names))
        character.location = location
        character.id = len(self.characters)
        self.characters.append(character)
        return character.id


class Location:
    def __init__(self):
        self.type = None
        self.id = None
        self.characters = []
        self.items = []



