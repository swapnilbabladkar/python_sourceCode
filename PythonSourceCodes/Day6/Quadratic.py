# Quad Equn Soln

import math

def solveQuadratic(a,b,c):
    dis = (b**2 - 4 * a * c)
    if a<0:
        raise ZeroDivisionError , "Not a quadratic Equation. Its a Linear equn"
    elif dis < 0:
        raise ValueError , "Imaginary roots as discriminant < 0"
    else:
        x1 = (-b + math.sqrt(dis))/(2*a)
        x2 = (-b - math.sqrt(dis))/(2*a)
        return x1, x2

try:
    r1,r2 = solveQuadratic(10,5,6)    
except ValueError,ErrorMsg:
    print "Rcvd: ", ErrorMsg
except ZeroDivisionError,ErrorMsg:
    print "Rcvd: ", ErrorMsg
else:
    print r1, " ", r2
finally:
    print "See you soon!"
