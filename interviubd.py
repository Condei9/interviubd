############ import ############

import sys
import mostUsedNamesLibrary as mun

############ data input ############

try:
    f = open(sys.argv[1], "r")
    k = int(sys.argv[2])
except:
    print("Something went wrong with the input")

####################################
try:
    dictionaryWithNames = mun.mostUsedNames(f)
    mun.printDict(dictionaryWithNames, k)
except:
    print("An error occured - something went wrong with the function")
finally:
    f.close()

####################################