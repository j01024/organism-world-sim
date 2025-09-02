from Plant import Plant

class SosnowskyHogweed(Plant):
    def draw(self):
        return "Y"

    def __humanUsesSpecialAbility(self, fields, fieldNumber, sizeX, sizeY):
        if not fields[fieldNumber].isEmpty() and fields[fieldNumber].getOrganism().draw() == "H":
            if fields[fieldNumber].getOrganism().usesSpecialAbility():
                return False
            else:
                return True
        else:
            return True

    def action(self, sizeX, sizeY, fieldNumber, fields):
        if fieldNumber % sizeX < sizeX - 1 and self.__humanUsesSpecialAbility(fields, fieldNumber + 1, sizeX, sizeY):
            fields[fieldNumber + 1].setValue(None)
        if fieldNumber % sizeX > 0 and self.__humanUsesSpecialAbility(fields, fieldNumber - 1, sizeX, sizeY):
            fields[fieldNumber - 1].setValue(None)
        if fieldNumber >= sizeX and self.__humanUsesSpecialAbility(fields, fieldNumber - sizeX, sizeX, sizeY):
            fields[fieldNumber - sizeX].setValue(None)
        if fieldNumber < (sizeX * sizeY) - sizeX and self.__humanUsesSpecialAbility(fields, fieldNumber + sizeX, sizeX, sizeY):
            fields[fieldNumber + sizeX].setValue(None)

    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        fields[attackerPreviousField].setValue(None)
