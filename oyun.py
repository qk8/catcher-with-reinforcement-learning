#import os
#os.environ['SDL_VIDEODRIVER']='dummy'




import pygame
import random


displayWidth = 1200
displayHeight = 800

display = pygame.display.set_mode((displayWidth,displayHeight))

stateSize = 2
actionSize = 3

class Player:
    def __init__(self):
        self.image = pygame.image.load("monster.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = displayWidth/2
        self.rect.bottom = displayHeight
        self.speedx = 0

    def draw(self):
        display.blit(self.image, self.rect)
        
    def move(self, action):
        if action == 0:
            self.speedx = 0
        elif action == 1:
            self.speedx = -10
        elif action == 2:
            self.speedx = +10
         
        self.rect.x +=self.speedx
        
        if self.rect.right > displayWidth:
            self.rect.right = displayWidth
        if self.rect.left < 0:
            self.rect.left = 0
            
    
class Candy:
    def __init__(self):
        self.image = pygame.image.load("candy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, displayWidth - self.rect.width)
        self.rect.y = -self.rect.h
        self.speedy = 5

    def draw(self):
        display.blit(self.image, self.rect)
    
    def moveAndControl(self, playerRect):
        self.rect.y += self.speedy


        if self.rect.colliderect(playerRect):
            self.rect.x = random.randrange(0, displayWidth - self.rect.width)
            self.rect.y = -self.rect.h
            return 'success'
        elif self.rect.top > displayHeight:
            return 'fail'
        
        
            
 
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    
    def reset(self):

        self.score = 0

        self.done = False
        
        self.player = Player()
        self.candy = Candy()
        
    
        state = []


        state.append(self.candy.rect.centerx-self.player.rect.centerx)
        state.append(self.candy.rect.y-self.player.rect.y)
        

        return state
        
    
    def step(self, action):

        reward = 0
        
        self.player.move(action)

        result = self.candy.moveAndControl(self.player.rect)

        if result == 'success':
            reward = +100
            self.score += 1

        elif result == 'fail':
            reward = -100
            self.done = True

        nextState = []

        nextState.append(self.candy.rect.centerx-self.player.rect.centerx)
        nextState.append(self.candy.rect.y-self.player.rect.y)

        display.fill((0,191,255))

        self.player.draw()
        self.candy.draw()

        pygame.display.set_caption("SCORE: " + str(self.score))

        pygame.display.update()

        self.clock.tick(60) 
        
        return reward, nextState, self.done
         
    















    