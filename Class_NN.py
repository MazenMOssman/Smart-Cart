from keras.layers import Dense, Flatten, Dropout
from keras.applications import VGG16
from keras import models
import numpy as np
# Create a class for neural network with same number of parameters
class NN:
    def __init__(self):
      # import the convolutional base model (VGG16 in this case)
        self.conv_base = VGG16(weights='imagenet',
                          input_shape=(500, 500, 3),
                          include_top=False)
        self.model = models.Sequential()
        self.model.add(self.conv_base)
      # Flatten the output to prepare it for dense 2d dot product.
        self.model.add(Flatten())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(512, activation='relu'))
        self.model.add(Dense(5, activation='softmax'))
      # Set last convolution block trainable only and the rest are frozen
        self.conv_base.trainable = True
        set_trainable = False
        for layer in self.conv_base.layers:
            if layer.name == 'block5_conv1':
                set_trainable = True
            if set_trainable:
                layer.trainable = True
            else:
                layer.trainable = False
        # load the model
        self.model.load_weights("resource\graduationtestv2.5.1Accepted.h5")
        print(self.model.summary())
    # this method used to receive the image and get us a result if the model is 98% sure of the product
    def run_NN(self,image):
        assert image.shape == (500, 500, 3)
        dat = image * 1./ 255
        data = dat.reshape(1, dat.shape[0], dat.shape[1], dat.shape[2])
        if np.max(self.model.predict(data) > 0.98) :
            self.flag = True
            if self.flag == True:
                return np.argmax(self.model.predict(data)),np.max(self.model.predict(data)),self.model.predict(data),self.model.predict_classes(data),self.flag
        else:
            self.flag = False
            return np.argmax(self.model.predict(data)),np.max(self.model.predict(data)),self.flag,self.model.predict(data),self.model.predict_classes(data)
