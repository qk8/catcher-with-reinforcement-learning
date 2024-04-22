import oyun
import RLAgent
import numpy

from os.path import exists

agent = RLAgent.Agent(oyun.stateSize, oyun.actionSize)
game = oyun.Game()



episodes = 99999999


if exists('YakalamaANNmodel_weights.h5'):
    agent.loadWeights('YakalamaANNmodel_weights.h5')



for episode in range(episodes):

    state = game.reset()

    state = numpy.reshape(state, [1, oyun.stateSize])

    state = state/(2*oyun.displayWidth)




    totalReward = 0
    while True:

    
        action = agent.action(state)

        reward, nextState, done = game.step(action)

        nextState = numpy.reshape(nextState, [1, oyun.stateSize])

        nextState = nextState/(2*oyun.displayWidth)

            
        

        agent.experienceStorage(state, action, reward, nextState, done)
        
        

        #agent.experienceReplay()
        

        agent.adaptiveExploration()
        

        state = nextState



        totalReward += reward

        
        """
        
        
        if totalReward % 2000 == 0:
            totalReward += 100
            agent.saveWeights('YakalamaANNmodel_weights.h5')

        """

        print('TOTAL REWARD: ',totalReward)
        
        


        if done:
            
            print('Episode: ', episode, ' Total Reward: ', totalReward)
            break







