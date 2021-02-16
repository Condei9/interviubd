import sys
#data input
f = open(sys.argv[1], "r")
k = int(sys.argv[2])

###########
#----------printing all the words that start with uppercase
#for line in f:
#    word = line.split()
#    for m in word:
#        if m[0].isupper():
#            print(m)
#            k = k+1
############

from collections import defaultdict
from operator import itemgetter
import time
start_time = time.time()

def process(f):
    apparitions = defaultdict(int)
    f.seek(0)
    for line in f:
        words = line.split()
        for m in words:
            if m[0].isupper():
                apparitions[m] += 1
    return sorted(apparitions.items(), key=itemgetter(1), reverse=True)

x = process(f)
for a in range(k):
    print(x[a])

print("%s secunde" % (time.time() - start_time))
f.close()