# Fibonacci Series

def fib(n):
    a,b = 1,1
    for i in range(n):
        a,b = b, a+b
    return a

if __name__ == "__main__":
    if fib(1) == 1 and fib(2) == 1 and fib(3) == 2 and fib(5) == 5:
        print("Correct Implementation")
        print("Well done!")
    else:
        print("Recheck your algorithm")
    
