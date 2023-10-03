import matplotlib.pyplot as plt
import numpy as np
from garden import *

def getSubgrid(t, pos):
    rmin = pos[0]-1
    rmax = pos[0]+2
    cmin = pos[1]-1
    cmax = pos[1]+2
    print(rmin, rmax, cmin, cmax)
    sub = t[rmin:rmax,cmin:cmax]
    return sub

def main():
    LIMITS = (50,50)
    print("\nWelcome to the Secret Garden...\n")
    print("LIMITS ARE:",LIMITS)

    terrain = np.zeros(LIMITS)
    ant = Ant("A1", (40,30))
    bfly = Butterfly("B1", (10,25), "yellow")

    plt.figure(figsize=(8,8))
    ax = plt.axes()
    ax.set_aspect("equal")

    ants = []
    bflys = []
    for i in range(5):
        a= Ant("A1", (15 + (i*5),30))
        ants.append(a)
        b=Butterfly("B1", (5 + (i*6),10), "yellow")
        bflys.append(b)
    
        for j in range(5):
            for a in ants:
            a.stepChange(getSubgrid(terrain, a.getPos()))
            print(a)
            a.plotMe(ax, LIMITS)

    plt.imshow(terrain)

    print("\nAnt ##########################")
    ant.stepChange(getSubgrid(terrain, ant.getPos()))
    print(ant)
    ant.plotMe(ax, LIMITS)

    print("\nButterfly ##################")
    bfly.stepChange(getSubgrid(terrain, bfly.getPos()))
    print(bfly)
    bfly.plotMe(ax, LIMITS)

    plt.title("Initial Code", fontsize="18")
    plt.grid()
    plt.show()
    plt.pause(1)
    plt.cla()

if __name__ == "__main__":
    main()
