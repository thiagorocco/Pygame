import pygame
from pygame.locals import *
from sys import exit


pygame.init()


largura = 640
altura = 480
titulo = 'Meu Primeiro Jogo com Pygame'


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(titulo)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    ## Desenhando na tela

    posRectX = 200
    posRectY = 300
    largRect = 40
    altRect = 50
    rgbRect = (255, 0, 0)

    posCircleX = 300
    posCircleY = 100
    raioCircle = 20
    rgbCircle = (0, 150, 255)


    pygame.draw.rect( tela, rgbRect, (posRectX, posRectY, largRect, altRect))
    pygame.draw.circle(tela, rgbCircle, (posCircleX, posCircleY), raioCircle)

    pygame.display.update()