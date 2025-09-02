from dataclasses import fields
from Animal import Animal
import random

class Fox(Animal):
    def __init__(self, s = 3, a = 0):
        self.__age = a
        self._strength = s
        self._initiative = 7

    def draw(self):
        return "F"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        r = random.choice([0, 1, 2, 3])
        newPosition = -1
        if r == 0:
            if fieldNumber % sizeX < sizeX - 1:
                newPosition = fieldNumber + 1
            elif fieldNumber % sizeX == sizeX - 1:
                newPosition = fieldNumber - 1
        elif r == 1:
            if fieldNumber % sizeX > 0:
                newPosition = fieldNumber - 1
            elif fieldNumber % sizeX == 0:
                newPosition = fieldNumber + 1
        elif r == 2:
            if fieldNumber >= sizeX:
                newPosition = fieldNumber - sizeX
            else:
                newPosition = fieldNumber + sizeX
        elif r == 3:
            if fieldNumber < (sizeX * sizeY) - sizeX:
                newPosition = fieldNumber + sizeX
            else:
                newPosition = fieldNumber - sizeX
        
        if newPosition != -1:
            if(fields[newPosition].isEmpty()):
                fields[newPosition].setValue(fields[fieldNumber].getOrganism())
                fields[fieldNumber].setValue(None)
            elif not fields[newPosition].isEmpty() and fields[fieldNumber].getOrganism().draw() == fields[newPosition].getOrganism().draw():
                freeField = self.getFreeSpot(fields, newPosition, sizeX, sizeY)
                if freeField != -1:
                    fields[newPosition].setValue(fields[fieldNumber].getOrganism())
                    fields[freeField].setValue(fields[fieldNumber].getOrganism())
            else:
                otherOrganismStrength = fields[newPosition].getOrganism().getStrength()
                if otherOrganismStrength < self._strength:
                    fields[newPosition].getOrganism().collision(fields, sizeX, sizeY, newPosition, fieldNumber)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        super().collision(fields, sizeX, sizeY, fieldNumber, attackerPreviousField)