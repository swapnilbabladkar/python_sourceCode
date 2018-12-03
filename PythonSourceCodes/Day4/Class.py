# Basic Rectangle Class

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


r1 = Rectangle(12,10)
print "Details = ", r1.printDetails()
print Rectangle.area.__doc__
print "Area = ", r1.area()
print Rectangle.perimeter.__doc__
print "Peri = ", r1.perimeter()


