from turtle import *

#n = Strichlänge
def koch(n):
    if n >= 3:
        koch(n/3)
        left(60)
        koch(n/3)
        right(120)
        koch(n/3)
        left(60)
        koch(n/3)
    else:
        forward(3)



#Koch Funktion
koch(300)

