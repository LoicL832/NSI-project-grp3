#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 00:11:38 2020

@author: loiclamour
"""

import pygame
import math

pygame.init()
running = True 
game = False


while running :
    pygame.display.set_caption("Calcul mental ")
    screen = pygame.display.set_mode((1600,900))
    background = pygame.image.load('assets/bg2.jpg')
    play_button = pygame.image.load('assets/bouton.png')
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width()/3.33)
    play_button_rect.y = math.ceil(screen.get_height()/3)
    screen.blit(background,(0,0))
    screen.blit(play_button,play_button_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            running= False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if play_button_rect.collidepoint(event.pos) :
                game = True
                running=False
                
                
                
                
                
while game : 
    screen2 = pygame.display.set_mode((1920,1080))
    background = pygame.image.load('assets/bg3.jpg')
    screen.blit(background,(0,0))
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    varText = ""
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render(varText, True, green,blue)
    textRect = text.get_rect()
    textRect.center = (960, 540)
    screen2.blit(text, textRect)
    calcul = font.render('3 * 3', True, green, blue)
    calculRect = calcul.get_rect()
    calculRect.center = (960,200)
    screen2.blit(calcul, calculRect)
    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            game = False
            running= False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            varText = varText + pygame.key.name(event.key)
            print(varText)
    
            
            
            

        

