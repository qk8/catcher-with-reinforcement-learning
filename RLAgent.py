import random
import numpy
import collections
import NeuralNetwork







class Agent:
    
    def __init__(self, stateSize, actionSize):

        self.stateSize = stateSize
        self.actionSize = actionSize
        self.miniBatchSize = 32
        self.learningRate = 0.00025
        self.discountFactor = 0.99
        self.replayMemorySize = 100000
        self.replayStartSize = 50000
        self.exploration = 1.0
        self.explorationDecay = 0.999
        self.explorationMin = 0.1


        self.model = NeuralNetwork.buildModel(self.stateSize, self.actionSize, self.learningRate)

        self.replayMemory = collections.deque(maxlen=self.replayMemorySize)

        
    
    
    #SORUNNNNNNNNNNNNNNNNN ACTION > 4
    def action(self, state):
        #if random.random() < self.exploration:
        if False:
            action =  random.randrange(self.actionSize)
            print("RND: ",action)
            return action
        else:
            QValues = self.model.predict(state)
            #print('QVALUES SHAPE: ',QValues.shape)
            action = numpy.argmax(QValues)
            print("NN: ",action)
            return action
    
    def experienceStorage(self, state, action, reward, nextState, done):
        self.replayMemory.append((state, action, reward, nextState, done))
        


    def experienceReplay(self):
        if len(self.replayMemory) < self.replayStartSize:
            return
        miniBatch = random.sample(self.replayMemory, self.miniBatchSize)
        
        for state, action, reward, nextState, done in miniBatch:
            target = self.model.predict(state)
            if done:
                target[0][action] = reward
            else:
                target[0][action] = reward + self.discountFactor*numpy.amax(self.model.predict(nextState))
            
            self.model.fit(state, target, epochs=1, verbose=0)

    
    def adaptiveExploration(self):
        if self.exploration > self.explorationMin:
            self.exploration *= self.explorationDecay


    def saveWeights(self, name):
        self.model.save_weights(name, overwrite = True)

    def loadWeights(self, name):
        self.model.load_weights(name)






