import sys
import glob
import os
from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import json
import scoring
from scoring import main_class

query=input("Enter any dailogue:\n")
result=main_class.proc_func(query)
print('------------')
print('given dailogue is from the following pages')
for i in result:
    print(i)
    