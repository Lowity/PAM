from sympy import *
from turtle import *
from typing import List
import colorsys
import numpy as np
from alive_progress import alive_bar

width = 700
height = 100

setup(width, height)

#Check wheter w or h is bigger, to adapt to the bigger value, verhältnis
if width > height:
    width = height
    height = width

colormode(255)

#Make Function and Derivate
x = Symbol("x")
my_func = x**3 - 17
my_func_prime = my_func.diff(x)
f = lambdify(x, my_func)
f_prime = lambdify(x, my_func_prime)

#Return function value
def func(c):
    return f(c), f_prime(c)

def newton_calczero(n, i, c):
    if abs(n) < 0.01 and abs(n) > 0:
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
        return newton_calczero(n, i, c)

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
    return complex(round(x, 2), round(y, 2))

def hsv_to_rgb(list_hsv):
    list_rgb = colorsys.hsv_to_rgb(list_hsv[0], list_hsv[1], list_hsv[2])
    list_rgb = list(map(lambda x: int(x*255), list_rgb))
    return list_rgb

def drawNumber(x, y, col_val):
    penup()
    setpos(x, y)
    pendown()
    #number of items in list
    l = []
    w = width
    h = height
    zero_root_list = zero_root(w, h, l)
    print(zero_root_list)
    #Adapt color hsv
    color = [360, 1, 1]
    color[0] = (col_val*360)/len(zero_root_list)
    #if col_val == 50:
        #color[2] = 0
    color = hsv_to_rgb(color)
    dot(1, color)

def newton_color(x, y, zero_root_list):
    c = pix_to_complex(x, y, width, height)
    numb = newton_calczero(0, 0, c)
    numb = round(abs(numb), 3)
    if numb not in zero_root_list:
        zero_root_list.append(numb)
    pos_n = zero_root_list.index(numb)
    drawNumber(x, y, pos_n)

def newton_drawer(w, h, l):
    with alive_bar(w**2, title="Calculating...") as bar:
        for x in range(int(-(w/2)), int((w/2))):
            for y in range(int(-(w/2)), int((w/2))):
                newton_color(x, y, l)
                bar()

def zero_root(w, h, zero_root_list):
    x_y_c_array = []
    with alive_bar(w**2, title="Calculating...") as bar:
        for x in range(int(-(w/2)), int((w/2))):
            for y in range(int(-(w/2)), int((w/2))):
                c = pix_to_complex(x, y, w, h)
                numb = newton_calczero(0, 0, c)
                numb = round(abs(numb), 2)
                if numb not in zero_root_list:
                    zero_root_list.append(numb)
                pos_n = zero_root_list.index(numb)
                x_y_c_list = []
                x_y_c_list.append(x)
                x_y_c_list.append(y)
                x_y_c_list.append(pos_n)
                x_y_c_array.append(x_y_c_list)
                bar()
    return zero_root_list, x_y_c_array

def draw_newton(zero_root_list, x_y_c_array):
    pass

tracer(0,0)

l = []

print(zero_root(width, height, l))

#newton_drawer(width, height, l)
#newton_color(25, 25, l)
hideturtle()
update()
#mainloop()




