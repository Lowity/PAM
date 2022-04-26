from sympy import *
from turtle import *
from typing import List
import colorsys
import numpy as np
from alive_progress import alive_bar

width = 200
height = 100

setup(width, height)

#Check wheter w or h is bigger, to adapt to the bigger value, verhältnis
if width > height:
    width = height
    height = width

colormode(255)

def func(c):
    x = Symbol("x")
    f = x**3 - 17
    f_prime = f.diff(x)
    f = lambdify(x, f)
    f_prime = lambdify(x, f_prime)
    return f(c), f_prime(c)

def newton(n, i, c):
    if abs(n) < 0.1 and abs(n) > 0:
        return c
    if i > 50:
        return c
    else:
        f, f_diff = func(c)
        if f_diff == 0:
            return n
        n = f/f_diff
        c = c - n
        i += 1
        return newton(n, i, c)

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

def newton_color(x, y):
    c = pix_to_complex(x, y, width, height)
    zero_root_list = []
    numb = newton(0, 0, c)
    numb = round(abs(numb), 3)
    if numb not in zero_root_list:
        zero_root_list.append(numb)
    pos_n = zero_root_list.index(numb)
    col = pos_n * 30
    drawNumber(x, y, col)

def newton_drawer(w, h):
    with alive_bar(w**2, title="Calculating...") as bar:
        for x in range(int(-(w/2)), int((w/2))):
            for y in range(int(-(w/2)), int((w/2))):
                newton_color(x, y)
                bar()


tracer(0,0)
newton_drawer(width, height)
hideturtle()
update()
mainloop()




