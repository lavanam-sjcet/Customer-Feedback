#load packages
import tarfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential, Model, model_from_json
from keras.layers import Dense, Conv2D, Activation, MaxPool2D, Flatten, Dropout, BatchNormalization
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
# read csv file 
train = pd.read_csv("fer2013.csv")
#seperates the images data with space
train['pixels'] = train['pixels'].apply(lambda im: np.fromstring(im, sep=' '))
# array conversion train set
x_train = np.vstack(train['pixels'].values)
y_train = np.array(train["emotion"])
#seperates the images data with space
train["pixels"] = train["pixels"].apply(lambda im: np.fromstring(im, sep=' '))
# array conversion train set
x_test = x_train#np.vstack(train["pixels"].values)
y_test = np.array(train["emotion"])
#normalize the dataset
x_train = x_train.reshape(-1, 48, 48, 1)
x_test = x_test.reshape(-1, 48, 48, 1)
#convert the prediction labels into numerical vectors
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
print("dfffffffffff hfffffffffffff fddddddddddddddddddddd ghfffffffff",y_train.shape, y_test.shape)

#convolutional neural network architecture
model = Sequential()
#covolution layers
model.add(Conv2D(64, 3, data_format="channels_last", kernel_initializer="he_normal", 
                 input_shape=(48, 48, 1)))
model.add(BatchNormalization())
model.add(Activation("relu"))

model.add(Conv2D(64, 3))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))
model.add(Dropout(0.6))

model.add(Conv2D(32, 3))
model.add(BatchNormalization())
model.add(Activation("relu"))

model.add(Conv2D(32, 3))
model.add(BatchNormalization())
model.add(Activation("relu"))

model.add(Conv2D(32, 3))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))
model.add(Dropout(0.6))

model.add(Flatten())
model.add(Dense(128))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(Dropout(0.6))

model.add(Dense(7))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()


# save best weights
checkpointer = ModelCheckpoint(filepath='face_model.h5', verbose=1, save_best_only=True)
print("dkj",x_train.shape,y_train.shape,x_test.shape, y_test.shape)
# num epochs
epochs = 10

# run model
hist = model.fit(x_train, y_train, epochs=epochs,
                 shuffle=True,
                 batch_size=100, validation_data=(x_test, y_test),
                 callbacks=[checkpointer], verbose=2)
print("gdfdhfjhj")

# save model to json
model_json = model.to_json()
with open("face_model.json", "w") as json_file:
    json_file.write(model_json)
