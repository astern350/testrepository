#Chapter 2
#ST
#Updated 24/11/16
#fonts.py

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Font goes here', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

while True:
    for event in pygame.event.get():
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        
        if event.type == QUIT:  #if pressing X exit the program - other event checks go here!
            pygame.quit()
            sys.exit()
    pygame.display.update()
