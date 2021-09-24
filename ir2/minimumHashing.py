from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
import string
import re
import random
import numpy as np
import time
# shuffle is used to generate a random shuffling of
# an array of elements 0 to size-1.
# input : int size which is the number of shingles
# return : a numpy array in of elements in range 0 to size - 1
#          both inclusive shuffled in a random order.


def shuffle(size):
    hashedList = np.arange(size)
    for i in range(0, size - 1):
        j = random.randrange(i + 1, size)  # i+1 instead of i
        hashedList[i], hashedList[j] = hashedList[j], hashedList[i]
    return hashedList


# shuffleList is used to generate a random shuffling of
# an array of elements 0 to size-1 but the input is different then
# the other function
# input : a numpy array of elements in range 0 to size - 1
# return : a numpy array in of elements in range 0 to size - 1
#          both inclusive shuffled in a random order.


def shuffleList(hashedList):
    size = np.size(hashedList)
    random.seed(time.time())
    for i in range(0, size - 1):
        j = random.randrange(i + 1, size)  # i+1 instead of i
        hashedList[i], hashedList[j] = hashedList[j], hashedList[i]
    return hashedList

def minHashing(arr):
    x, y = arr.shape  # x = number of shingles,y = number of documents

    signatureMatrix = np.empty((100, y), dtype=np.int32)
    signatureMatrix.fill(2147483647)
    hashMatrix = np.empty((100, x), dtype=np.int32)

    hashedList = shuffle(x)

    for i in range(0, 100):
        hashedList = shuffleList(hashedList)
        hashMatrix[i] = np.array(hashedList)

    hashMatrix = np.transpose(hashMatrix)

    # hashMatrix has a dimensions of x rows and 100 columns
    # signatureMatrix has a dimensions of 100 rows and y columns

    for i in range(0, x):
        for j in range(0, y):
            if arr[i, j] == 1:
                for k in range(0, 100):
                    val = hashMatrix[i, k]
                    if signatureMatrix[k, j] > val:
                        signatureMatrix[k, j] = val

    return signatureMatrix
