# import pandas as pd
# import numpy as np
import nltk, re, itertools, csv, os
# os.chdir('/home/enclaveit/SeniorProject/FlirtAnalyzer/EDfT/detector/preprocessing')

# data = pd.read_csv('text_emotion.csv')

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

#filter data
import csv, re
# import numpy as np

fileR = 'text_emotion.csv'
fileWorry = 'worryToken.txt'
fileSadness = 'sadnessToken.txt'
fileHappiness = 'happinessToken.txt'
fileSurprise = 'surpriseToken.txt'

def filterFile(fileRead, fileWrite, key):
    with open(fileWrite, 'w') as outFile:
        fileWriter = csv.writer(outFile)
        with open(fileRead, 'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                subrow = []
                for words in row:
                    word = str(words)
                    w = re.compile('^[0-9]+|http:\S+|^@[a-zA-Z0-9_]+')
                    ww = w.sub('', word)
                    subrow.append(ww)
                    for sr in subrow:
                        if sr == key and len(subrow) > 3:
                            # print(subrow.pop())
                            fileWriter.writerow([subrow.pop()])

filterFile(fileR, fileWorry, "worry")
filterFile(fileR, fileSadness, "sadness")
filterFile(fileR, fileSurprise, "surprise")
filterFile(fileR, fileHappiness, "happiness")
