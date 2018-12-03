# Convert a temperature from Celcius to Fahrenheit
# C/5 = (F - 32)/9
# User should accept a temp in Celcius

def CToF(cel):
    return 9/5.0*(cel) + 32.0


print "Equivalent temp in F = ", CToF(input('Enter a temp(in C):'))
