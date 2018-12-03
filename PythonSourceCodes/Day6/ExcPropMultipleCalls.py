# sqrt(x) + 1

from math import sqrt

def a(x):
    return b(x) + 1

def b(x):
    if x<0:
        raise ValueError,"Sq Root of a negative no yields imag values"
    else:
        return sqrt(x)


try:
    print a(-16)
except ValueError,ErrorMsg:
    print "Received Error : ", ErrorMsg
    
