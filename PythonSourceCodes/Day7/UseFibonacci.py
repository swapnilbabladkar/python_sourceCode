# This program uses the Fibonacci module.
# Every module, while being invoked, gets assigned to a built-in
# attribute __name__

from Fibonacci import fib

a = input('Enter the value of n for Fib(n):')
print fib(a)
