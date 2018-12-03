# Find out all the .py scripts (Python scripts) in your current directory.

import os

for items in os.listdir('.'):
    if os.path.isfile(items) and items.endswith('.txt'):
        print "Python file : ",  items
