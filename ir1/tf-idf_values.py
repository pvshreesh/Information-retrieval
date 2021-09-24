from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
import os
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import  json


vocabulary = {}
vocabulary_idf = {}
freqDist = {}
tokens_li= []
tokens_doc = []
snowball_stemmer = SnowballStemmer('english')
docs = [f for f in os.listdir('./corpus') if f.endswith(".txt")]
docs.sort()

def idf_gen():
    """
    function for building the IDF
    """
    z=0
    for word in vocabulary:
        z+=1
        print(z)
        for ts in tokens_li:
            if word in ts:
                if word in vocabulary_idf:
                    vocabulary_idf[word] = vocabulary_idf[word] + 1
                else:
                    vocabulary_idf[word] = 1

def freq_build(tokens_li):
    """
    function for building the FreqDistribution
    """
    i=0
    z=0
    for ts in tokens_li:
        z+=1
        print(z)
        freqDist[i] = FreqDist(ts)
        i = i + 1
        
def rtf(term, ts, ts_index):
    """
    Function to return the term frequency
    """
    return math.log2(1+(freqDist[ts_index][term]/float(len(ts))))

def rIDF(term):
    """ 
    Function to return corresponding idf
    searching in the vocabulary
    """
    return math.log2(len(tokens_li)/vocabulary_idf[term])

"""
Funnction for computing the primary dictionary necessary for tf-idf calculations
The structure is as follows:
It has nested dictionaries
DICTIONARY1-word in vocabulary:
                DICTIONARY2-document_number:
                    DICTIONARY3- TF,IDF,TF-IDF
"""

with open('./savers/tokens.json') as json_data:
    tokens_li = json.load(json_data)


with open('savers/words.json') as json_data:
    vocabulary = json.load(json_data)

print("yo")
freq_build(tokens_li)
idf_gen()

primaryDictionary=dict()

j=0
for vocab in vocabulary:
    j+=1
    print(j) #for keeping count of how many words of the vocabulary are done
    if vocab not in primaryDictionary:
        inner_dict=dict()
        k=0
        for ts in tokens_li:
            inner_dict[k]=dict()
            termFreq = rtf(vocab, ts, k)
            idf = rIDF(vocab)
            inner_dict[k] = {1:termFreq,2:idf,3:(termFreq*idf)}
            k = k + 1
            #inner_dict[i]=(tf_idf_rapport(vocab,tokens_li[i],tokens_li))
    primaryDictionary[vocab]=inner_dict
#IDF by searching in the vocabulary
#print (primaryDictionary)
#print (len(vocabulary))

with open('savers/dictionary.json', 'w') as fp:
    json.dump(primaryDictionary, fp)
