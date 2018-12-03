# Read the contents of a file

fp = open('ArrayOfObj.py','r+')
ifile = fp.read()
fp.close()
print(ifile)

# Alternatively,

print("Alternative method for file opening:")
with open('ArrayOfObj.py') as fp:
    ifile = fp.read()
print(ifile)
