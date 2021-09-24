from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
import string
import re
import random
import numpy as np
import time


# vectorizing:
# input : a dictionary of with key as integer denoting a document
#         and value as a set of the shingles present in the document
# func : creates a numpy array with shingles as rows and documents
#        as columns, the array has 0 or 1 value based on whether the
#        shingle is present in document or not
# return type : a 2D numpy array which is basically a document vector
def vectorizing(hashmap):
    mainSet = set()
    for shingles in hashmap.values():
        mainSet.update(shingles)
    n = len(mainSet)
    k = len(hashmap)
    arr = np.empty((n, k), dtype=np.int8)
    shinglesDictionary = {}
    cnt = 0
    for shingle in mainSet:
        shinglesDictionary[cnt] = shingle
        for i in range(0, k):
            if shingle in hashmap[i]:
                arr[cnt, i] = 1
            else:
                arr[cnt, i] = 0
        cnt += 1
    return arr



def jaccardSimilarity(vec1,vec2):
    a = 0
    for i in range (0,100):
        if vec1[i] == vec2[i]:
            a += 1
    return a/100