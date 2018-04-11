from keras.models import *
import numpy as np
import tensorflow as tf
from keras import backend as K
from nltk.stem import LancasterStemmer, PorterStemmer

class Classifier:
    def __init__(self):
        self.model = None

    def load_model(self):
        f = open('detector/deep_learn/configs', 'r')
        cfg = f.read()
        f.close()
        self.model = model_from_json(cfg)
        self.model.load_weights('detector/deep_learn/weights')
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return self.model

    def start(self, vectors):
        tf_session = tf.Session()
        K.set_session(tf_session)

        with open('detector/deep_learn/emotion_lexicon_dic.txt','r') as f:
            lex_dic = f.read()
        lex_dic = lex_dic.split('\n')
        a = 0
        for x in lex_dic:
            lex_dic[a] = x.split(' ')
            a += 1
        # with open('test.txt','r') as f:
        #     sentence = f.read()
        # sentences = self.model.sent_tokenize(sentence)

        # s = LancasterStemmer()
        s = PorterStemmer()
        # unwantedWords = ['the' , 'a', 'is' , 'was' , 'are',
        #                   'were' , 'to', 'at', 'i' , 'my',
        #                   'on' , 'me'  , 'of' , '.' , 'in' ,
        #                   'that' , 'he' , 'she' , 'it' , 'by']
        for i in range(0, a - 1):
            lex_dic[i][0] = s.stem(lex_dic[i][0])

        # If not self.model:
        self.load_model()
        dataset = np.loadtxt('detector/deep_learn/featureVectorForSentence.csv', delimiter=',')
        X = dataset[:-1, :]
        predictions = self.model.predict(X)
        rounded = np.around(predictions, decimals=0)
        # counters = [0,0,0,0,0]
        counters = [0, 0, 0]
        c = 1

        # with tf_session.as_default():
        #     for x in rounded:
        #         if x[0] == 1 and x[1] == 0 and x[2] == 0 and x[3] == 0 and x[4] == 0:
        #             counters[0] += 1
        #             print("Sentence Number " + str(c) + " is Angry")
        #         elif x[0] == 0 and x[1] == 1 and x[2] == 0 and x[3] == 0 and x[4] == 0:
        #             counters[1] += 1
        #             print("Sentence Number " + str(c) + " is Disgust")
        #         elif x[0] == 0 and x[1] == 0 and x[2] == 1 and x[3] == 0 and x[4] == 0:
        #             counters[2] += 1
        #             print("Sentence Number " + str(c) + " is Joy")
        #         elif x[0] == 0 and x[1] == 0 and x[2] == 0 and x[3] == 1 and x[4] == 0:
        #             counters[3] += 1
        #             print("Sentence Number " + str(c) + " is Sad")
        #         elif x[0] == 0 and x[1] == 0 and x[2] == 0 and x[3] == 0 and x[4] == 1:
        #             counters[4] += 1
        #             print("Sentence Number " + str(c) + " is Shame")
        #         c += 1
        with tf_session.as_default():
            for x in rounded:
                if x[0] == 1 and x[1] == 0 and x[2] == 0:
                    counters[0] += 1
                    print("Sentence Number " + str(c) + " is Angry")
                elif x[0] == 0 and x[1] == 1 and x[2] == 0:
                    counters[1] += 1
                    print("Sentence Number " + str(c) + " is Disgust")
                elif x[0] == 0 and x[1] == 0 and x[2] == 1:
                    counters[2] += 1
                    print("Sentence Number " + str(c) + " is Joy")

                c += 1

        K.clear_session()

        total = len(predictions)

        results = dict()
        results['predictions'] = predictions
        results['counters'] = counters
        results['total'] = total
        return results

        print (results)
