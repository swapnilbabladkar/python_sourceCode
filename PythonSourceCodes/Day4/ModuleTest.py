# Defining our own custom modules
# Purpose: Reusable components

#Variables
numberOfParticipants = 35
year = 2016

#Functions
def someFunc():
    return "Hola!"

# Classes
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
