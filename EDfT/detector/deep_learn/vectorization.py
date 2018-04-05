from nltk import *
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

#
class Vectorizer:
#
#     def __init__(self):
#         self.hashTable = {}
#
#         self.angryVectors = []
#         self.disgustVectors = []
#         self.joyVectors = []
#         # self.sadnessVectors = []
#         # self.surpriseVectors = []
#         # self.neutralVectors = []
#
#
    def processTokenFile(self, fileName, token):
        with open("detector/deep_learn/emotion_lexicon_dic.txt", 'r') as f:
            lex_dic = f.read()
            lex_dic = lex_dic.split("\n")
            a = 0
            for x in lex_dic:
                lex_dic[a] = x.split(' ')
                a += 1

                stemmer = LancasterStemmer()
                for i in range(0, a-1):
                    lex_dic[i][0] = stemmer.stem(lex_dic[i][0])
        with open(fileName,'r') as f:
            token = f.read()
        sentenceTokens = sent_tokenize(token)
        unwantedWords = ['the' , 'a', 'is' , 'was' , 'are',
                          'were' , 'to', 'at', 'i' , 'my',
                          'on' , 'me'  , 'of' , '.' , 'in' ,
                          'that' , 'he' , 'she' , 'it' , 'by']

        if not os.path.isfile('detector/deep_learn/vectorization.csv'):
            open('detector/deep_learn/vectorization.csv','w')
        with open('detector/deep_learn/vectorization.csv','w') as vectorsFile:
            vectorsFile.write('')

        for x in sentenceTokens:
            featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 dimension
            words = word_tokenize(x)
            for y in words:
                y = stemmer.stem(y)
                y = y.lower()
                if y in unwantedWords != -1:
                    continue
                for i in range(0, a-1):
                    if y == lex_dic[i][0]:
                        for j in range(0,10):
                            featureVector[j] = featureVector[j] + int(lex_dic[i][j+1])
                        break
            featureVector.append(0)

            # write to detector/deep_learn/vectorization.csv file
            for k in range(0,10):
                with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
                    vectorsFile.write(str(featureVector[k]) + ',')
            with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
                vectorsFile.write(str(featureVector[10]) + '\n')

        with open('detector/deep_learn/vectorization.csv','r') as f:
            features = f.read()
        features = features.split('\n')
        with open('detector/deep_learn/vectorization.csv','w') as vectorsFile:
            vectorsFile.write('')

        for i in range(0,1040):
            with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
                vectorsFile.write(features[i] + '\n')
                vectorsFile.write(features[i+1040] + '\n')
                vectorsFile.write(features[3117-i] + '\n')

        pass


    def vectorize(self, sentences):
        if not os.path.isfile('detector/deep_learn/featureVectorForSentence.csv'):
            open('detector/deep_learn/featureVectorForSentence.csv' , 'w')
        with open('detector/deep_learn/featureVectorForSentence.csv', 'w') as featuresFile:
            featuresFile.write('')

        s = LancasterStemmer()

        with open("detector/deep_learn/emotion_lexicon_dic.txt", 'r') as f:
            lex_dic = f.read()
            lex_dic = lex_dic.split("\n")
            a = 0
            for x in lex_dic:
                lex_dic[a] = x.split(' ')
                a += 1

        for i in range(0, a-1):
            lex_dic[i][0] = s.stem(lex_dic[i][0])


        unwantedWords = ['the' , 'a', 'is' , 'was' , 'are',
                          'were' , 'to', 'at', 'i' , 'my',
                          'on' , 'me'  , 'of' , '.' , 'in' ,
                          'that' , 'he' , 'she' , 'it' , 'by']


        listOfVectors = []

        for x in sentences:
            featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            words = word_tokenize(x)
            for y in words :
                y = s.stem(y)
                y = y.lower()
                if y in unwantedWords != -1:
                    continue
                for i in range(0, a - 1):
                    if y == lex_dic[i][0]:
                        for j in range(0, 10):
                            featureVector[j] = featureVector[j] + int (lex_dic[i][j + 1])
                        break
            # write this feature vector to featureVectors File
            for k in range (0, 9):
                with open('detector/deep_learn/featureVectorForSentence.csv', 'a') as featuresFile:
                    featuresFile.write(str(featureVector[k]) + ',')
            with open('detector/deep_learn/featureVectorForSentence.csv', 'a') as featuresFile:
                featuresFile.write(str(featureVector[9]) + '\n')
        # to avoid one Sentence Error
        for k in range (0, 9):
            with open('detector/deep_learn/featureVectorForSentence.csv', 'a') as featuresFile:
                    featuresFile.write(str(featureVector[k]) + ',')
        with open('detector/deep_learn/featureVectorForSentence.csv', 'a') as featuresFile:
            featuresFile.write(str(featureVector[9]) + '\n')

        return np.loadtxt("detector/deep_learn/featureVectorForSentence.csv", delimiter=",")

    def start(self, mode='train', text=None):

        if mode == 'train':
            self.processTokenFile('detector/deep_learn/angryTokens.txt',0)
            self.processTokenFile('detector/deep_learn/disgustTokens.txt',1)
            self.processTokenFile('detector/deep_learn/joyTokens.txt',2)
            # self.readTokenFile('detector/preprocessing/worryTokens.txt')
            # self.readTokenFile('detector/preprocessing/sadnessTokens.txt')
            # self.readTokenFile('detector/preprocessing/happinessTokens.txt')

        else:
            sentences = sent_tokenize(text)
            return self.vectorize(sentences)


# class Vectorizer:
# if __name__ == '__main__':
#
#     with open('detector/deep_learn/angryTokens.txt','r') as f:
#         angry = f.read()
#     angrySentences = sent_tokenize(angry)
#
#     with open('detector/deep_learn/disgustTokens.txt','r') as f:
#         disgust = f.read()
#     disgustSentences = sent_tokenize(disgust)
#
#     with open('detector/deep_learn/joyTokens.txt','r') as f:
#         joy = f.read()
#     joySentences = sent_tokenize(joy)
#
#     with open('detector/deep_learn/emotion_lexicon_dic.txt','r') as f:
#         lex_dic = f.read()
#     lex_dic = lex_dic.split('\n')
#     a = 0
#     for x in lex_dic:
#         lex_dic[a] = x.split(' ')
#         a += 1
#     stemmer = LancasterStemmer()
#     unwantedWords = ['the' , 'a', 'is' , 'was' , 'are',
#                       'were' , 'to', 'at', 'i' , 'my',
#                       'on' , 'me'  , 'of' , '.' , 'in' ,
#                       'that' , 'he' , 'she' , 'it' , 'by']
#     if not os.path.isfile('detector/deep_learn/vectorization.csv'):
#         open('detector/deep_learn/vectorization.csv','w')
#     with open('detector/deep_learn/vectorization.csv','w') as vectorsFile:
#         vectorsFile.write('')
#
#     for i in range(0, a-1):
#         lex_dic[i][0] = stemmer.stem(lex_dic[i][0])
#
#     # Create feature vector to each sentence in angryTokens.txt file
#     for x in angrySentences:
#         featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 dimension
#         words = word_tokenize(x)
#         for y in words:
#             y = stemmer.stem(y)
#             y = y.lower()
#             if y in unwantedWords != -1:
#                 continue
#             for i in range(0, a-1):
#                 if y == lex_dic[i][0]:
#                     for j in range(0,10):
#                         featureVector[j] = featureVector[j] + int(lex_dic[i][j+1])
#                     break
#         featureVector.append(0)
#
#         # write to detector/deep_learn/vectorization.csv file
#         for k in range(0,10):
#             with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
#                 vectorsFile.write(str(featureVector[k]) + ',')
#         with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
#             vectorsFile.write(str(featureVector[10]) + '\n')
#
#     # Create feature vector to each sentence in disgustTokens.txt file
#     for x in disgustSentences:
#         featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 dimension
#         words = word_tokenize(x)
#         for y in words:
#             y = stemmer.stem(y)
#             y = y.lower()
#             if y in unwantedWords != -1:
#                 continue
#             for i in range(0, a-1):
#                 if y == lex_dic[i][0]:
#                     for j in range(0,10):
#                         featureVector[j] = featureVector[j] + int(lex_dic[i][j+1])
#                     break
#         featureVector.append(1)
#
#         # write to detector/deep_learn/vectorization.csv file
#         for k in range(0,10):
#             with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
#                 vectorsFile.write(str(featureVector[k]) + ',')
#         with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
#             vectorsFile.write(str(featureVector[10]) + '\n')
#
#     # Create feature vector to each sentence in joyTokens.txt file
#     for x in joySentences:
#         featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 dimension
#         words = word_tokenize(x)
#         for y in words:
#             y = stemmer.stem(y)
#             y = y.lower()
#             if y in unwantedWords != -1:
#                 continue
#             for i in range(0, a-1):
#                 if y == lex_dic[i][0]:
#                     for j in range(0,10):
#                         featureVector[j] = featureVector[j] + int(lex_dic[i][j+1])
#                     break
#         featureVector.append(2)
#
#         # write to detector/deep_learn/vectorization.csv file
#         for k in range(0,10):
#             with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
#                 vectorsFile.write(str(featureVector[k]) + ',')
#         with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
#             vectorsFile.write(str(featureVector[10]) + '\n')
#
#     with open('detector/deep_learn/vectorization.csv','r') as f:
#         features = f.read()
#     features = features.split('\n')
#     with open('detector/deep_learn/vectorization.csv','w') as vectorsFile:
#         vectorsFile.write('')
#
#     for i in range(0,1040):
#         with open('detector/deep_learn/vectorization.csv','a') as vectorsFile:
#             vectorsFile.write(features[i] + '\n')
#             vectorsFile.write(features[i+1040] + '\n')
#             vectorsFile.write(features[3117-i] + '\n')
#
#     pass
