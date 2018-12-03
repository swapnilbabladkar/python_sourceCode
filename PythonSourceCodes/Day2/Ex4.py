def sum(*args):
    #Sum of arbitrary number
    # of arguments '''
    r=0
    for i in args:
        r += i
    return r
print sum.__doc__
print sum(1,2,3)
print sum(1,2,3,4,5)
