from Animal import Animal

class Wolf(Animal):
    def __init__(self, s = 9, a = 0):
        self.__age = a
        self._strength = s
        self._initiative = 5

    def draw(self):
        return "W"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        super().action(sizeX, sizeY, fieldNumber, fields)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        super().collision(fields, sizeX, sizeY, fieldNumber, attackerPreviousField)