import pygame, sys
import time
from pygame.locals import *
from random import randint
clock = pygame.time.Clock()

ecran = (720,480)
FPS = 60

pygame.init()
pygame.display.init()
fenetre = pygame.display.set_mode(ecran)

def cheh():
    while True :
        fenetre.fill([0,0,0])
        
        keys=pygame.key.get_pressed() 
        if keys[K_LEFT]:
           print("e")
        if keys[K_RIGHT]:
           print("b")
        if keys[K_UP]:
           print("n")
        if keys[K_DOWN]:
           print("w")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
                
               
        pygame.display.flip()    
        clock.tick(FPS)
cheh()