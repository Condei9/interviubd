############ import ############

import sys
import mostUsedNamesLibrary as mun

############ data input ############

f = open(sys.argv[1], "r")
k = int(sys.argv[2])

####################################

dictionaryWithNames = mun.mostUsedNames(f)
f.close()

############ printing most used k names ############

for i in range(k):
   print(dictionaryWithNames[i])

####################################