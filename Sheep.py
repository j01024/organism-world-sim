from Animal import Animal

class Sheep(Animal):
    def __init__(self, s = 4, a = 0):
        self.__age = a
        self._strength = s
        self._initiative = 4

    def draw(self):
        return "S"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        super().action(sizeX, sizeY, fieldNumber, fields)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        super().collision(fields, sizeX, sizeY, fieldNumber, attackerPreviousField)