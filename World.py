import tkinter as tk
from Field import Field
import random

class World:
    __frame = None
    __root = None
    __label = None
    __x = 0
    __y = 0
    __fields = []
    __order = []
    __amountOfOrganismsInOrderArray = 0

    def __init__(self, x ,y):
        self.__x = x
        self.__y = y
        World.__root = tk.Tk()
        World.__root.geometry("600x600")
        self.__root.bind('<KeyPress>', self.__makeTurns)
        World.__frame = tk.Frame(World.__root, width=600, height=600)
        World.__root.title("md jahid hasan Arif, 192095")
        r = 0
        for i in range(x * y):
            org = -1
            a = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            if a >= 0 and a <= 2:
                org = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            if(i == 0):
                org = 10
            self.__fields.append(Field(self.__frame, (i % x), r, org))
            if i % x == x - 1:
                r += 1
        World.__frame.pack()

    def __orderOrganisms(self):
        self.__order = []
        firstAdded = False
        amountAdded = 0
        self.__amountOfOrganismsInOrderArray = 0
        for i in range(self.__x * self.__y):
            if self.__fields[i].isEmpty() == False:
                self.__order.append(i)
                if firstAdded == False:
                    firstAdded = True
                else:
                    for j in range(amountAdded):
                        if self.__fields[self.__order[j]].getOrganism().getInitiative() < self.__fields[self.__order[amountAdded]].getOrganism().getInitiative():
                            tmp = self.__order[j]
                            self.__order[j] = self.__order[amountAdded]
                            self.__order[amountAdded] = tmp
                        elif self.__fields[self.__order[j]].getOrganism().getInitiative() == self.__fields[self.__order[amountAdded]].getOrganism().getInitiative():
                            if self.__fields[self.__order[j]].getOrganism().getAge() < self.__fields[self.__order[amountAdded]].getOrganism().getAge():
                                tmp = self.__order[j]
                                self.__order[j] = self.__order[amountAdded]
                                self.__order[amountAdded] = tmp
                amountAdded += 1
                self.__amountOfOrganismsInOrderArray += 1

    def __makeTurns(self, mov):
        if mov.char == "s":
            self.__saveToFile()
        elif mov.char == "l":
            self.__loadToFile()
        else:
            self.__orderOrganisms()
            isHumanOnBoard = False
            for i in range(self.__amountOfOrganismsInOrderArray):
                if self.__fields[self.__order[i]].isEmpty() == False:
                    self.__fields[self.__order[i]].getOrganism().addAge()
                    if(self.__fields[self.__order[i]].getOrganism().draw() == "H"):
                        isHumanOnBoard = True
                        self.__fields[self.__order[i]].getOrganism().action(self.__x, self.__y, self.__order[i], self.__fields, mov.keysym)
                    else:
                        self.__fields[self.__order[i]].getOrganism().action(self.__x, self.__y, self.__order[i], self.__fields)
            if not isHumanOnBoard:
                self.__root.destroy()

    def drawWorld(self):
        self.__root.mainloop()

    def __saveToFile(self):
        f = open("game_save.txt", "w")
        for i in range(self.__x * self.__y):
            if not self.__fields[i].isEmpty():
                if self.__fields[i].getOrganism().draw() == "H":
                    u = 0
                    if self.__fields[i].getOrganism().usesSpecialAbility():
                        u = 1
                    f.write(str(i) + " " + self.__fields[i].getOrganism().draw() + " " + str(self.__fields[i].getOrganism().getStrength()) + " " + str(self.__fields[i].getOrganism().getAge()) + " " + str(u) + " " + str(self.__fields[i].getOrganism().turnsSinceAbility()) + "\n")
                else:
                    f.write(str(i) + " " + self.__fields[i].getOrganism().draw() + " " + str(self.__fields[i].getOrganism().getStrength()) + " " + str(self.__fields[i].getOrganism().getAge()) + "\n")
            else:
                f.write(str(i) + " E\n")
        f.close()

    def __getOrganismNumber(self, org):
        if org == "H":
            return 10
        elif org == "W":
            return 0
        elif org == "S":
            return 1
        elif org == "A":
            return 2
        elif org == "B":
            return 3
        elif org == "F":
            return 4
        elif org == "T":
            return 5
        elif org == "G":
            return 6
        elif org == "U":
            return 7
        elif org == "Y":
            return 8
        elif org == "O":
            return 9
    
    def __loadToFile(self):
        f = open("game_save.txt", "r")
        self.__fields = []
        i = 0
        r = 0
        for x in f:
            a = x.split(" ")
            if a[1] == "E\n":
                self.__fields.append(Field(self.__frame, (i % self.__x), r, -1))
            else:
                if a[1] == "H":
                    self.__fields.append(Field(self.__frame, (i % self.__x), r, self.__getOrganismNumber(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5])))
                else:
                    self.__fields.append(Field(self.__frame, (i % self.__x), r, self.__getOrganismNumber(a[1]), int(a[2]), int(a[3])))
            if i % self.__x == self.__x - 1:
                r += 1
            i += 1
        f.close()
