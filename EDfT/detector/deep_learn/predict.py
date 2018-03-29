from keras.models import *
import numpy as np
import tensorflow as tf
from keras import backend as K

class Classifier:
    def __init__(self):
        self.model = None

    def load_model(self):
        f = open('configs', 'r')
        cfg = f.read()
        f.close()
        self.model = model_from_json(cfg)  #TODO: create weights file first
        self.model.load_weights('weights') 
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return self.model

    def start(self, vectors):
        tf_session = tf.Session()
        K.set_session(tf_session)

        # If not self.model:
        self.load_model()
        predictions = []
        counters = [0,0,0]

        with tf_session.as_default():
            for result in self.model.predict(np.array(vectors)):
                print(result)
                if result[0] > result[1] and result[0] > result[2]:
                    predictions.append(0)
                    counters[0] += 1
                elif result[1] > result[0] and result[1] > result[2]:
                    predictions.append(1)
                    counters[1] += 1
                else:
                    predictions.append(2)
                    counters[2] += 1

        K.clear_session()

        total = len(predictions)

        results = dict()
        results['predictions'] = predictions
        results['counters'] = counters
        results['total'] = total
        return results
