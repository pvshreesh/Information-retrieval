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
print(docs)

for i in range(len(docs)):
    docs[i] = int(docs[i].split(".")[0])
    print(docs[i])

docs.sort()
print(docs)

def create_tokens_li():
    """
    Function for creating tokens_li and then storing in json file for further usage
    """
    cnt=0
    for file in docs:
        file_name = open("./corpus/"+ str(file) + ".txt")
        print(cnt)
        cnt+=1
        words = file_name.read()
        tokens_doc = nltk.word_tokenize(words)
        tokens_doc = [w.lower() for w in tokens_doc]
        #tokens_doc = [snowball_stemmer.stem(token) for token in tokens_doc]
        tokens_doc = [token for token in tokens_doc if token not in nltk.corpus.stopwords.words('english')]
        tokens_li.append(tokens_doc)


    #storing in json file
    with open('savers/tokens.json', 'w') as fp:
        json.dump(tokens_li, fp)


#caling function
create_tokens_li()
