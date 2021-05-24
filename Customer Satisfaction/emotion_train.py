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
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import pickle



train = pd.read_csv("fer2013.csv")
#seperates the images data with space
train['pixels'] = train['pixels'].apply(lambda im: np.fromstring(im, sep=' '))

x_train = np.vstack(train['pixels'].values)
print("In for loop")

# array conversion train set
print("exit for loop")
y_train = np.array(train["emotion"])
#seperates the images data with space
train["pixels"] = train["pixels"].apply(lambda im: np.fromstring(im, sep=' '))
# array conversion train set

x_test = np.vstack(train["pixels"].values)

y_test = np.array(train["emotion"])
#normalize the dataset
x_train = x_train.reshape(-1, 48, 48, 1)
x_test = x_test.reshape(-1, 48, 48, 1)
#convert the prediction labels into numerical vectors
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
print("dfffffffffff hfffffffffffff fddddddddddddddddddddd ghfffffffff",y_train.shape, y_test.shape)
print(x_train.shape)
nsamples, nx, ny,t = x_train.shape
x_train = x_train.reshape((nsamples,nx*ny))



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
print(model.summary())


# save best weights
checkpointer = ModelCheckpoint(filepath='face_model.h5', verbose=1, save_best_only=True)
print("dkj")
# num epochs
epochs = 50

# run model
##H = model.fit(x_train, y_train, epochs=50,
##                 shuffle=True,
##                 batch_size=100, validation_data=(x_test, y_test), verbose=2)
print("gdfdhfjhj")

# save model to json
model_json = model.to_json()
with open("face_model.json", "w") as json_file:
    json_file.write(model_json)
print ("Classification Report:")
y_pred = model.predict(x_test)
print (metrics.classification_report(y_test, y_pred))
print ("Confusion Matrix:")
print (metrics.confusion_matrix(y_test, y_pred))
from sklearn.metrics import accuracy_score

from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge
def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
    
    clf.fit(X_train, y_train)
    
    print ("Accuracy on training set:")
    print (clf.score(X_train, y_train))
    print ("Accuracy on testing set:")
    print (clf.score(X_test, y_test))
    
    y_pred = clf.predict(X_test)
    
    print ("Classification Report:")
    print (metrics.classification_report(y_test, y_pred))
    print ("Confusion Matrix:")
    print (metrics.confusion_matrix(y_test, y_pred))
    filename = 'face_model.sav'
    pickle.dump(clf, open(filename, 'wb'))



filename = 'face_model.sav'
pickle.dump(clf, open(filename, 'wb'))
print ("Training Completed")
import random
import numpy as np
import matplotlib.pyplot as plt 
N=epochs
plt.plot(np.arange(0, N), H.history['loss'], label="Training Loss")
#plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history['val_loss'], label="Validation Loss")
#plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
#plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Accuracy")
plt.legend(loc="lower left")
plt.savefig("loss.png")
plt.show()
plt.plot(np.arange(0, N), H.history['acc'], label="Training Accuracy")
#plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history['val_acc'], label="Validation Accuracy")
#plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
#plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Accuracy")
plt.legend(loc="lower left")
plt.savefig("acc.png")
plt.show()
