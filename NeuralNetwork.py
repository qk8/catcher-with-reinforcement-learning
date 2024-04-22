import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"



from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam


        
def buildModel(stateSize, actionSize, learningRate):
    
    model = Sequential()
    model.add(Dense(48, input_dim = stateSize, activation = "tanh"))
    model.add(Dense(actionSize, activation = "linear"))

    adam = Adam(lr=learningRate)
    model.compile(loss = "mse", optimizer = adam)

    return model
   







