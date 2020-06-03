import pygame
import random
import math

pygame.display.set_caption("SUPER JEU DE OUF")
background = pygame.image.load("assets/bg.jpg")
(width, height) = (1920, 1080)
win = pygame.display.set_mode((width, height))
pygame.display.update()
selection = ""
gagne = pygame.image.load('assets/gagné.png')
perdu = pygame.image.load('assets/perdu.png')
perdu_rect= perdu.get_rect
gagne_rect=gagne.get_rect

class button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        # Call this method to draw the button on the screen
        pygame.draw.rect(win, (self.x, self.y, self.width, self.height), 0)

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def gagné():
    win.blit(gagne, (gagne_rect))
    button_ciseaux == pygame.image.load("assets/clear.png")
    button_pierre == pygame.image.load('assets/clear.png')
    button_feuille == pygame.image.load("assets/clear.png")
    selection == ""
    selection_ordi == ""


def perdu():
    win.blit(perdu, (0, 0))
    button_ciseaux == pygame.image.load("assets/clear.png")
    button_pierre == pygame.image.load('assets/clear.png')
    button_feuille == pygame.image.load("assets/clear.png")
    selection == ""
    selection_ordi == ""


def pierre_feuille_ciseaux():
    if selection_ordi == "Pierre" and selection == "Ciseaux":
        perdu()
    if selection_ordi == "Feuille" and selection == "Pierre":
        perdu()
    if selection_ordi == "Ciseaux" and selection == "Feuille":
        perdu()
    if selection == "Pierre" and selection_ordi == "Ciseaux":
        gagné()
    if selection == "Feuille" and selection_ordi == "Pierre":
        gagné()
    if selection == "Ciseaux" and selection_ordi == "Feuille":
        gagné()


class button_pierre(object):
    def __init__(self):
        self.image = pygame.image.load('assets/pierre.png').convert_alpha()
        self.image_scale = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class button_feuille(object):
    def __init__(self):
        self.image = pygame.image.load('assets/feuille.png').convert_alpha()
        self.image_scale = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10


class button_ciseaux(object):
    def __init__(self):
        self.image = pygame.image.load('assets/ciseaux.png').convert_alpha()
        self.image_scale = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100


# def button_cliqué():
# if event.type == pygame.MOUSEBUTTONDOWN and event.button_pierre == 1:
#   return selection=="Pierre"
# if event.type == pygame.MOUSEBUTTONDOWN and event.button_feuille == 1:
#     return selection=="Feuille"
# if event.type == pygame.MOUSEBUTTONDOWN and event.button_ciseaux == 1:
#     return selection=="Ciseaux"
# class Bouton:
# def __init__(self, window, pos, image):
#  self.image = pygame.image.load(image).convert_alpha()
#   self.rect = self.image.get_rect()
#   self.rect.x = pos[0] * window.get_rect().w
#   self.rect.y = pos[1] * window.get_rect().h
#   self.window = window

button_ciseaux = pygame.image.load('assets/ciseaux.png')
button_pierre = pygame.image.load('assets/pierre.png')
button_feuille = pygame.image.load('assets/feuille.png')
button_feuille = pygame.transform.scale(button_feuille, (400, 150))
button_feuille_rect = button_feuille.get_rect()
button_feuille_rect.x = math.ceil(win.get_width() / 3.33)
button_feuille_rect.y = math.ceil(win.get_height() / 2)
button_pierre = pygame.transform.scale(button_pierre, (400, 150))
button_pierre_rect = button_pierre.get_rect()
button_pierre_rect.x = math.ceil(win.get_width() / 2)
button_pierre_rect.y = math.ceil(win.get_height() / 2)
button_ciseaux = pygame.transform.scale(button_ciseaux, (400, 150))
button_ciseaux_rect = button_ciseaux.get_rect()
button_ciseaux_rect.x = math.ceil(win.get_width() / 6)
button_ciseaux_rect.y = math.ceil(win.get_height() / 2)
# button_ciseaux= pygame.transform.scale(button_ciseaux, (100,100))
# Bouton_ciseaux= Bouton(screen,(0.1,0.5), 'assets/ciseaux.png')
formes_ordi = ["Pierre", "Feuille", "Ciseaux"]
selection_ordi = formes_ordi[random.randint(0, 2)]
# def redrawwindow():
# win.fill((255,255,255))
# button_f.draw(win)
# win.blit(button_feuille_scale,(0,300))
running = True
# button_f=button(0,300,250,100)
while running:
    win.blit(background, (0, 0))
    pygame.display.update()
    win.blit(button_pierre, button_pierre_rect)
    win.blit(button_ciseaux, button_ciseaux_rect)
    win.blit(button_feuille, button_feuille_rect)
    # button_feuille.show(events, selection= "feuille")
    # Bouton_ciseaux.show(events, selection="ciseaux")
    print(selection)
    print(selection_ordi)
    # if selection_ordi=="Ciseaux":
    #  screen.blit(button_ciseaux_scale,(0,0))
    # if selection_ordi == "Pierre":
    #    screen.blit(button_pierre_scale,(100,0))
    # if selection_ordi == "Feuille":
    #    screen.blit(button_feuille_scale,(200,0))
    pygame.display.flip()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_feuille_rect.collidepoint(event.pos):
                selection = "Feuille"
            if button_pierre_rect.collidepoint(event.pos):
                selection = "Pierre"
            if button_ciseaux_rect.collidepoint(event.pos):
                selection = "Ciseaux"
            # if button_f.isOver(pos):
            # print("vous avez selectionné la feuille")
            # if event.type == pygame.MOUSEMOTION:
            #    if button_f.isOver(pos):
            #      button_f.color = (0,250,0)
            #    else:
            #      button_f.color =(0,0,0)
        pierre_feuille_ciseaux()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
