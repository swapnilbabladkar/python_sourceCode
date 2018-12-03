# Find out the nth Fibonacci number using Recursion
# 1,1,2,3,5,8......
# Arithmetically it starts from 0. So 0,1 ,1 , 2, 3, ....

def Fibonacci(a,b,n):
    if n == 0 :
        return 0
    else:
        return Fibonacci(b,a+b,n-1) + a + b

num = input('Enter the value of n:')
print "Fibo(", num, ") = " , Fibonacci(1,0,num)

