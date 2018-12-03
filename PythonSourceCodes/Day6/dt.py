import doctest;

def fib(n):
    '''
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(4)
    3
    >>> 
    '''
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    doctest.testmod()
