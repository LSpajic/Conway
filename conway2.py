from cgitb import grey
import time
import pygame
import numpy
from datetime import datetime
import os
import subprocess
import easygui



#treba napravit drugu matricu gdje cesspremat promjenute podatke
#
#
NUMBER_OF_FIELDS = 50
BLOCK_SIZE_PX = 20
matrix = numpy.zeros((NUMBER_OF_FIELDS+2,NUMBER_OF_FIELDS+2)).astype(int)
matrixtng = numpy.zeros((NUMBER_OF_FIELDS+2,NUMBER_OF_FIELDS+2)).astype(int)

def tng(matrica,x,y):
    trenvre = matrica[x][y]
    suma = matrica[x-1][y]+matrica[x+1][y] + matrica[x-1][y+1]+matrica[x+1][y+1] +matrica[x-1][y-1]+matrica[x+1][y-1] + matrica[x][y+1]+matrica[x][y-1]
    if trenvre == 0:
        if suma == 3:
            return 1
        return 0
    if suma>3:
        return 0
    if suma < 2:
        return 0
    return 1

yellow = ( 255, 166, 0)
black = (0,0,0)
dark_grey = (100,100,100)



width = NUMBER_OF_FIELDS * BLOCK_SIZE_PX + 200
height = NUMBER_OF_FIELDS * BLOCK_SIZE_PX
oneside = NUMBER_OF_FIELDS * BLOCK_SIZE_PX

pygame.init()

smallfont = pygame.font.SysFont('Corbel', 32)
text = smallfont.render('LOAD' , True , yellow)
text2 = smallfont.render('SAVE' , True , yellow)


screen = pygame.display.set_mode([width,height])

screen.fill(black)

pygame.draw.line(screen, yellow, (oneside,0),(oneside,oneside))

pygame.draw.rect(screen, dark_grey, [oneside+60, 100, 80 , 30])
pygame.draw.rect(screen, dark_grey, [oneside+60, 200, 80 , 30])

screen.blit(text, (oneside+60,100))
screen.blit(text2, (oneside+60,200))


pygame.display.flip()

running = True
catching = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                catching = False

    if catching:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 1060 <= pos[0] <= 1140 and 100 <= pos[1] <= 130:
                file = easygui.fileopenbox()
            if 1060 <= pos[0] <= 1140 and 200 <= pos[1] <= 230:
                print("stisnio si me 2")

            try:
                x = pos[0]//BLOCK_SIZE_PX
                y = pos[1]//BLOCK_SIZE_PX
                if event.button == 1:
                    matrix[x+1][y+1] = 1
                    pygame.draw.rect(screen, yellow, pygame.Rect(x * BLOCK_SIZE_PX, y * BLOCK_SIZE_PX , BLOCK_SIZE_PX-2, BLOCK_SIZE_PX-2))

                if event.button == 3:
                    matrix[x+1][y+1] = 0
                    pygame.draw.rect(screen, black, pygame.Rect(x * BLOCK_SIZE_PX, y * BLOCK_SIZE_PX , BLOCK_SIZE_PX-2, BLOCK_SIZE_PX-2))
            except IndexError:
                continue
            
    while not catching:
        for x in range(1,NUMBER_OF_FIELDS+1):
            for y in range(1,NUMBER_OF_FIELDS+1):
                nextstate = tng(matrix,x,y)
                matrixtng[x][y] = nextstate
                nextcolor = black if nextstate == 0 else yellow 

                pygame.draw.rect(screen, nextcolor, pygame.Rect((x-1) * BLOCK_SIZE_PX, (y-1) * BLOCK_SIZE_PX , 18, 18))


        pygame.display.flip()
        matrix = matrixtng
        matrixtng = numpy.zeros((NUMBER_OF_FIELDS+2,NUMBER_OF_FIELDS+2)).astype(int)
        catching = True


    pygame.display.flip()


pygame.quit()
