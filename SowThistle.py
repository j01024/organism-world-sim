from Plant import Plant
import random

class SowThistle(Plant):
    def draw(self):
        return "O"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        for i in range(3):
            a = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            if a == 5:
                r = random.choice([0, 1, 2, 3])
                if r == 0:
                    if fieldNumber % sizeX < sizeX - 1 and fields[fieldNumber + 1].isEmpty():
                        fields[fieldNumber + 1].setValue(SowThistle())
                elif r == 1:
                    if fieldNumber % sizeX > 0 and fields[fieldNumber - 1].isEmpty():
                        fields[fieldNumber - 1].setValue(SowThistle())
                elif r == 2:
                    if fieldNumber >= sizeX and fields[fieldNumber - sizeX].isEmpty():
                        fields[fieldNumber - sizeX].setValue(SowThistle())
                elif r == 3:
                    if fieldNumber < (sizeX * sizeY) - sizeX and fields[fieldNumber + sizeX].isEmpty():
                        fields[fieldNumber + sizeX].setValue(SowThistle())
                break

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        super().collision(fields, sizeX, sizeY, fieldNumber, attackerPreviousField)