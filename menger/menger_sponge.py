from turtle import *
from alive_progress import alive_bar

def drawSqaure(l):
    fillcolor("black")
    begin_fill()
    for i in range(4):
        forward(l)
        left(90)
    end_fill()

def divisor(s):
    if s < 1:
        return s
    s = s/3
    #penup()
    backward(2*s)
    right(90)
    forward(2*s)
    left(90)
    for i in range(4):
        for i in range(2):
            drawSqaure(s)
            divisor(s)
            forward(3*s)

        forward(s)
        left(90)
    forward(2*s)
    left(90)
    forward(2*s)
    right(90)

def menger(s):
    tracer(0,0)
    penup()
    drawSqaure(s)
    divisor(s)
    hideturtle()
    update()
    mainloop()

menger(100)



