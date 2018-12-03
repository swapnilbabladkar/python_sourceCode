def extendList(val,list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123)
list3 = extendList('a')

print("List 1 : %s " % list1)
print("List 2 : %s " % list2)
print("List 3 : %s " % list3)
