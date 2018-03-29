import random
import nltk
from numpy import array
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer

class Vectorizer:

    def __init__(self):
        self.hashTable = {}

        self.angryVectors = []
        self.disgustVectors = []
        self.joyVectors = []
        # self.sadnessVectors = []
        # self.surpriseVectors = []
        # self.neutralVectors = []

    def readLexiconDictionary(self):
        with open("detector/preprocessing/emotion_lexicon_dic.txt") as f:
            l = f.readlines()
            for i in l:
                l2 = i.split(' ',1)
                l3 = l2[1].split()
                self.hashTable[l2[0]] = []

                self.hashTable[l2[0]].append(int(l3[0])) #anger
                self.hashTable[l2[0]].append(int(l3[2])) #dusgust
                self.hashTable[l2[0]].append(int(l3[4])) #joy
                # self.hashTable[l2[0]].append(int(l3[7])) #sadness
                # self.hashTable[l2[0]].append(int(l3[8])) #surprise

    def readTokenFile(self, fileName, token):
        tokenFile = open(fileName,"r")
        tokenFileContent = tokenFile.read().decode('utf-8')
        sentenceTokens = nltk.sent_tokenize(tokenFileContent)

        for i in sentenceTokens:
            sentenceVector = []
            if token == 0:
                sentenceVector = [2+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0]
            elif token == 1:
                sentenceVector = [0.1+random.uniform(0.1,0.2),2+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),1]
            else:
                sentenceVector = [0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),2+random.uniform(0.1,0.2),2]
        #Add code for sadnessVectors and surpriseVectors here --
        # for i in sentenceTokens:
        #     sentenceVector = []
        #     if token == 0:
        #         sentenceVector = [2+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0]
        #     elif token == 1:
        #         sentenceVector = [0.1+random.uniform(0.1,0.2),2+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),1]
        #     elif token == 2:
        #         sentenceVector = [0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),2+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),2]
        #     elif token == 3:
        #         sentenceVector = [0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),2+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),3]
        #     elif token == 4:
        #         sentenceVector = [0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),0.1+random.uniform(0.1,0.2),2+random.uniform(0.1,0.2),4]

            wordTokens = nltk.word_tokenize(i)
            stemmer = PorterStemmer()

            for j in wordTokens:
                jj = j.lower()
                if jj in self.hashTable:
                    for k in range(3):
                        sentenceVector[k] += self.hashTable[jj][k]
                else:
                    wordStem = stemmer.stem(jj)
                    if wordStem[-1] == 'i':  #The stemmer strangely change 'y' to 'i'. It's not usual in English
                        wordStem = list(wordStem)
                        wordStem[-1] = 'y'
                        wordStem = ''.join(wordStem)
                    # if self.hashTable.has_key(wordStem):
                    if wordStem in self.hashTable:
                        for k in range(3):
                            sentenceVector[k] += self.hashTable[wordStem][k]

            if token == 0:
                self.angryVectors.append(sentenceVector)
            elif token == 1:
                self.disgustVectors.append(sentenceVector)
            else:
                self.joyVectors.append(sentenceVector)
            # elif token == 2:
            #     self.joyVectors.append(sentenceVector)
            # elif token == 3:
            #     self.sadnessVectors.append(sentenceVector)
            # else:
            #     self.surpriseVectors.append(sentenceVector)

    def writeVectorsToFile(self):
        f = open('detector/preprocessing/vectorization.csv','w')
        maximumSize = max(len(self.angryVectors), len(self.disgustVectors), len(self.joyVectors))

        for i in range(maximumSize):
            if i < len(self.angryVectors):
                vectorLengthMinusOne = len(self.angryVectors[i])-1
                for j in range(vectorLengthMinusOne):
                    f.write(str(self.angryVectors[i][j]))
                    f.write(',')
                f.write(str(self.angryVectors[i][-1]+'\n'))
            if i < len(self.disgustVectors):
                vectorLengthMinusOne = len(self.disgustVectors[i])-1
                for j in range(vectorLengthMinusOne):
                    f.write(str(self.disgustVectors[i][j]))
                    f.write(',')
                f.write(str(self.disgustVectors[i][-1]+'\n'))
            if i < len(self.joyVectors):
                vectorLengthMinusOne = len(self.joyVectors[i])-1
                for j in range(vectorLengthMinusOne):
                    f.write(str(self.joyVectors[i][j]))
                    f.write(',')
                f.write(str(self.joyVectors[i][-1]+'\n'))
            # if i < len(self.worryVectors):
            #     vectorLengthMinusOne = len(self.worryVectors[i])-1
            #     for j in range(vectorLengthMinusOne):
            #         f.write(str(self.worryVectors[i][j]))
            #         f.write(',')
            #     f.write(str(self.worryVectors[i][-1]+'\n'))
            # if i < len(self.sadnessVectors):
            #     vectorLengthMinusOne = len(self.sadnessVectors[i])-1
            #     for j in range(vectorLengthMinusOne):
            #         f.write(str(self.sadnessVectors[i][j]))
            #         f.write(',')
            #     f.write(str(self.sadnessVectors[i][-1]+'\n'))
            # if i < len(self.surpriseVectors):
            #     vectorLengthMinusOne = len(self.surpriseVectors[i])-1
            #     for j in range(vectorLengthMinusOne):
            #         f.write(str(self.surpriseVectors[i][j]))
            #         f.write(',')
            #     f.write(str(self.surpriseVectors[i][-1]+'\n'))
            # if i < len(self.neutralVectors):
            #     vectorLengthMinusOne = len(self.neutralVectors[i])-1
            #     for j in range(vectorLengthMinusOne):
            #         f.write(str(self.neutralVectors[i][j]))
            #         f.write(',')
            #     f.write(str(self.neutralVectors[i][-1]+'\n'))

    def vectorize(self, sentences):
        listOfVectors = []

        for i in sentences:
            sentenceVector = [random.uniform(0.1,0.2),random.uniform(0.1,0.2),random.uniform(0.1,0.2)]
            wordTokens = nltk.word_tokenize(i)
            stemmer = PorterStemmer()

            for j in wordTokens:
                jj = j.lower()
                # if self.hashTable.has_key(jj):
                if jj in self.hashTable:
                    for k in range(3):
                        sentenceVector[k] += self.hashTable[jj][k]
                else:
                    wordStem = stemmer.stem(jj)
                    if wordStem[-1] == 'i':
                        wordStem = list(wordStem)
                        wordStem[-1] == 'y'
                        wordStem = ''.join(wordStem)

                    # if self.hashTable.has_key(wordStem):
                    if wordStem in self.hashTable:
                        for k in range(3):
                            sentenceVector[k] += self.hashTable[wordStem][k]
            listOfVectors.append(sentenceVector)
        return listOfVectors

    def start(self, mode='train', text=None):
        self.readLexiconDictionary()

        if mode == 'train':
            self.readTokenFile('detector/preprocessing/angryTokens.txt',0)
            self.readTokenFile('detector/preprocessing/disgustTokens.txt',1)
            self.readTokenFile('detector/preprocessing/joyTokens.txt',2)
            # self.readTokenFile('detector/preprocessing/worryTokens.txt')
            # self.readTokenFile('detector/preprocessing/sadnessTokens.txt')
            # self.readTokenFile('detector/preprocessing/happinessTokens.txt')

            self.writeVectorsToFile()
        else:
            sentences = nltk.sent_tokenize(text)
            return self.vectorize(sentences)
