def modifyList(vlist):
    vlen = len(vlist)
    print "List Length : ", vlen
    del vlist[vlen-1]

myList = ['E','J','O','T','Y']
print myList
modifyList(myList[:])
print myList
