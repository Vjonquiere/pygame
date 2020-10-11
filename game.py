import pygame, sys
import time
from pygame.locals import *
from random import randint

clock = pygame.time.Clock()

ecran = (720,480)
FPS = 60

taille_goutte = 10
nb_gouttes = 8

taille_vaisseau = 20

pygame.init()
pygame.display.init()
fenetre = pygame.display.set_mode(ecran)


class Goutte :
    def __init__(self, posx): 
        self.x = posx
        self.y = 0
        self.dy = randint(5, 10)
        self.color = (255, 0, 0)
        self.taille = taille_goutte
        self.alive = True
  
    def move(self):
        self.y += self.dy
        if self.y >= 480 :
            self.dy = -self.dy
        elif self.y <= 0 :
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(fenetre,self.color,(self.x,self.y),self.taille)
        
       

class Vaisseau:
    def __init__(self):
        self.x = 40
        self.y = ecran[1] // 2
        self.color = (200,200,200)
        self.taille = taille_vaisseau
        self.direction = "left"
        
    def draw(self) :
        if self.direction == "left":
            v_sprite = pygame.transform.scale(pygame.image.load('left.png'), (20,20))
        if self.direction == "right":
            v_sprite = pygame.transform.scale(pygame.image.load('right.png'), (20,20))
        if self.direction == "up":
            v_sprite = pygame.transform.scale(pygame.image.load('up.png'), (20,20))
        if self.direction == "down":
            v_sprite = pygame.transform.scale(pygame.image.load('down.png'), (20,20))
        fenetre.blit(v_sprite, (self.x, self.y))
        
    def collision(self):
        if self.y >= 480 - self.taille:
            self.y -= 7
        elif self.y <= 0:
            self.y += 7
        if self.x >= 720 - self.taille:
            self.x -= 7
        elif self.x <= 0:
            self.x += 7
            
class Ennemi:
    def __init__(self):
        self.x = 0
        self.y = randint(10, 470)
        self.dy = randint(0, 7)
        self.dx = randint(0, 7)
        self.taille = 10
        
    def draw(self):
        pygame.draw.circle(fenetre,(0,0,255),(self.x,self.y),self.taille)
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y >= 480 :
            self.dy = -self.dy
        elif self.y <= 0 :
            self.dy = -self.dy
        if self.x >= 720 :
            self.dx = -self.dx
        elif self.x <= 0 :
            self.dx = -self.dx
            
class Outils:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 32)
        self.font2 = pygame.font.SysFont("impact", 64)
        self.win = None
        
    def chrono(self):
        real_time = round(time.time() - chrono, 2)  
        label = self.font.render(str(real_time), 1, (255,255,0))
        fenetre.blit(label, (660, 0))
        
    def clear_fenetre(self):
        liste_ennemis.clear()
        liste_gouttes.clear()
        fenetre.fill([0,0,0])
        
    def fenetre_fin(self):
        while True:
            keys=pygame.key.get_pressed()
            if keys[K_LEFT]:
               print("w")
            else :
                if self.win == True :
                    fin = self.font.render("you win", 1, (255,255,0))
                    fenetre.blit(fin, (280, 480//2))
                if self.win == False :
                    fin = self.font2.render("you lose", 1, (255,255,0))
                    fenetre.blit(fin, (280, 480//2))
                pygame.display.flip()
                clock.tick(FPS)
                fenetre.fill([0,0,0])
player = Vaisseau()
liste_ennemis = []
liste_gouttes = []
overlay = Outils()

for k in range(nb_gouttes):
    liste_gouttes.append(Goutte(10+k*ecran[0]//nb_gouttes))

chrono = time.time()

while True :
    fenetre.fill([0,0,0])
    
    overlay.chrono()
    
    for g in liste_gouttes:
        g.move()
        g.draw()
        
    for e in liste_ennemis:
        e.move()
        e.draw()
 
    player.draw()
    player.collision()
    
    
    keys=pygame.key.get_pressed() 
    if keys[K_LEFT]:
       player.x -= 5
       player.direction = "left"
    if keys[K_RIGHT]:
       player.x += 5
       player.direction = "right"
    if keys[K_UP]:
       player.y -= 5
       player.direction = "up"
    if keys[K_DOWN]:
       player.y += 5
       player.direction = "down"

    for g in liste_gouttes:
        if (player.x-g.x)**2 + (player.y-g.y)**2 < (player.taille + g.taille)**2:
            g.alive = False
            liste_ennemis.append(Ennemi())
            
    for e in liste_ennemis:
        if (player.x-e.x)**2 + (player.y-e.y)**2 < (player.taille + e.taille)**2:
            overlay.win = False
            overlay.clear_fenetre()
            overlay.fenetre_fin()

            
    for g in liste_gouttes :  
        if g.alive == False :
            liste_gouttes.remove(g)

    
    if len(liste_gouttes) == 0 :
        pygame.display.quit()
        end = time.time()
        print(round(end - chrono, 2))
        sys.exit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            
           
    pygame.display.flip()    
    clock.tick(FPS)