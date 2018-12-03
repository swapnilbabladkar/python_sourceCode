#Leap Year(y)
# y%100==0  y%400==0   LY!
# y%100!=0  y%4==0   LY!

y = int(input('Enter an year:'))
print(y)
flag=1
if(y%100 == 0):
    if(y%400==0):
        flag=1
    else:
        flag=0
else:
    if(y%4==0):   
        flag=1
    else:
        flag=0

if(flag==1):
    print ("Leap Year")
else:
    print ("Not a lep year")
