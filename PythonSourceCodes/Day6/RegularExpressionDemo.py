# Find all ministries starting with H

import re

fp = open('CabinetMinisters.txt')
for line in fp:
    if re.search(r"Smr[ie]e?t[ie]",line):
        print line.rstrip()
fp.close()

