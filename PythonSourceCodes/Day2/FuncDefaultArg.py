# Function returning multiple values
# substring(TENDULKAR,pos=5) >> LKAR

def modifyString(vstr,pos=5):
    return vstr[pos:]

vs = raw_input('Enter a string:')
print "String after default modification at 5th pos: ", modifyString(vs)
print "String after default modification at user def pos: ", modifyString(vs,-2)
