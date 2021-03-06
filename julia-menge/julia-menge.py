#Seya Fässler 18.04.22
from turtle import *
from typing import List
import colorsys
import numpy as np
from alive_progress import alive_bar

width = 500
height = 200

setup(width, height)

#Check wheter w or h is bigger, to adapt to the bigger value, verhältnis
if width > height:
    width = height
    height = width

colormode(255)

def calcJulia(z, c, iter):
    if iter < 50 and abs(z) < 2:
        z = z**3 + c
        iter += 1
        return calcJulia(z, c, iter)
    return iter

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

def hsv_to_rgb(list_hsv):
    list_rgb = colorsys.hsv_to_rgb(list_hsv[0], list_hsv[1], list_hsv[2])
    list_rgb = list(map(lambda x: int(x*255), list_rgb))
    return list_rgb

def drawNumber(x, y, col_val):
    penup()
    setpos(x, y)
    pendown()
    #Adapt color hsv
    color = [360, 1, 1]
    color[0] = (col_val*360)/50
    if col_val == 50:
        color[2] = 0
    color = hsv_to_rgb(color)
    dot(1, color)

    
def drawJulia(w, h, c):
    with alive_bar(w**2, title="Calculating...") as bar:
        for x in range(int(-(w/2)), int((w/2))):
            for y in range(int(-(w/2)), int((w/2))):
                z = pix_to_complex(x, y, w, h)
                n = calcJulia(z, c, 0)
                drawNumber(x, y, n)
                bar()

c = complex(-0.5, 0.4)

tracer(0,0)
drawJulia(width, height, c)
hideturtle()
update()
mainloop()
