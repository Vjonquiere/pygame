import pygame, sys, time
from pygame.locals import *
from random import randint
import variables
clock = pygame.time.Clock()

ecran = (720,480)
FPS = 60

taille_goutte = 10
variables.nb_gouttes = 8

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
            v_sprite = pygame.transform.scale(pygame.image.load('images/left.png'), (20,20))
        if self.direction == "right":
            v_sprite = pygame.transform.scale(pygame.image.load('images/right.png'), (20,20))
        if self.direction == "up":
            v_sprite = pygame.transform.scale(pygame.image.load('images/up.png'), (20,20))
        if self.direction == "down":
            v_sprite = pygame.transform.scale(pygame.image.load('images/down.png'), (20,20))
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

    def chrono(self):
        real_time = round(time.time() - variables.chronometre, 2)
        label = self.font.render(str(real_time), 1, (255,255,0))
        fenetre.blit(label, (660, 0))

    def freeze_time(self):
        real_time = round(variables.end_time - variables.chronometre, 2)
        label = self.font2.render("time : " + str(real_time), 1, (255,255,0))
        fenetre.blit(label, (240, 300))
class End_game():
    def __init__(self):
        self.win = variables.win
    
    def win_status_display(self):
        replay_message = font7.render("appuyer sur 'espace' pour rejouer", 1, (255,255,0))
        fenetre.blit(replay_message, (175, 400))
        font7 = pygame.font.Font('ConcertOne-Regular.ttf', 25)
        back = pygame.transform.scale(pygame.image.load('back.jpg'), (720,480))
        fenetre.blit(back, (0, 0))
        variables.overlay.freeze_time()
        if self.win :
            message = font7.render("you win", 1, (255,255,0))
            fenetre.blit(message, (270, 100))
            icon = pygame.transform.scale(pygame.image.load('icons8-trophy-64.png'), (75,75))
            fenetre.blit(icon, (310, 175))
        else:
            message = font7.render("you lose", 1, (255,255,0))
            fenetre.blit(message, (270, 100))
            icon = pygame.transform.scale(pygame.image.load('icons8-sad-64.png'), (75,75))
            fenetre.blit(icon, (310, 175))
            

def real_game():
    variables.chronometre = time.time()
    player = Vaisseau()
    variables.liste_ennemis = []
    variables.liste_gouttes = []
    variables.overlay = Outils()
    for k in range(variables.nb_gouttes):
        variables.liste_gouttes.append(Goutte(10+k*ecran[0]//variables.nb_gouttes))
    while True :
        fenetre.fill([0,0,0])
        variables.overlay.chrono()

        for g in variables.liste_gouttes:
            g.move()
            g.draw()

        for e in variables.liste_ennemis:
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

        for g in variables.liste_gouttes:
            if (player.x-g.x)**2 + (player.y-g.y)**2 < (player.taille + g.taille)**2:
                g.alive = False
                variables.liste_ennemis.append(Ennemi())

        for e in variables.liste_ennemis:
            if (player.x-e.x)**2 + (player.y-e.y)**2 < (player.taille + e.taille)**2:
                variables.win = False
                end_game()

        for g in variables.liste_gouttes :
            if g.alive == False :
                variables.liste_gouttes.remove(g)


        if len(variables.liste_gouttes) == 0 :
            variables.win = True
            end = time.time()
            print(round(end - variables.chronometre, 2))
            end_game()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()


        pygame.display.flip()
        clock.tick(FPS)

def end_game():
    variables.liste_ennemis.clear()
    variables.liste_gouttes.clear()
    variables.end_time = time.time()
    while True :
        font = pygame.font.SysFont("arial", 48)
        font7 = pygame.font.Font('ConcertOne-Regular.ttf', 25)
        back = pygame.transform.scale(pygame.image.load('back.jpg'), (720,480))
        fenetre.blit(back, (0, 0))
        replay_message = font7.render("appuyer sur 'espace' pour rejouer", 1, (255,255,0))
        fenetre.blit(replay_message, (175, 400))
        if variables.win == False:
            lose_message = font.render("you lose", 1, (255,255,0))
            fenetre.blit(lose_message, (270, 100))
            icon = pygame.transform.scale(pygame.image.load('icons8-sad-64.png'), (75,75))
            fenetre.blit(icon, (310, 175))
            variables.overlay.freeze_time()
        if variables.win == True:
            lose_message = font.render("you win", 1, (255,255,0))
            fenetre.blit(lose_message, (270, 100))
            icon = pygame.transform.scale(pygame.image.load('icons8-trophy-64.png'), (75,75))
            fenetre.blit(icon, (310, 175))
            variables.overlay.freeze_time()

        keys=pygame.key.get_pressed()
        if keys[K_SPACE]:
               real_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)
