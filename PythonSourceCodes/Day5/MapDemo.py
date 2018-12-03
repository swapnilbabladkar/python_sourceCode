def Fahrenheit(T):
    return (9/5.0 * T) + 32

def Celcius(T):
    return (5/9.0)*(T - 32)

# List of Temperatures in Celcius
tTuple = (23.6,-40,88,95,7.6)

F = map(Fahrenheit,tTuple)
C = map(Celcius, F)
