from abc import ABC, abstractmethod

class Organism:
    __age = 0
    _strength = 0
    _initiative = 0

    @abstractmethod
    def action(self, fields, sizeX, sizeY, fieldNumber):
        pass

    @abstractmethod
    def collision(self, fields, sizeX, sizeY, fieldNumber, attackerPreviousField):
        pass

    @abstractmethod
    def draw(self):
        pass

    def getStrength(self):
        return self._strength

    def getAge(self):
        return self.__age
    
    def addAge(self):
        self.__age += 1
    
    def setAge(self, value):
        self.__age = value
    
    def addStrength(self, value):
        self._strength += value

    def getInitiative(self):
        return self._initiative