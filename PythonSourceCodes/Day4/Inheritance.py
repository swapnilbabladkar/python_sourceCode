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
    

r1 = Rectangle(12,10)
s1 = Square(15)
print "Details = ", s1.printDetails()
print "Area = ", s1.area()
print "Peri = ", s1.perimeter()
