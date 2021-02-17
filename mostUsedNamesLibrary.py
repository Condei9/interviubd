########################### import ##############################

import nltk

############ making sure nltk packages are up to date ############

nltk.download("punkt", quiet = True)
nltk.download("stopwords", quiet = True)

##################################################################

from collections import defaultdict
from operator import itemgetter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

##################################################################

punctuation = {".", ",", "!", "?", "-"}
stop_words = set(stopwords.words('english'))

##################### mostUsedNames function #####################
######### - takes in a file as a parameter and returns ###########
#########   a sorted defaultdict with the most used    ###########
#########   names in the file                          ###########
##################################################################

def mostUsedNames(f):
    apparitions = defaultdict(int)
    f.seek(0)
    name = ""
    isPunctuation = 0
    for line in f:
        words = word_tokenize(line)
        for m in words:
            if isPunctuation == 0:
                if m[0].isupper() and m.lower() not in stop_words:
                    name += m + " "
                elif name != "":
                    name = name[:-1]
                    apparitions[name] += 1
                    name = ""
                if m in punctuation:
                    isPunctuation = 1
            else:
                isPunctuation = 0;
    return sorted(apparitions.items(), key=itemgetter(1), reverse=True)

####################  a simple print function   ###################

def printDict(usedDictionary, k):
    for i in range(k):
        print(usedDictionary[i])
        
############################### END ###############################