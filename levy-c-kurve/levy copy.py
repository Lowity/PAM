from turtle import *
import math

def makeTriangle(l):
    penup()
    backward(l)
    pendown()
    l = math.sqrt((l/2)**2 + (l/2)**2)
    right(45)
    forward(l)
    left(90)
    forward(l)


def levy(l):
    if l < 1:
        return l
    makeTriangle(l)
    l = math.sqrt((l/2)**2 + (l/2)**2)
    levy(l)
    

forward(100)
levy(100)

