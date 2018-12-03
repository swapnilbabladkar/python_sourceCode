# doctest module
# Test case first, Implementation later

import doctest

def fib(n):
    ''' Finds the nth Fib number
    >>> fib(1)
    1
    >>> fib(8)
    21
    >>> fib(30)
    832040
    >>> fib(88)
    1100087778366101931L
    >>> 
    '''
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a


if __name__ == "__main__":
    doctest.testmod()
