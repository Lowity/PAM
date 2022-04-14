from typing import List
import numpy

c_complex = complex(1+0.4j)
print(c_complex)

def checkMandelbrot(c):
    n = 0
    it = 0
    while abs(n) < 2 and it <= 10:
        n = n**2 + c
        print(n)
        it += 1
    if abs(n) < 2:
        return True
    else:
        return False

def checkNumbers(l):
    complex_x0 = 0
    for i in range(1000):
        for i in range(1000):
            complex_x0 += complex(0.01)
            if checkMandelbrot(complex_x0) == True:
                l.append(complex_x0)
            complex_x0 += complex(0.01j)
            if checkMandelbrot(complex_x0) == True:
                l.append(complex_x0)
        

print(checkMandelbrot(c_complex))

list = []
checkNumbers(list)
print(list)
