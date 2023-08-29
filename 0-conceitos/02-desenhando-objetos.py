import pygame
from pygame.locals import *
from sys import exit

class Linha:
    def __init__(self, tela, cor, posIniXY, posFimXY, larg):
        pygame.draw.line(tela, cor, posIniXY, posFimXY, larg)

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

    #propriedades do retângulo
    posRectX = 200
    posRectY = 300
    largRect = 40
    altRect = 50
    rgbRect = (255, 0, 0)

    #propriedades do círculo
    posCircleX = 300
    posCircleY = 100
    raioCircle = 20
    rgbCircle = (0, 150, 255)

    #propriedades da linha
    rgbLinha = (255, 255, 0)
    posLinhaInicioXY = (390, 10)
    posLinhaFimXY = (390, 400)
    larguraLinha = 5

    pygame.draw.rect( tela, rgbRect, (posRectX, posRectY, largRect, altRect))
    pygame.draw.circle(tela, rgbCircle, (posCircleX, posCircleY), raioCircle)
    l1 = Linha(tela,rgbLinha,posLinhaInicioXY, posLinhaFimXY,larguraLinha)
    l2 = Linha(tela,(0,255,100),(10,0),(10,500),20)
    l3 = Linha(tela,(255,50,100),(30,0),(30,500),20)
    l4 = Linha(tela,(15,255,255),(50,0),(50,500),20)

    pygame.display.update()