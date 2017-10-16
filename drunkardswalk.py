import random
import math
import numpy
import matplotlib.pyplot as plt


class DrunkardsWalk:
    x = 0 ##starting x coordinate
    y = 0 ##starting y coordinate

    T = 100 ##number of steps

    recsteps = [] ##recorded steps
    xsteps = []
    ysteps = []

    def __init__(self):
        steps(x, y)
        generateplot(xs, ys)
        
    def plotshift(x1, y1, rise, run):
        ##updates x and y plot coordinates
        new_x = x1 + run
        new_y = y1 + rise
        return(new_x, new_y)

    def generaterandom():
        ##generates random number between 0 and 2(pi) for use as the random angle measure
        rand = random.randrange(0, 180, 1)
        return(rand)

    def nextstep(x, y):
        ##using current coordinates and random angle, creates the next "step"
        angle = generaterandom()
        run = 1 * math.cos(angle)
        rise =  1 * math.sin(angle)
        new_coord = plotshift(x, y, rise, run)
        return(new_coord)

    def steps(x, y):
        ##loops through previous functions T amount of times, records them in recsteps
        i = 0
        while i < T:
            new_coord = list(nextstep(x, y))
            recsteps.insert(len(recsteps), new_coord)
            x = new_coord[0]
            xsteps.insert(len(xsteps), x)
            y = new_coord[1]
            ysteps.insert(len(ysteps), y)
            i+=1

    def generateplot(xs, ys):
        ##creates the pyplot of coordinates
        plt.plot(xs, ys)
        plt.axis([-10, 10, -10, 10])
        plt.show()

    def createlog():
        ##creates a textfile log of each step, saved into the 'history' folder
        pass







