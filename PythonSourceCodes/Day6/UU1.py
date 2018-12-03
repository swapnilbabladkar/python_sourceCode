def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

if __name__ == "__main__":
    if fib(0)==0  and fib(10)==55:
        print "Good"
    else:
        print "Bad"
