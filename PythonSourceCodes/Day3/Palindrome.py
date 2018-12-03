# Check if a string is Palindrome or not
# MADAM / ANNA , etc.

mystr = raw_input('Enter a string:')
mystr_to_list = list(mystr)
mystr_to_list.reverse()
mystr_r = ''.join(mystr_to_list)

if(mystr == mystr_r):
    print "Palindrome"
else:
    print "Not a palindrome"
