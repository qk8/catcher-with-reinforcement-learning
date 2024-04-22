import oyun
import numpy


game = oyun.Game()

coordinates = game.reset()

print(coordinates)

coordinates = numpy.reshape(coordinates, [1, oyun.stateSize])

print(coordinates)

coordinates = coordinates/(2*oyun.displayWidth)

print(coordinates)


#state = numpy.concatenate((state, state, state, state))

#print(state.shape)

#print(state)

#state = numpy.concatenate(([1,1,1], state[:36]))


#print(state.shape)

#print(state)



#input()


