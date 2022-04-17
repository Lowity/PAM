from turtle import *
from typing import List

import numpy as np
from alive_progress import alive_bar

width = 400
height = 700

setup(width, height)

def checkMandelbrot(c):
    n = 0
    it = 0
    while abs(n) < 2 and it <= 10:
        n = n**2 + c
        #print(n)
        it += 1
    if abs(n) < 2:
        return True
    else:
        return False

def pix_to_complex(x, y, w, h):
    #Adapt coordinate system to screen
    #Adapt for x values
    point_q = [-w/2, w/2]
    point_r = [-2, 2]
    func = np.polyfit(point_q, point_r, 1)
    #Adapt for y values
    output = np.poly1d(func)
    x = output(x)
    y = output(y)
    return complex(round(x, 3), round(y, 3))

def drawNumber(x, y):
    penup()
    setpos(x, y)
    pendown()
    dot(0.5)
    
def drawMandelbrot(w, h):
    with alive_bar() as bar:
        for x in range(int(-(w/2)), int((w/2))):
            for y in range(int(-(w/2)), int((w/2))):
                c = pix_to_complex(x, y, w, h)
                if checkMandelbrot(c) == True:
                    drawNumber(x, y)
                bar()

tracer(0,0)
drawMandelbrot(width, height)
update()
mainloop()
