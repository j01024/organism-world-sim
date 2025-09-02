import tkinter as tk
from Wolf import Wolf
from Sheep import Sheep
from Antelope import Antelope
from Belladonna import Belladonna
from Fox import Fox
from Turtle import Turtle
from Grass import Grass
from Guarana import Guarana
from SosnowskyHogweed import SosnowskyHogweed
from SowThistle import SowThistle
from Human import Human

class Field:
    __organism = None
    __b = None
    __empty = True

    def __createOrganism(self, org, s = -1, a = -1, u = -1, t = -1):
        self.__empty = False
        if s != -1:
            if org == 10:
                self.__organism = Human(s, a, u, t)
            elif org == 0:
                self.__organism = Wolf(s, a)
            elif org == 1:
                self.__organism = Sheep(s, a)
            elif org == 2:
                self.__organism = Antelope(s, a)
            elif org == 3:
                self.__organism = Belladonna()
            elif org == 4:
                self.__organism = Fox(s, a)
            elif org == 5:
                self.__organism = Turtle(s, a)
            elif org == 6:
                self.__organism = Grass()
            elif org == 7:
                self.__organism = Guarana()
            elif org == 8:
                self.__organism = SosnowskyHogweed()
            elif org == 9:
                self.__organism = SowThistle()
        else:
            if org == 10:
                self.__organism = Human()
            elif org == 0:
                self.__organism = Wolf()
            elif org == 1:
                self.__organism = Sheep()
            elif org == 2:
                self.__organism = Antelope()
            elif org == 3:
                self.__organism = Belladonna()
            elif org == 4:
                self.__organism = Fox()
            elif org == 5:
                self.__organism = Turtle()
            elif org == 6:
                self.__organism = Grass()
            elif org == 7:
                self.__organism = Guarana()
            elif org == 8:
                self.__organism = SosnowskyHogweed()
            elif org == 9:
                self.__organism = SowThistle()

    def __init__(self, frame, c, r, org, s = -1, a = -1, u = -1, t = -1):
        if org != -1:
            if s != - 1:
                self.__createOrganism(org, s, a, u, t)
            else:
                self.__createOrganism(org)
            text = self.__organism.draw()
        else:
            text = ""
        self.__b = tk.Button(frame, text=text, width=5, height=1, command = lambda: self.__command())
        self.__b.grid(column=c, row=r)

    def getField(self):
        return self.__b

    def isEmpty(self):
        return self.__empty

    def setValue(self, value):
        if value == None:
            self.__organism = None
            self.__empty = True
            self.__b.config(text="")
        else:
            self.__organism = value
            self.__empty = False
            self.__b.config(text=value.draw())

    def getOrganism(self):
        return self.__organism

    def __createOrganismByButton(self, org, r):
        self.__createOrganism(org)
        self.__b.config(text=self.__organism.draw())
        self.__empty = False
        r.destroy()

    def __command(self):
        if self.isEmpty():
            r = tk.Tk()
            r.geometry("250x300")
            r.title("Choose organism")
            but1 = tk.Button(r, text="Wolf", width = 20, command = lambda: self.__createOrganismByButton(0, r))
            but1.grid(column=0, row=0)
            but2 = tk.Button(r, text="Sheep", width = 20, command = lambda: self.__createOrganismByButton(1, r))
            but2.grid(column=0, row=1)
            but3 = tk.Button(r, text="Antelope", width = 20, command = lambda: self.__createOrganismByButton(2, r))
            but3.grid(column=0, row=2)
            but4 = tk.Button(r, text="Belladonna", width = 20, command = lambda: self.__createOrganismByButton(3, r))
            but4.grid(column=0, row=3)
            but5 = tk.Button(r, text="Fox", width = 20, command = lambda: self.__createOrganismByButton(4, r))
            but5.grid(column=0, row=4)
            but6 = tk.Button(r, text="Turtle", width = 20, command = lambda: self.__createOrganismByButton(5, r))
            but6.grid(column=0, row=5)
            but7 = tk.Button(r, text="Grass", width = 20, command = lambda: self.__createOrganismByButton(6, r))
            but7.grid(column=0, row=6)
            but8 = tk.Button(r, text="Guarana", width = 20, command = lambda: self.__createOrganismByButton(7, r))
            but8.grid(column=0, row=7)
            but9 = tk.Button(r, text="Sosnowsky Hogweed", width = 20, command = lambda: self.__createOrganismByButton(8, r))
            but9.grid(column=0, row=8)
            but10 = tk.Button(r, text="Sow Thistle", width = 20, command = lambda: self.__createOrganismByButton(9, r))
            but10.grid(column=0, row=9)
            r.mainloop()
