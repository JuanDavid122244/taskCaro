#
# Student Name   : Carolina Cardona Osorio 
# Student Number : 21070000
#
# caterpillar.py - plotting the adventures of a very hungry caterpillar
#
import matplotlib.pyplot as plt
import numpy as np


# Caterpillar code
catx = np.array([40,55,70,85,100])
caty = np.array([30,30,30,30,30])
catcol = ["green","green","green","green","red"]

# Day/count/food/colour code
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
counts = [1,2,3,4,5]
foods = ["Apple", "Pear", "Plum", "Strawberry", "Orange"]
colours = ["chartreuse", "yellow", "plum", "crimson", "orange"]

num_days = len(days)

# Supplied

plt.xlim([0,num_days*100+100])
plt.ylim([0,num_days*100+100])
plt.title("The Caterpillar ate...", fontsize="18")
pos = [100, 100]
plt.scatter(pos[0], pos[1], c=colours[0], s=500)
#plt.show()

# Question 1
plt.xlim([0,num_days*100+100])
plt.ylim([0,num_days*100+100])
for i in range (num_days):
    pos = [i*100+100, 100]
    plt.scatter(pos[0], pos[1], c=colours[i], s=500)
plt.show()

# Question 2
plt.xlim([0,num_days*100+100])
plt.ylim([0,num_days*100+100])
plt.title("The Caterpillar ate...", fontsize="18")
for i in range (num_days):
    for j in range (i+1):
        pos = [i*100+100, j*100+100]
        plt.scatter(pos[0], pos[1], c=colours[i], s=500)
plt.show()

# Question 3 - multiple days
plt.xlim([0,num_days*100+100])
plt.ylim([0,num_days*100+100])
for i in range (num_days):
    plt.xlim([0,num_days*100+100])
    plt.ylim([0,num_days*100+100])
    plt.title("On"+ days[i] +  "The Caterpillar ate...", fontsize="18")
    for j in range (i+1):
        for k in range (j+1):
            pos = [j*100+100, k*100+100]
            plt.scatter(pos[0], pos[1], c=colours[j], s=500)
    plt.show()

# Question 4 - annotation and caterpillar
for i in range (0,num_days):
    plt.xlim([0,num_days*100+100])
    plt.ylim([0,num_days*100+100])
    for j in range (0, i+1):
        for k in range (0,j+1):
            pos=[100,100]
            plt.scatter(pos[0]+j*100, pos[1]+(100*k), c=colours[j], s=500)
            if(k==0):
                an=str(k+1)+ ' '+ foods [j]
            else:
                an=str(k+1)+ ' ' +foods[j] + 's'          
            plt.annotate(an, [pos[0] + (j*100), pos[1] + (100*k)+ 40], fontsize=6, ha="center")
    plt.scatter(catx + 100*i, caty, c=catcol, s=100+(75*i))
    plt.title('On'+days[i]+  "The Caterpillar ate...", fontsize="18")
    plt.show()
