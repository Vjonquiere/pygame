import pygame, sys
from pygame.locals import *
import variables
import oulo
clock = pygame.time.Clock()

ecran = (720,480)
FPS = 60

pygame.init()
pygame.display.init()
fenetre = pygame.display.set_mode(ecran)

def test():
    variables.liste_ennemis.clear()
    variables.liste_gouttes.clear()
    while True :
        if variables.win == False:
            back = pygame.transform.scale(pygame.image.load('background.png'), (720,480))
            fenetre.blit(back, (0, 0))
        if variables.win == True:
            we = pygame.transform.scale(pygame.image.load('background2.png'), (720,480))
            fenetre.blit(we, (0, 0))           
        keys=pygame.key.get_pressed()
        if keys[K_SPACE]:
               oulo.real_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
                              
        pygame.display.flip()    
        clock.tick(FPS)
