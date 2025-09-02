from Animal import Animal
import random

class Antelope(Animal):
    def __init__(self, s = 4, a = 0):
        self.__age = a
        self._strength = s
        self._initiative = 4

    def draw(self):
        return "A"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        r = random.choice([0, 1, 2, 3])
        newPosition = -1
        if r == 0:
            if fieldNumber % sizeX < sizeX - 2:
                newPosition = fieldNumber + 2
            elif fieldNumber % sizeX == sizeX - 2:
                newPosition = fieldNumber - 2
        elif r == 1:
            if fieldNumber % sizeX > 1:
                newPosition = fieldNumber - 2
            elif fieldNumber % sizeX == 0:
                newPosition = fieldNumber + 2
        elif r == 2:
            if fieldNumber >= (2 * sizeX):
                newPosition = fieldNumber - (2 * sizeX)
            elif fieldNumber >= 0 and fieldNumber < sizeX:
                newPosition = fieldNumber + (2 * sizeX)
        elif r == 3:
            if fieldNumber < (sizeX * sizeY) - (2 * sizeX):
                newPosition = fieldNumber + (2 * sizeX)
            else:
                newPosition = fieldNumber - (2 * sizeX)

        if newPosition != -1:
            if fields[newPosition].isEmpty():
                fields[newPosition].setValue(fields[fieldNumber].getOrganism())
                fields[fieldNumber].setValue(None)
            elif not fields[newPosition].isEmpty() and fields[fieldNumber].getOrganism().draw() == fields[newPosition].getOrganism().draw():
                freeField = self.getFreeSpot(fields, fieldNumber, sizeX, sizeY)
                if(freeField != -1):
                    fields[newPosition].setValue(fields[fieldNumber].getOrganism())
                    fields[freeField].setValue(fields[fieldNumber].getOrganism())
            else:
                fields[newPosition].getOrganism().collision(fields, sizeX, sizeY, newPosition, fieldNumber)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        escape = random.choice([0, 1])
        findNewField = self.getFreeSpot(fields, fieldNumber, sizeX, sizeY)
        if escape == 0 or findNewField == -1:
            attackerStrength = fields[attackerPreviousField].getOrganism().getStrength()
            thisOrganismStrength = fields[fieldNumber].getOrganism().getStrength()
            if attackerStrength >= thisOrganismStrength:
                fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
                fields[attackerPreviousField].setValue(None)
            else:
                fields[attackerPreviousField].setValue(None)
        else:
            fields[findNewField].setValue(fields[fieldNumber].getOrganism())
            fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
            fields[attackerPreviousField].setValue(None)