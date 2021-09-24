import shingling
import vectorize
import minimumHashing

import numpy

def setGenerator():

    file = 'dataset.txt'
    query=input('enter the query:\n')
    
    with open("dataset.txt") as f: 
        lines = f.readlines()  

    lines[0] = query + '\n'+ lines[0] 
 
    with open("dataset.txt", "w") as f: 
        f.writelines(lines) 

    k = input('Input shingle size, mostly between 4-8:\n')
    hashmap = shingling.createShingles(file, k)
    arr = vectorize.vectorizing(hashmap)
    similarityMatrix = minimumHashing.minHashing(arr)
    numpy.save("Similarity Matrix", similarityMatrix, allow_pickle=False, fix_imports=False)

    commonset = set()
    similarityMatrix = numpy.load('Similarity Matrix.npy')
    band = int(input("Input the band size:\n"))  
    similarityThreshold = float(input("Input the similarity threshold. A value between \'0.7\'-\'0.9\':\n")  )# take = 0.8

    for i in range(0, int(100 / band)):
        hashtable = {}
        for j in range(0, similarityMatrix.shape[1]):
            k = tuple(similarityMatrix[band * i:band * (i + 1), j])
            if k in hashtable:
                sim = vectorize.jaccardSimilarity(similarityMatrix[:, hashtable[k]], similarityMatrix[:, j])
                if sim > similarityThreshold:
                    commonset.add((hashtable[k], j))
            else:
                hashtable[k] = j

    # print(commonset)
    return commonset


