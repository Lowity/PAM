from turtle import *
import colorsys

colormode(255)

def drawNumber_black_white(x, y, col_val):
    penup()
    setpos(x, y)
    pendown()
    #Adapt color
    color = [255, 255, 255]
    color = list(map(lambda x: int(x/50), color))
    color = list(map(lambda x: int(abs((x*col_val)-255)), color))
    #color[1] = 255
    color[2] = 255
    dot(0.5, color)


def hsv_to_rgb(list_hsv):
    h = float(list_hsv[0])
    s = float(list_hsv[1])
    v = float(list_hsv[2])
    list_rgb = colorsys.hsv_to_rgb(h/360, s, v)
    print(list_rgb)
    list_rgb = list(map(lambda x: int(x*255), list_rgb))
    return list_rgb


#def drawNumber(x, y, col_val):
    penup()
    setpos(x, y)
    pendown()
    #Adapt color hsv
    color = [360, 1, 1]
    color[0] = int(col_val * 7.2)
    if col_val == 50:
        color[2] = 0
    print(color)
    color = hsv_to_rgb(color)
    dot(100, color)

def drawNumber(x, y, col_val):
    penup()
    setpos(x, y)
    pendown()
    #Adapt color hsv
    color = [360, 1, 1]
    color[0] = int(col_val*7.2)
    if col_val == 50:
        color[2] = 0
    color = hsv_to_rgb(color)
    print(color)
    dot(100, color)


drawNumber(0, 0, 3)
mainloop()