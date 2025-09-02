from Plant import Plant

class Grass(Plant):
    def draw(self):
        return "G"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        super().action(sizeX, sizeY, fieldNumber, fields)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        super().collision(fields, sizeX, sizeY, fieldNumber, attackerPreviousField)