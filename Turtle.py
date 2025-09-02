from Animal import Animal
import random

class Turtle(Animal):
    def __init__(self, s = 2, a = 0):
        self.__age = 0
        self._strength = 2
        self._initiative = 1

    def draw(self):
        return "T"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        r = random.choice([0, 1, 2, 3])
        if r == 0:
            super().action(sizeX, sizeY, fieldNumber, fields)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        attackerStrength = fields[attackerPreviousField].getOrganism().getStrength()
        if attackerStrength > 5:
            fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
            fields[attackerPreviousField].setValue(None)