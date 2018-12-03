# Prime or Not
# sqrt(n)
# 

import math

n = int(input('Enter a number:'))
i = 2
while (i<math.sqrt(n)):
    if n%i == 0:
        print (n, "is not a Prime Number. Factor", i )
        break
    i+=1
else:
    print(n, "is a Prime Number")
    
