import sys
#data input
f = open(sys.argv[1], "r")

k = sys.argv[2]

for line in f:
    word = line.split()
    for k in word:
        if k[0].isupper():
            print(k)


f.close()