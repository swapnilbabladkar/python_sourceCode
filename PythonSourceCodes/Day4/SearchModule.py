# Define a module having a function
# implementing Binary Search. The called function will return the index
# of the element to the calling function.
# Also have Linear Search algo implemented in this module.

# We will later compare their performances.

def LinearSearch(vList,item):
    flag = 0
    for i in range(len(vList)):
        if item == vList[i]:            
            flag = 1
            pos = i
            break
    if flag == 0:
        return -1
    else:
        return pos

def BinarySearch(vList,item):
    start = 0
    end = len(vList) - 1
    mid = (start + end) / 2
    flag = 0
    while(vList[mid] != item and (start!=mid and end!=mid)):
        # print start, " : ", end, " : ", mid
        mid = (start + end) / 2
        if vList[mid] > item:
            end = mid
        elif vList[mid] < item:
            start = mid
        else:
            flag = 1
            break
        mid = (start + end) / 2
        if(vList[mid] == item ):
            flag = 1
            break
    if flag == 1:
        return mid
    else:
        return -1


L = [2,3,5,7,9,10,15,22,25]
print LinearSearch(L,22)
print BinarySearch(L,22)
