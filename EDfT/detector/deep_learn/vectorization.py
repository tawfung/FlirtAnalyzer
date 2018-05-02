from nltk import *
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

#
class Vectorizer:
#
    def __init__(self):
#         self.hashTable = {}
#
#         self.angryVectors = []
#         self.disgustVectors = []
#         self.joyVectors = []
#         self.sadnessVectors = []
#         self.surpriseVectors = []
#         self.neutralVectors = []
        pass

    # def processTokenFile(self, fileName, token):
    #     stemmer = LancasterStemmer()
    #     with open("detector/deep_learn/emotion_lexicon_dic.txt", 'r') as f:
    #         lex_dic = f.read()
    #     lex_dic = lex_dic.split("\n")
    #     a = 0
    #
    #     for x in lex_dic:
    #         lex_dic[a] = x.split(' ')
    #         a += 1
    #
    #     for i in range(0, a-1):
    #         lex_dic[i][0] = stemmer.stem(lex_dic[i][0])
    #
    #     unwantedWords = ['the', 'a', 'is', 'was', 'are',
    #                       'were', 'to', 'at', 'i', 'my',
    #                       'on', 'me', 'of', '.', 'in',
    #                       'that', 'he', 'she', 'it', 'by']
    #
    #     with open(fileName, 'r') as f:
    #         sentence = f.read()
    #     sentenceTokens = sent_tokenize(sentence)
    #
    #     if not os.path.isfile('detector/deep_learn/vectorization.csv'):
    #         open('detector/deep_learn/vectorization.csv', 'w')
    #     with open('detector/deep_learn/vectorization.csv', 'w') as vectorsFile:
    #             vectorsFile.write('')
    #
    #     for x in sentenceTokens:
    #         featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 dimension
    #         words = word_tokenize(x)
    #         for y in words:
    #             y = stemmer.stem(y)
    #             y = y.lower()
    #             if y in unwantedWords != -1:
    #                 continue
    #             for i in range(0, a-1):
    #                 if y == lex_dic[i][0]:
    #                     for j in range(0, 10):
    #                         featureVector[j] = featureVector[j] + int(lex_dic[i][j+1])
    #                     break
    #         featureVector.append(token)
    #
    #         # write to detector/deep_learn/vectorization.csv file
    #         for k in range(0, 10):
    #             with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
    #                 vectorsFile.write(str(featureVector[k]) + ',')
    #         with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
    #             vectorsFile.write(str(featureVector[10]) + '\n')
    #
    #     # pass
    #
    # def writeVectors2File(self):
    #
    #     with open('detector/deep_learn/vectorization.csv', 'r') as f:
    #         features = f.read()
    #     features = features.split('\n')
    #     with open('detector/deep_learn/vectorization.csv', 'w') as vectorsFile:
    #             vectorsFile.write('')
    #
        # for i in range(0, 1040):
        #     with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
        #         vectorsFile.write(features[i] + '\n')
        #         vectorsFile.write(features[i + 1040] + '\n')
        #         vectorsFile.write(features[3117 - i] + '\n')
        # pass


    def processTokenFile(self):
        # stemmer = LancasterStemmer()
        stemmer = PorterStemmer()
        with open("detector/deep_learn/emotion_lexicon_dic.txt", 'r') as f:
            lex_dic = f.read()
        lex_dic = lex_dic.split("\n")
        a = 0

        for x in lex_dic:
            lex_dic[a] = x.split(' ')
            a += 1

        for i in range(0, a - 1):
            lex_dic[i][0] = stemmer.stem(lex_dic[i][0])

        unwantedWords = ['the', 'a', 'is', 'was', 'are',
                         'were', 'to', 'at', 'i', 'my',
                         'on', 'me', 'of', '.', 'in',
                         'that', 'he', 'she', 'it', 'by']

        if not os.path.isfile('detector/deep_learn/vectorization.csv'):
            open('detector/deep_learn/vectorization.csv', 'w')
        with open('detector/deep_learn/vectorization.csv', 'w') as vectorsFile:
            vectorsFile.write('')

        # Tokenize angryTokens.txt file
        with open('detector/deep_learn/angryTokens.txt', 'r') as f:
            angry = f.read()
        angryTokens = sent_tokenize(angry)

        for x in angryTokens:
            featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 dimensions
            words = word_tokenize(x)
            for word in words:
                word = stemmer.stem(word)
                word = word.lower()
                if word in unwantedWords != -1:
                    continue
                elif word[-1] == 'i':
                    word = list(word)
                    word[-1] = 'y'
                    word = ''.join(word)
                for i in range(0, a - 1):
                    if word == lex_dic[i][0]:
                        for j in range(0, 10):
                            featureVector[j] = featureVector[j] + int(lex_dic[i][j + 1])
                        break
            featureVector.append(0)

            # write to detector/deep_learn/vectorization.csv file
            for k in range(0, 10):
                with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
                    vectorsFile.write(str(featureVector[k]) + ',')
            with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
                vectorsFile.write(str(featureVector[10]) + '\n')

        # Tokenize disgustTokens.txt file
        with open('detector/deep_learn/sadnessTokens.txt', 'r') as f:
            sad = f.read()
        sadTokens = sent_tokenize(sad)

        for x in sadTokens:
            featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 dimensions
            words = word_tokenize(x)
            for word in words:
                word = stemmer.stem(word)
                word = word.lower()
                if word in unwantedWords != -1:
                    continue
                elif word[-1] == 'i':
                    word = list(word)
                    word[-1] = 'y'
                    word = ''.join(word)
                for i in range(0, a - 1):
                    if word == lex_dic[i][0]:
                        for j in range(0, 10):
                            featureVector[j] = featureVector[j] + int(lex_dic[i][j + 1])
                        break
            featureVector.append(1)

            # write to detector/deep_learn/vectorization.csv file
            for k in range(0, 10):
                with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
                    vectorsFile.write(str(featureVector[k]) + ',')
            with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
                vectorsFile.write(str(featureVector[10]) + '\n')

        # Tokenize joyTokens.txt file
        with open('detector/deep_learn/joyTokens.txt', 'r') as f:
            joy = f.read()
        joyTokens = sent_tokenize(joy)

        for x in joyTokens:
            featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 dimensions
            words = word_tokenize(x)
            for word in words:
                word = stemmer.stem(word)
                word = word.lower()
                if word in unwantedWords != -1:
                    continue
                elif word[-1] == 'i':
                    word = list(word)
                    word[-1] = 'y'
                    word = ''.join(word)
                for i in range(0, a - 1):
                    if word == lex_dic[i][0]:
                        for j in range(0, 10):
                            featureVector[j] = featureVector[j] + int(lex_dic[i][j + 1])
                        break
            featureVector.append(2)

            # write to detector/deep_learn/vectorization.csv file
            for k in range(0, 10):
                with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
                    vectorsFile.write(str(featureVector[k]) + ',')
            with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
                vectorsFile.write(str(featureVector[10]) + '\n')


        with open('detector/deep_learn/vectorization.csv', 'r') as f:
            features = f.read()
        features = features.split('\n')
        with open('detector/deep_learn/vectorization.csv', 'w') as vectorsFile:
            vectorsFile.write('')

        for i in range(0, 1040):
            with open('detector/deep_learn/vectorization.csv', 'a') as vectorsFile:
                vectorsFile.write(features[i] + '\n')
                vectorsFile.write(features[i + 1040] + '\n')
                vectorsFile.write(features[3117 - i] + '\n')

    def vectorize(self, sentences):
        # s = LancasterStemmer()
        s = PorterStemmer()
        with open("detector/deep_learn/emotion_lexicon_dic.txt", 'r') as f:
            lex_dic = f.read()
        lex_dic = lex_dic.split("\n")
        a = 0
        for x in lex_dic:
            lex_dic[a] = x.split(' ')
            a += 1

        for i in range(0, a-1):
            lex_dic[i][0] = s.stem(lex_dic[i][0])

        unwantedWords = ['the', 'a', 'is', 'was', 'are',
                         'were', 'to', 'at', 'i', 'my',
                         'on', 'me', 'of', '.', 'in',
                         'that', 'he', 'she', 'it', 'by']
        if not os.path.isfile('detector/deep_learn/featureVectorForSentence.csv'):
            open('detector/deep_learn/featureVectorForSentence.csv', 'w')
        with open('detector/deep_learn/featureVectorForSentence.csv', 'w') as featuresFile:
            featuresFile.write('')

        for x in sentences:
            featureVector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            words = word_tokenize(x)
            for word in words:
                word = s.stem(word)
                word = word.lower()
                if word in unwantedWords != -1:
                    continue
                elif word[-1] == 'i':
                    word = list(word)
                    word[-1] = 'y'
                    word = ''.join(word)
                for i in range(0, a - 1):
                    if word == lex_dic[i][0]:
                        for j in range(0, 10):
                            featureVector[j] = featureVector[j] + int(lex_dic[i][j + 1])
                        break
            # write this feature vector to featureVectors File
            for k in range(0, 9):
                with open('detector/deep_learn/featureVectorForSentence.csv', 'a') as featuresFile:
                    featuresFile.write(str(featureVector[k]) + ',')
            with open('detector/deep_learn/featureVectorForSentence.csv', 'a') as featuresFile:
                featuresFile.write(str(featureVector[9]) + '\n')
        # to avoid one Sentence Error
        for k in range(0, 9):
            with open('detector/deep_learn/featureVectorForSentence.csv', 'a') as featuresFile:
                featuresFile.write(str(featureVector[k]) + ',')
        with open('detector/deep_learn/featureVectorForSentence.csv', 'a') as featuresFile:
            featuresFile.write(str(featureVector[9]) + '\n')

        return np.loadtxt("detector/deep_learn/featureVectorForSentence.csv", delimiter=",")

    def start(self, mode='train', text=None):

        if mode == 'train':
            # self.processTokenFile('detector/deep_learn/angryTokens.txt', 0)
            # self.processTokenFile('detector/deep_learn/disgustTokens.txt', 1)
            # self.processTokenFile('detector/deep_learn/joyTokens.txt', 2)
            # self.processTokenFile('detector/deep_learn/sadnessTokens.txt', 3)
            # self.processTokenFile('detector/deep_learn/shameTokens.txt', 4)

            # self.writeVectors2File()

            self.processTokenFile()

        else:
            sentences = sent_tokenize(text)
            return self.vectorize(sentences)
