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
    
vdict = {}
vdict["My Rectangle"]  =  Rectangle(12,10)
vdict["My Square"]  =  Square(5)
vdict["My Dbl Square"]  =  DoubleSquare(7)

for i in vdict.keys():
    # print "For: ", i , " Area = " , vdict[i].area(), " Peri = " , vdict[i].perimeter()
    print "For: %-20s Area = %-10d Peri = %-10d"%(i,vdict[i].area(),vdict[i].perimeter())

