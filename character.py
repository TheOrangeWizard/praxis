# praxis character.py


class Character:
    def __init__(self):
        self.name = "default"
        self.health = 100
        self.maxHealth = 100
        self.strength = 10
        self.agility = 10
        self.intellect = 10
        self.charisma = 10
        self.effects = []
        self.inventory = []
        self.equipment = {"head": None,
                          "hand": None,
                          "body": None,
                          "legs": None,
                          "feet": None}

    def update(self):
        pass
