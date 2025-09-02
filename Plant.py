from abc import ABC, abstractmethod
import random
from Organism import Organism

class Plant(Organism):
    @abstractmethod
    def draw(self):
        pass

    def action(self, sizeX, sizeY, fieldNumber, fields):
        a = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        if a == 5:
            r = random.choice([0, 1, 2, 3])
            if r == 0:
                if fieldNumber % sizeX < sizeX - 1 and fields[fieldNumber + 1].isEmpty():
                    fields[fieldNumber + 1].setValue(fields[fieldNumber].getOrganism())
            elif r == 1:
                if fieldNumber % sizeX > 0 and fields[fieldNumber - 1].isEmpty():
                    fields[fieldNumber - 1].setValue(fields[fieldNumber].getOrganism())
            elif r == 2:
                if fieldNumber >= sizeX and fields[fieldNumber - sizeX].isEmpty():
                    fields[fieldNumber - sizeX].setValue(fields[fieldNumber].getOrganism())
            elif r == 3:
                if fieldNumber < (sizeX * sizeY) - sizeX and fields[fieldNumber + sizeX].isEmpty():
                    fields[fieldNumber + sizeX].setValue(fields[fieldNumber].getOrganism())

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
        fields[attackerPreviousField].setValue(None)
