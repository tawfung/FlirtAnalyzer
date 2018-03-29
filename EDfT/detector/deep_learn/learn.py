from keras.models import Sequential, model_from_json
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
import numpy as np
import tensorflow as tf
from keras import backend as K

class Trainer:
    def __init__(self):
        pass

    def start(self):
        tf_session = tf.Session()
        K.set_session(tf_session)

        data_set = np.loadtxt("detector/preprocessing/vectorization.csv", delimiter=",")
        data_size = len(data_set)

        # Change those according to your needs
        test_data_size = 800
        num_features = 3 # or 5

        # Train Set
        in_vec = data_set[0:(data_size - test_data_size +1), 0:num_features]
        out_vec = data_set[0:(data_size - test_data_size +1), num_features]
        output_vec_categorical = to_categorical(out_vec)

        # Test Set
        test_in_vec = data_set[test_data_size:, 0:num_features]
        test_out_vec = data_set[test_data_size:, num_features]
        test_output_vec_categorical = to_categorical(test_out_vec)

#========================  Model Configuration  ==============================#
        # Stacking 3 layers, so choosing a sequential model
        model = Sequential()
        # The first layer has 3 inputs and 3 outputs
        in_layer = Dense(3, input_dim=3, init='uniform', activation='relu')
        # The second hidden layer has 3 outputs as well
        hid_layer = Dense(3, init='uniform', activation='relu')
        # The third output layer has 3 outputs between [0, 1], that's why a sigmoid activation function was used
        out_layer = Dense(3, init='uniform', activation='sigmoid')

        # Adding the layer to the model
        model.add(in_layer)
        model.add(hid_layer)
        model.add(out_layer)

        # Compile model with loss function for multi-class classification, with the adam algorithm for optimizing
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model_configs = model.to_json()

#=========================  Training The Model  ===============================#
        with tf_session.as_default():
            model.fit(in_vec, output_vec_categorical, nb_epoch=10, batch_size=10)
            model_weights = model.get_weights()

#=========================  Saving model configs and weights  =================#
        with open('configs','w') as cf:
            cf.write(model_configs)
        model.save_weights('weights')

#=========================  Evaluating Model  =================================#
        scores = None
        with tf_session.as_default():
            scores = model.evaluate(test_in_vec,test_output_vec_categorical)
        K.clear_session()

        print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        return scores[1]*100.0
