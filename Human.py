from Animal import Animal

class Human(Animal):
    __usesSpecialAbility = False
    __turnsSinceAbility = 0

    def __init__(self, s = 5, a = 0, u = 0, t = 0):   #constructor
        x = False
        if x == 1:
            x = True
        self.__usesSpecialAbility = x
        self.__turnsSinceAbility = t
        self._strength = s
        self._initiative = 4

        #Getter methods

    def usesSpecialAbility(self):  
        return self.__usesSpecialAbility

    def turnsSinceAbility(self):
        return self.__turnsSinceAbility

    def draw(self):   # implementation of the abstract method 
        return "H"

    def action(self, sizeX, sizeY, fieldNumber, fields, dir):
        newPosition = -1
        if dir == "Right":
            if fieldNumber % sizeX < sizeX - 1:
                newPosition = fieldNumber + 1
            elif fieldNumber % sizeX == sizeX - 1:
                newPosition = fieldNumber - 1
        elif dir == "Left":
            if fieldNumber % sizeX > 0:
                newPosition = fieldNumber - 1
            elif fieldNumber % sizeX == 0:
                newPosition = fieldNumber + 1
        elif dir == "Up":
            if fieldNumber >= sizeX:
                newPosition = fieldNumber - sizeX
            else:
                newPosition = fieldNumber + sizeX
        elif dir == "Down":
            if fieldNumber < (sizeX * sizeY) - sizeX:
                newPosition = fieldNumber + sizeX
            else:
                newPosition = fieldNumber - sizeX
        elif dir == "Space":
            if not self.__usesSpecialAbility and self.__turnsSinceAbility >= 5:
                self.__usesSpecialAbility = True
                self.__turnsSinceAbility = 0
        
        if newPosition != -1:
            if fields[newPosition].isEmpty():
                fields[newPosition].setValue(fields[fieldNumber].getOrganism())
                fields[fieldNumber].setValue(None)
            else:
                if self.__usesSpecialAbility:
                    freeSpot = self.getFreeSpot(fields, fieldNumber, sizeX, sizeY)
                    if freeSpot != -1:
                        fields[freeSpot].setValue(fields[fieldNumber].getOrganism())
                        fields[fieldNumber].setValue(None)
                    else :
                        tmp = fields[fieldNumber].getOrganism()
                        fields[fieldNumber].setValue(fields[newPosition].getOrganism())
                        fields[newPosition].setValue(tmp)
                else:
                    fields[newPosition].getOrganism().collision(fields, sizeX, sizeY, newPosition, fieldNumber)
        self.__turnsSinceAbility += 1
        if self.__usesSpecialAbility and self.__turnsSinceAbility == 5:
            self.__turnsSinceAbility = 0
            self.__usesSpecialAbility = False
#if special ability is not active then collision will work here 
    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        if self.__usesSpecialAbility:
            freeField = self.getFreeSpot(fields, fieldNumber, sizeX, sizeY)
            if freeField != -1:
                fields[freeField].setValue(fields[fieldNumber].getOrganism())
                fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
                fields[attackerPreviousField].setValue(None)
            else:
                tmp = fields[fieldNumber].getOrganism()
                fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
                fields[attackerPreviousField].setValue(tmp)
        else:
            attackerStrength = fields[attackerPreviousField].getOrganism().getStrength()
            thisOrganismStrength = fields[fieldNumber].getOrganism().getStrength()
            if(attackerStrength >= thisOrganismStrength):
                fields[fieldNumber].setValue(fields[attackerPreviousField].getOrganism())
                fields[attackerPreviousField].setValue(None)
            else:
                fields[attackerPreviousField].setValue(None)