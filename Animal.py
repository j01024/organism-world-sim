from abc import ABC, abstractmethod
import random
from Organism import Organism

class Animal(Organism):
    @abstractmethod
    def draw(self):
        pass

    def getFreeSpot(self, fields, fieldNumber, sizeX, sizeY):
        if fieldNumber % sizeX < sizeX - 1 and fields[fieldNumber + 1].isEmpty():
            return fieldNumber + 1
        if fieldNumber % sizeX > 0 and fields[fieldNumber - 1].isEmpty():
            return fieldNumber - 1
        if fieldNumber >= sizeX and fields[fieldNumber - sizeX].isEmpty():
            return fieldNumber - sizeX
        if fieldNumber < (sizeX * sizeY) - sizeX and fields[fieldNumber + sizeX].isEmpty():
            return fieldNumber + sizeX
        return -1

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
        attackerStrength = fields[attackerPreviousField].getOrganism().getStrength()
        thisOrganismStrength = fields[fieldNumber].getOrganism().getStrength()
        if(attackerStrength >= thisOrganismStrength):
            fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
            fields[attackerPreviousField].setValue(None)
        else:
            fields[attackerPreviousField].setValue(None)
