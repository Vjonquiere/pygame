import pygame, sys, time
from pygame.locals import *
from random import randint
import variables
from pygame import overlay



class Goutte :
    def __init__(self, posx):
        self.x = posx
        self.y = 0
        self.dy = randint(5, 10)
        self.color = (255, 0, 0)
        self.taille = variables.taille_goutte
        self.alive = True

    def move(self):
        self.y += self.dy
        if self.y >= 480 :
            self.dy = -self.dy
        elif self.y <= 0 :
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(variables.fenetre,self.color,(self.x,self.y),self.taille)



class Vaisseau:
    def __init__(self):
        self.x = 40
        self.y = variables.ecran[1] // 2
        self.color = (200,200,200)
        self.taille = variables.taille_vaisseau
        self.direction = "left"

    def draw(self) :
        if self.direction == "left":
            v_sprite = pygame.transform.scale(pygame.image.load('images/left.png'), (20,20))
        if self.direction == "right":
            v_sprite = pygame.transform.scale(pygame.image.load('images/right.png'), (20,20))
        if self.direction == "up":
            v_sprite = pygame.transform.scale(pygame.image.load('images/up.png'), (20,20))
        if self.direction == "down":
            v_sprite = pygame.transform.scale(pygame.image.load('images/down.png'), (20,20))
        variables.fenetre.blit(v_sprite, (self.x, self.y))

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
        pygame.draw.circle(variables.fenetre,(0,0,255),(self.x,self.y),self.taille)

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
        self.font = pygame.font.Font('ConcertOne-Regular.ttf', 25)
        self.font1 = pygame.font.Font('ConcertOne-Regular.ttf', 50)
        self.replay_message = self.font.render("appuyer sur 'espace' pour rejouer", 1, (255,255,0))
        self.quit_message = self.font.render("appuyer sur 'm' pour revenir au menu", 1, (255,255,0))
        
    def chrono(self):
        real_time = round(time.time() - variables.chronometre, 2)
        label = self.font.render(str(real_time), 1, (255,255,0))
        variables.fenetre.blit(label, (660, 0))

    def freeze_time(self):
        real_time = round(variables.end_time - variables.chronometre, 2)
        label = self.font1.render("time : " + str(real_time) + " sec", 1, (255,255,0))
        variables.fenetre.blit(label, (195, 300))
    
    def routine_pygame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                variables.quit = 1
                pygame.display.quit()
                sys.exit()

        pygame.display.flip()
        variables.clock.tick(variables.FPS)
    
    def end_game(self):
        variables.liste_ennemis.clear()
        variables.liste_objectifs.clear()

        while True:
            back = pygame.transform.scale(pygame.image.load('back.jpg'), (720,480))
            variables.fenetre.blit(back, (0, 0))
            variables.fenetre.blit(self.quit_message, (145, 435))
            variables.fenetre.blit(self.replay_message, (175, 400)) 
            variables.overlay.freeze_time()
            if variables.win :
                message = self.font1.render("You Win", 1, (255,255,0))
                variables.fenetre.blit(message, (270, 100))
                icon = pygame.transform.scale(pygame.image.load('icons8-trophy-64.png'), (75,75))
                variables.fenetre.blit(icon, (320, 190))
            else:
                message = self.font1.render("You Lose", 1, (255,255,0))
                variables.fenetre.blit(message, (270, 100))
                icon = pygame.transform.scale(pygame.image.load('icons8-sad-64.png'), (75,75))
                variables.fenetre.blit(icon, (320, 190))
             
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]:
                   real_game()
            if keys[K_m]:
                   pygame.quit()
            variables.overlay.routine_pygame()


def collision_objectif(player):
    for g in variables.liste_objectifs:
        if (player.x-g.x)**2 + (player.y-g.y)**2 < (player.taille + g.taille)**2:
            g.alive = False
            variables.liste_ennemis.append(Ennemi())
                
def collision_ennemi(player):
    for e in variables.liste_ennemis:
        if (player.x-e.x)**2 + (player.y-e.y)**2 < (player.taille + e.taille)**2:
            variables.win = False
            variables.end_time = time.time()
            variables.overlay.end_game()
                
def real_game():
    variables.chronometre = time.time()
    player = Vaisseau()
    variables.liste_ennemis = []
    variables.liste_objectifs = []
    variables.overlay = Outils()
    
    for k in range(variables.nb_objectifs):
        variables.liste_objectifs.append(Goutte(10+k*variables.ecran[0]//variables.nb_objectifs))
    if variables.nb_player == 2:
        player2 = Vaisseau()
    while True :
        variables.fenetre.fill([0,0,0])
        variables.overlay.chrono()

        for g in variables.liste_objectifs:
            g.move()
            g.draw()

        for e in variables.liste_ennemis:
            e.move()
            e.draw()

        player.draw()
        player.collision()
        collision_ennemi(player)
        collision_objectif(player)
        
        if variables.nb_player == 2:
            player2.draw()
            player2.collision()
            collision_objectif(player2)
            collision_ennemi(player2)
            
        if variables.nb_player == 2:
            keys=pygame.key.get_pressed()
            if keys[K_q]:
               player2.x -= 5
               player2.direction = "left"
            if keys[K_d]:
               player2.x += 5
               player2.direction = "right"
            if keys[K_z]:
               player2.y -= 5
               player2.direction = "up"
            if keys[K_s]:
               player2.y += 5
               player2.direction = "down"
               
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


        


        for g in variables.liste_objectifs :
            if g.alive == False :
                variables.liste_objectifs.remove(g)


        if len(variables.liste_objectifs) == 0 :
            variables.end_time = time.time()
            variables.win = True
            end = time.time()
            print(round(end - variables.chronometre, 2))
            variables.overlay.end_game()


        variables.overlay.routine_pygame()



def launch_game():
    variables.clock = pygame.time.Clock()
    
    variables.ecran = (720,480)
    variables.FPS = 60

    variables.taille_goutte = 10

    variables.taille_vaisseau = 20
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption('Galaxy War')
    variables.fenetre = pygame.display.set_mode(variables.ecran)
    real_game()

