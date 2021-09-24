from math import log
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
import sys
import math
import os
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import  json

docFiles = [f for f in os.listdir('./corpus') if f.endswith(".txt")]
for i in range(len(docFiles)):
    docFiles[i] = int(docFiles[i].split(".")[0])
    
docFiles.sort()
print(docFiles)
main=[]
for f in docFiles:
    fname = open("./corpus/"+ str(f)+'.txt')
    words=fname.read()
    l=words.split()
    punc = '''!()-[]{;:'"}\, <>./?@#$%^&*_~'''
    words.lower()
    for i in words:
        if i in punc:
            words=words.replace(i," ")
    for i in range(1): 
        text_tokens=word_tokenize(words) 
    tokens_without_sw = [ 
    word for word in text_tokens if not word in stopwords.words()] 
    for i in tokens_without_sw:
        main.append(i)
    set(main)
    list(main)
    fname.close()
dic={}
count=2
for i in docFiles :
    fname = open("./corpus/"+ str(i)+'.txt')
    words=fname.read()
    for item in main:
        if item in words:

            if item not in dic:
                dic[item]=[]
            if item in dic:
                dic[item].append(i)
                set(dic[item])
                list(dic[item])
    fname.close()
print(dic)
with open('savers/ii.json', 'w') as fp:
        json.dump(dic, fp)
