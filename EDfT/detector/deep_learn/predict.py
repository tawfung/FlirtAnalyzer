from keras.models import *
import numpy as np
import tensorflow as tf
from keras import backend as K
from nltk.stem import *
import datetime

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

        # with open('detector/data/emotion_lexicon_dic.txt', 'r') as f:
        #     lex_dic = f.read()
        # lex_dic = lex_dic.split('\n')
        # a = 0
        # for x in lex_dic:
        #     lex_dic[a] = x.split(' ')
        #     a += 1
        #
        # # s = LancasterStemmer()
        # s = PorterStemmer()
        #
        # for i in range(0, a - 1):
        #     lex_dic[i][0] = s.stem(lex_dic[i][0])

        # If not self.model:
        self.load_model()
        dataset = np.loadtxt('detector/data/featureVectorForSentence.csv', delimiter=',')
        X = dataset[:-1, :]
        predictions = self.model.predict(X)
        rounded = np.around(predictions, decimals=0)
        total = len(predictions)
        counters = [0, 0, 0]
        c = 1


        with open('detector/data/daily-log.csv', 'a') as daily:

            with tf_session.as_default():
                for x in rounded:
                    if x[0] == 1 and x[1] == 0 and x[2] == 0:
                        counters[0] += 1
                        print("Sentence Number " + str(c) + " is Angry")
                    elif x[0] == 0 and x[1] == 1 and x[2] == 0:
                        counters[1] += 1
                        print("Sentence Number " + str(c) + " is Sad")
                    elif x[0] == 0 and x[1] == 0 and x[2] == 1:
                        counters[2] += 1
                        print("Sentence Number " + str(c) + " is Joy")
                    else:
                        print("Sentence Number " + str(c) + " is Undefined")
                    c += 1
            K.clear_session()

            daily.write(str(datetime.datetime.now()) + ',' + str(total) + ',' + str(counters[0]) + ','
                        + str(counters[1]) + ',' + str(counters[2]) + ',' + str(total-(counters[0]+counters[1]+counters[2])) + '\n')

        results = dict()
        results['predictions'] = predictions
        results['counters'] = counters
        results['total'] = total

        return results
