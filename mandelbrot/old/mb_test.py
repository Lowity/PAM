from typing import List
from turtle import *
import numpy as np

np.seterr(invalid='ignore')

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

def drawNumber(x, y):
    penup()
    setpos(x, y)
    pendown()
    dot(0.5)

def pix_to_complex(x, y, w, h):
    #Adapt coordinate system to screen
    #Adapt for x values
    x_point_q = [0, w]
    x_point_r = [-2, 2]
    x_func = np.polyfit(x_point_q, x_point_r, 1)
    #Adapt for y values
    y_point_q = [(h-w)/2, h-((h-w)/2)]
    y_point_r = [2, -2]
    y_func = np.polyfit(y_point_q, y_point_r, 1)
    output_x = np.poly1d(x_func)
    output_y = np.poly1d(y_func)
    x = output_x(x)
    y = output_y(y)
    return complex(round(x, 3), round(y, 3))
    
def drawMandelbrot(w, h):
    for x in range(w):
        for y in range(int((h-w)/2), int(h-((h-w)/2))):
            c = pix_to_complex(x, y, w, h)
            if checkMandelbrot(c) == True:
                drawNumber(x, y)

#tracer(0,0)
drawMandelbrot(width, height)
#update()
#mainloop()


