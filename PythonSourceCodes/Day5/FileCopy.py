# Read a file. Copy its contents to another file
# and also print on console with the line number at the beginning.
# 1: Line 1
# 2: Line 2 ...

f_in = open('Poem.txt')
f_out = open('Poem_copied.txt','w')

i = 1

for line in f_in:
    print(str(i) + " : " + line.rstrip())
    f_out.write(str(i) + " : " + line)
    i += 1
f_out.close()
f_in.close()
