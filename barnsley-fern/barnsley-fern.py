from turtle import *
import random
import sys

sys.setrecursionlimit(4000)

x = 0
y = 0

def drawNumber(x, y):
    color("green")
    penup()
    setpos(x * 20, y * 20)
    pendown()
    dot(2)

def barnsleyfern(x, y, it):
    r_int = random.random()
    if it >= 3290:
        print("Done")
        return x, y
    elif r_int < 0.01:
        x = 0
        y = 0.16 * y
        drawNumber(x, y)
        it += 1
        return barnsleyfern(x, y, it)
    elif r_int < 0.86:
        x = 0.85 * x + 0.04 * y
        y = -0.04 * x + 0.85 * y  + 1.6
        drawNumber(x, y)
        it += 1
        return barnsleyfern(x, y, it)
    elif r_int < 0.93:
        x = 0.2 * x - 0.26 * y
        y = 0.23 * x + 0.22 * y + 1.6
        drawNumber(x, y)
        it += 1
        return barnsleyfern(x, y, it)
    else:
        x = -0.15 * x + 0.28 * y
        y = 0.26 * x + 0.24 * y + 0.44
        drawNumber(x, y)
        it += 1
        return barnsleyfern(x, y, it)

tracer(0,0)
barnsleyfern(x, y, 0)
hideturtle()
update()
mainloop()