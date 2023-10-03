import matplotlib.pyplot as plt
import numpy as np
import random

def flipCoords(rcpos,LIMITS):
    y = rcpos[0]
    x = rcpos[1]
    return (x,y)

class Ant():
    size = 0.5

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.colour = "red" 
        #self.heading = heading

    def getPos(self):
        return self.pos

    def stepChange(self,subgrid):
        validMoves = [(1,0), (-1,0)]
        print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

class Butterfly():

    def __init__(self, name, pos, colour):
        self.name = name
        self.pos = pos
        self.colour = colour
        self.size = 1

    def getPos(self):
        return self.pos

    def stepChange(self,subgrid):
        validMoves = [(1,-1),(1,1)]
        print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])

    def plotMe(self, ax,LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)
