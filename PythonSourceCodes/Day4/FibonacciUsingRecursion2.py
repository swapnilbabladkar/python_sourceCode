# Find out the nth Fibonacci number using Recursion
# 1,1,2,3,5,8......
# Arithmetically it starts from 0. So 0,1 ,1 , 2, 3, ....

def Fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

num = input('Enter the value of n:')
print "Fibo(", num, ") = " , Fibonacci(num)

