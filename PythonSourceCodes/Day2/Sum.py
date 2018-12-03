def sumDiffOfNumbers(val1,val2):
    s = val1 + val2
    d = val1 - val2
    return s,d

a = input('Enter the first number:')
b = input('Enter the second number:')
ss,dd = sumDiffOfNumbers(a,b)          
print "Sum = ", ss , " Diff = ", dd
