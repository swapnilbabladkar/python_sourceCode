# Implement factorial using recursion

def factRecursively(n):
    if n==1:
        return 1
    else:
        return n * factRecursively(n-1)

num = input('Enter a number:')
print "Fact(", num, ") = " , factRecursively(num)
