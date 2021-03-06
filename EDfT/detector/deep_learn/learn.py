from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
import numpy as np
import tensorflow as tf
from keras import backend as K
import os

class Trainer:
    def __init__(self):
        pass

    def start(self):
        tf_session = tf.Session()
        K.set_session(tf_session)

        data_set = np.loadtxt("detector/data/vectorization.csv", delimiter=",")

        # # Train Set
        #
        inp_vec = data_set[:, 0:10]
        out_vec = data_set[:, 10:]
        output_vec_categorical = to_categorical(out_vec)

        # # Test Set
        #
        test_in_vec = data_set[0:200, 0:10]
        test_out_vec = data_set[0:200, 10:]
        test_output_vec_categorical = to_categorical(test_out_vec)

# ========================  Model Configuration  ==============================#
        # Stacking 3 layers, so choosing a sequential model
        model = Sequential()
        # The first layer has 10 inputs and 100 outputs
        inp_layer = Dense(output_dim=100, init='uniform', activation='relu', input_dim=10)
        # The second hidden layer has 100 inputs and outputs as well
        hid_layer = Dense(output_dim=100, init='uniform', activation='relu', input_dim=100)
        # The third output layer has 3 outputs, that's why a softmax activation function was used
        out_layer = Dense(output_dim=3, init='uniform', activation='softmax', input_dim=100)

        # Adding the layer to the model
        model.add(inp_layer)
        model.add(hid_layer)
        model.add(out_layer)

        # Compile model with loss function for multi-class classification, with the adam algorithm for optimizing
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model_configs = model.to_json()

# =========================  Training The Model  ===============================#
        with tf_session.as_default():
            model.fit(inp_vec, output_vec_categorical, nb_epoch=1000, batch_size=10)
            # model_weights = model.get_weights()

# =========================  Saving model configs and weights  =================#
        if not os.path.isfile('detector/deep_learn/configs'):
            open('detector/deep_learn/configs', 'w')
        with open('detector/deep_learn/configs', 'w') as cf:
            cf.write(model_configs)
        model.save_weights('detector/deep_learn/weights')

# =========================  Evaluating Model  =================================#
        with tf_session.as_default():
            scores = model.evaluate(test_in_vec, test_output_vec_categorical)
        K.clear_session()

        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        return scores[1]*100.0


