from turtle import *
import math

def triangle(l):
    right(45)
    forward(l)
    left(45)
    left(45)
    forward(l)
    right(45)

def levy(n):
    if n == 0:
        return "F"
    order = levy(n-1)
    return order.replace("F", "RFLLFR")
    
def exec_levy(order):
    for character in order:
        if character == "F":
            forward(5)
        elif character == "R":
            right(45)
        elif character == "L":
            left(45)



penup()
setpos(-200, 200)
pendown()
tracer(0,0)
exec_levy(levy(20))
update()
mainloop()

