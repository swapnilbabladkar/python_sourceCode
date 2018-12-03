#Bubble sort a list
# Use for
# Use range

a = [12,23,22,11,67,4,0,-1,88,100,77]

for i in range(len(a) - 1):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            t=a[j]; a[j]=a[j+1]; a[j+1] = t

print(a)


