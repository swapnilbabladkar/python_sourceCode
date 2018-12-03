from copy import deepcopy

l1 = ['a','b',['c','d']]

# l2 = l1
l2 = deepcopy(l1)

l1[2][0] = 'u'
l2[1] = 'w'
l2[2][1] = 'v'

print(l1)
print(l2)

print("Address(l1) : " , id(l1), " Address(l2) : " , id(l2))
