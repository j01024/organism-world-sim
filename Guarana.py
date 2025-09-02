from Plant import Plant

class Guarana(Plant):
    def draw(self):
        return "U"

    def action(self, sizeX, sizeY, fieldNumber, fields):
        super().action(sizeX, sizeY, fieldNumber, fields)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
        fields[fieldNumber].getOrganism().addStrength(3)
        fields[attackerPreviousField].setValue(None)