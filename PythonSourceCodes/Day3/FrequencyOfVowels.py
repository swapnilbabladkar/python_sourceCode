# Take a string from  user.
# Count the occurrences of each vowel in the string.
# A : 1
# E : 3 & so on

vsent = raw_input('Enter a string:')
vwls = ['a','e','i','o','u']
cnt=[]

for item in vwls:
    print item, ' : ', vsent.lower().count(item)
