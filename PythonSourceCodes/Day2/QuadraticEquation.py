# Solve a Quadratic Equation by using functions
# ax^2 + bx + c = 0
# x = (-b + sqrt(b^2 - 4ac))/ (2a)

from math import sqrt

def solveQuad(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/2.0*a
    x2 = (-b - sqrt(b**2 - 4*a*c))/2.0*a
    return x1,x2

a = input('Enter a:')
b = input('Enter b:')
c = input('Enter c:')
x1,x2 = solveQuad(a,b,c)
print "Roots: ", x1,x2
