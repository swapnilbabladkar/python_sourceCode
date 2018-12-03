# Sum of first N natural numbers

def sumOfNRecursively(n):
    if n==1:
        return 1
    else:
        return n + sumOfNRecursively(n-1)

num = input('Enter a number:')
print "Sigma(", num, ") = " , sumOfNRecursively(num)
