from Plant import Plant

class Belladonna(Plant):
    def draw(self):
        return "B"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        super().action(sizeX, sizeY, fieldNumber, fields)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        fields[fieldNumber].setValue(None)
        fields[attackerPreviousField].setValue(None)