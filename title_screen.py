import pygame
import variables
from pygame.locals import *
import sys
import Structure
ecran = (720,480)
FPS = 60
pygame.init()
pygame.display.init()
fenetre = pygame.display.set_mode(ecran)
clock = pygame.time.Clock()
variables.nb_gouttes = 8

def key_pressed(key_pres):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.key_pres:
            variables.nb_gouttes += 1
while True:
    img_background = pygame.transform.scale(pygame.image.load('back.jpg'), (720,480))
    fenetre.blit(img_background, (0, 0))
    font7 = pygame.font.Font('ConcertOne-Regular.ttf', 25)
    label = font7.render(str(variables.nb_gouttes), 1, (255,255,0))
    fenetre.blit(label, (660, 0))
    en_number = pygame.transform.scale(pygame.image.load('l.png'), (64,64))
    fenetre.blit(en_number, (100, 100))
    if pygame.mouse.get_pos() <= (100,100) and pygame.mouse.get_pressed()[0]:
        print("y")
        variables.nb_gouttes += 1
    keys=pygame.key.get_pressed() 
    if keys[K_LEFT]:
        Structure.run_game()
    if keys[K_h]:
        key_pressed(K_h)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
                
    pygame.display.flip()    
    clock.tick(FPS)