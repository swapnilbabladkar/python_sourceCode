# Class Inheritance

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        ''' Calculate Area'''
        return self.l * self.b
    def perimeter(self):
        ''' Calculate Peri'''
        return 2 * (self.l + self.b)
    def printDetails(self):
        print "Len = " ,self.l, " Bre = ", self.b

class Square(Rectangle):
    def __init__(self,a):
        self.l = self.b = a

class DoubleSquare(Square):
    def __init__(self,a):
        self.l = 2 * a
        self.b = a
    #Overridden method
    def perimeter(self):
        return 2*self.l + 3 * self.b

r1 = Rectangle(12,10)
s1 = Square(15)
ds1 = DoubleSquare(11)
print "Details = ", ds1.printDetails()
print "Area = ", ds1.area()
print "Peri = ", ds1.perimeter()
