# Read a certain number of characters from a file

with open('Poem.txt') as fp:
    ifile = fp.read(13)
    print fp.tell()
print ifile


