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

class Displayable:
    
    def __init__(self, taille_x = 720, taille_y = 480, x = 0, y = 0):
        self.font = pygame.font.Font('ConcertOne-Regular.ttf', 25)
        self.taille_x = taille_x 
        self.taille_y = taille_y
        self.x = x
        self.y = y
        
    def text(self, text):
        label = self.font.render(text, 1, (255,255,0))
        fenetre.blit(label, (self.x, self.y))
        
    def image(self, img):
        en_number = pygame.transform.scale(pygame.image.load(img), (self.taille_x, self.taille_y))
        fenetre.blit(en_number, (self.x, self.y))
        
def key_pressed(key_pres):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.key_pres:
            variables.nb_gouttes += 1
            
icon = Displayable(64,64)
t = Displayable()

while True:
    img_background = pygame.transform.scale(pygame.image.load('back.jpg'), (720,480))
    fenetre.blit(img_background, (0, 0))

    t.text("test")
    t.text("rtt")
    icon.image("l.png")
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