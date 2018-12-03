class Rectangle:
    def __init__(self,l=None,b=None):
        #Constructor Overloading
        if l != None and b!= None:
            self.l  = l
            self.b = b
        else:
            self.l = self.b = 0
    def setLen(self,len):
        self.l = len
    def setBre(self,bre):
        self.b = bre
    def display(self):
        dtls = "Len = " + str(self.l) + " Bre = " + str(self.b)
        return repr(dtls)
    def area(self):
        return self.l * self.b
    def peri(self):
        return 2 * (self.l + self.b)
    

#Array of Rectangle objects            
r = [Rectangle() for i in range(4)]
for i in range(3):
    r[i].l = 2 * i
    r[i].b = i

for i in range(4):
    print("Details :  ", r[i].display(), "Area: ", r[i].area() , "Perimeter: ", r[i].peri() )

