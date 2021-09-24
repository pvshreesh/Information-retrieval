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
docFiles = [f for f in os.listdir('./corpus') if f.endswith(".txt")]
docFiles.sort()


def voc_comp():
    """
    Function for retreiving the tokens_li for creating the vocabulary,then storing the vocabulary in a json file
    """
    with open('./savers/tokens.json') as json_data:
        tokens_li = json.load(json_data)

    for document_tokens in tokens_li:
        voc_construct(document_tokens)
        
    with open('savers/words.json', 'w') as fp:
        json.dump(vocabulary, fp)

def voc_construct(document_tokens):
        """
        Function for building the vocabulary i.e. the dictionary which has all the unique words in the corpus
        """
        count=0

        vocabulary_index=len(vocabulary)-1
        for word in document_tokens: # accsessing words in document tokens list
                if word not in vocabulary:
                            print(count)
                            count+=1
                            vocabulary[word] = vocabulary_index
                            vocabulary_index+= 1

voc_comp()


