# Sum of natural numbers from 1 to N

def SumOfN(N):
    s=0
    for i in range(1,N):
        s+=i
    return s

print "Sum:", SumOfN(input('Enter N:'))
